# Reference evapotranspiration (ETo)
This code generates FAO 56 - reference evapotranspiration using meteorological data. The code is a direct conversion of extension work from the University of Florida IFSA extension "Step by Step Calculation of the Penman-Monteith Evapotranspiration (FAO-56 Method)" into a python code. This paper to code conversion needed python packages like NumPy, math, and pandas.  

#### Input data for code:  
solor radiation - megaJoulePerMeterSquared  
Temperature min/max- celsius  
windspeed MeterPerSecond  
Relative humidity  
Altitude  
Julian date  
1 W/m2 = 0.0864 MJ/m2/day  

#### Output: Reference Evapotranspiration  
Hypothetical reference crop - crop height 0.12 m, surface resistance 70 s/m, and albedo of 0.23

Refrences: IFAS Extension 
[Step by step ET manual] (https://edis.ifas.ufl.edu/pdf/AE/AE45900.pdf)
[Relative humidity calculation] (https://www.seaford.k12.ny.us/cms/lib/NY01000674/Centricity/Domain/684/Dewpoint%20Relative%20Humidity%20How%20To.pdf)
