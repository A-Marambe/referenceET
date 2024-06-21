# import libraries
#import numpy as np
import math
from math import pi, sin, cos, tan, atan, acos

# Tmax input
day_input = input("Enter: Day of the year in Julian day format - ")
tmax_input = input("Enter : Max Temperature - ")
tmin_input = input("Enter: Min Temperature - ")
slrd_input = input("Enter: Solar radiation - ")
windrun_input = input("Enter: WindRun - distance wind travel in a day - ")
lat_input = input("Enter - Location lat - ")
lon_input = input("Enter - Location lon - ")
print('*************** USER INPUT ENDS ************************')
# Converting the string input to an integer
tmax = int(tmax_input)
tmin = int(tmin_input)
slrd = int(slrd_input)
j = int(day_input)
# for wind
windrun = int(windrun_input)
windspeed = (windrun * 1000) / (24 * 60 * 60)
tmean = (tmax + tmin) / 2
# print all climate variables
print(f"for the {j} th day of the year\nmean temp is {tmean}\nsolar radiation is {slrd}\nwindspeed is {windspeed}\n ")
print('**************** Calculated penman variables *************')

# step 4 - Slope of saturation vapor pressure curve
term1 = ((17.27 * tmean) /(tmean + 237.3))
term2 = (tmean + 237.3) ** 2
ssvp = (4098 * (0.6108 * math.exp(term1))) / term2
print('slope of the saturated vapour pressure curve {}'.format(ssvp))

# step5  atmoshpere pressure in Kpa at a elevation Z (elevation above sea level m)
# atmosphere preseure affect ET but the 
z = 239
p = 101.3 * pow(((293 - 0.0065 * z) / 293), 5.26)
print(f'atmospheric pressure is {p}')

# step6 - Psychrometric constant  KPa / C
pc = 0.000665 * p
print(f'Psychrometric constant is {pc}')

# Step 7  Delta  term  - anxiliary calculation for radiation term
# it is relationship between psychromatric constant, slope of the vapour pressure curve and wind peed
dt = ssvp / (ssvp + (pc * (1+0.34 * windspeed)))
print('delta term is {}'.format(dt))

# step 8  - Psi term (auxialiary calculation for wind term)
pt = pc / (ssvp + (pc * (1+0.34 * windspeed)))
print(f'psi term is {pt}')

# step9 Temperature term (auxialiary calculation for wind term)
tt = (900/(tmean + 273)) * windspeed
print('temperature term {}'.format(tt))

# Step 10
# mean saturation vapor pressure using air temperature 
# et is satureation vapor pressure at the air temperature t in KPa
# the satureation air pressure is calcuated at the max temperature and min
# temperature for a day. The avarage it to take mean saturation vapor pressure

# fucntion to calculate saturate vapor pressure
def calculate_saturation_vapor_pressure(temp):
    term3 = (17.27 * temp) / (temp + 237.3)
    return 0.6108 * math.exp(term3)

# saturated vapor pressure at tmax
e_tmax = calculate_saturation_vapor_pressure(tmax)
# saturated vapor pressure at tmin
e_tmin = calculate_saturation_vapor_pressure(tmin)

# mean daily saturate vapor pressure
es = (e_tmax + e_tmin) / 2
print(f'saturated vapor pressure {es}')

# Step 11 - Actual vapor pressure in KPa, derived from relative humidity
# here we do not have RH measurements
# This data set absent the dew point temperature, therefore considering the 

# actural vaour pressure consider as the vapour pressure at the tmin
term4 = (17.27 * tmin) / (tmin + 237.3)
etmin = 0.6108 * math.exp(term4)
# based on available data
ea = etmin
print('actual vapor pressure {}'.format(ea))

# Step 12- The inverse relative distance between earth and sun
j = 201  # day of the year

# relative distance
term5 = (2 * pi / 365) * j
dr = 1 + (0.033 * cos(term5))
print('relative distance', dr)
# solar declination
declination = 0.409 * sin(term5 - 1.39)
print('solar declination', declination)


# Step 13 - conversion of latitude in degrees to radiance
lat, lon = 42.2278, 85.5200  # for Kalamazoo lat lon
# Conversion factor: pi divided by 180
pi_over_180 = pi / 180
# Convert latitude to radians
lat_rad = lat * pi_over_180
print('lat in radians', lat_rad)

# Calculate tangent of latitude in radians
term6 = tan(lat_rad)
# Calculate tangent of solar declination
term7 = tan(declination)
# Use arctangent for inverse tangent (alternative to arccos)
sun_hour_angle = acos((-term6 * term7))
print('solar hour angle is', sun_hour_angle)

# Step 15
# Extrateristral radiation (solor radiation incident outcide the earth atmosphere )
# solor constants
GSC = 0.0820
term9 = sun_hour_angle * sin(lat_rad) * sin(declination)
term10 = cos(lat_rad) * cos(declination) * sin(sun_hour_angle)
term11 = term9 + term10
ra = (24 * (60) / pi) * GSC * dr * term11
print('Extra terrestrial radiation is {}'.format(ra))

# Step 16  - Clear sky solor radiation
term12 = (2 * pow(10, -5)) * z
rso = (0.75+term12) * ra
print('clear sky radiation {}'.format(rso))

# step17 - Net solar radiation - shortwave radiation
rns = (1 -0.23) * slrd
print('Net solor radiation {}'.format(rns))

# step 18 - netout going long wave radiation
boltzman = 4.903 * pow(10, -9)
term13 = (pow((tmax+273.16), 4) + pow((tmin+273.16), 4)) / 2
term14 = (0.34 - 0.14) * math.sqrt(ea)
term15 = (1.35 * (slrd/rso)) - 0.35
rnl = boltzman * term13 * term14 * term15
print(f'Net out going long wave radiation is {rnl}')

# step 19
# net radiation
rn = rns - rnl
print('net radiation {}'.format(rn))

# net radiation equalant of evapotranspiration
rng = 0.408 * rn

# final step
et_rad = dt * rng
# print it
print("\n")
print('*** ET from radiation ***')
print(f'# {et_rad} #')



# wind term
et_wind = pt * tt * (es - ea)
print("\n")
print('*** ET from wind ***')
print(f'# {et_wind} #')


# Final reference ET value for hypothetical crop
eto = et_wind + et_rad

print("\n")
print("\n")
print('*** Penman reference ET is ***')
print('#######################################')
print(f'########### {eto} mm/day#############')
print('######################################')
print('evapotranspiration is {} mm/day and can be adjected with crop/vegetation factors'.format(eto))