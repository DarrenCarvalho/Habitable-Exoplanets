# Habitable-Exoplanets

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

1. Drop Columns with more than 50% Nan Values

2. Check Habitable Planets are discovered by which method

3. Define Constants (Solar Radii, Solar Luminosity, Stefan Boltzman Constant)

4. Impute Stellar Luminosity Values which had 84% Nan Values

5. Change Orbital Period ( Days to Years )

6. Transform Numerical to Gausian Dist:
	Transformations: ( LOG, LOG(1+VAL), Square, Inverse )

7. Drop Outlier Rows

8. Drop Nan Rows

9. qqplot and Boxplot to check Normality and Distribution

10. Label Encoding To categorical variables

11. Under Sampling ( Random Sample from '0' class )

12. Feature Selection ( Select K BEST )

13. Cross Validation Evaluation

14. Evaluation on test data
