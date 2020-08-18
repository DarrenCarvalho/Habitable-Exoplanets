# Habitable-Exoplanets

## Heroku model deployment url:

https://exoplanets-api.herokuapp.com/

## Feature Details

Pl_HOSTNAME – Star Name

PL_NAME – Name of the Planet 

PL_DISCMETHOD – Planet Discovery Method

PL_ORBPER – Planet Orbital Period (In Earth Days)

PL_RADJ – Planet Radius ( In terms of Jupiter)

ST_DIST – Distance to Star ( pc (1pc = 3.26156 ly))

ST_TEFF – Temperature of Star (K)

ST_RAD – Radius of Star ( In terms of Solar Radii )

ST_LUM – Luminosity of Star ( Log(Solar) )

## Flow OF Code

1. Drop Columns with more than 50% Nan Values.

2. Check Habitable Planets are discovered by which method (Count Plot).

3. Define Constants (Solar Radii, Solar Luminosity, Stefan Boltzman Constant).

4. Impute Stellar Luminosity Values which had 84% Nan Values.

5. Transform Numerical to Gausian Dist:
	Transformations: ( LOG, LOG(1+VAL), Square, Inverse ).

6. Drop Outlier Rows.

7. Drop Nan Rows.

9. qqplot and Boxplot to check Normality and Distribution.

10. Drop pl_hostname, pl_name and perform One Hot Encoding on pl_discmethod.

11. Up Sampling using SMOTE.

13. Cross Validation Evaluation.

14. Evaluation on test data.

15. Feature Creation : inner_radius and outer radius of habitable zones, binning st_temp as per stelar type 
