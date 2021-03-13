# Heart-Disease-Prediction
This repository contains the data analysis of 4 databases concerning heart disease diagnosis.

The data source:
     1. Cleveland Clinic Foundation (processed.cleveland.data) \\
     2. Hungarian Institute of Cardiology, Budapest (processed.hungarian.data) \\
     3. V.A. Medical Center, Long Beach, CA (processed.va.data) \\
     4. University Hospital, Zurich, Switzerland (processed.switzerland.data)

Each dataset has the same instance format with 14 attributes (original 76 attributes, here we use the processed version)
The authors of the databases have requested:
that any publications resulting from the use of the data include the names of the principal investigator responsible for the data collection at each institution.  They would be:
       1. Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
       2. University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
       3. University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
       4. V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.

The goal is to predict presence of heart disease in the patient, where the presence as 4 and no presence as 0.

# Number of Instances: 
Database: # of instances:
1. Cleveland: 303
2. Hungarian: 294
3. Switzerland: 123
4. Long Beach VA: 200

# Attribute Information:  
  Only 14 used
  1. #3  age: age in years
  2. #4  sex: male=1; female=0      
  3. #9  cp: chest pain type (1= typical angina; 2= atypical angina; 3= non-anginal pain; 4= asymptomatic)      
  4. #10 trestbps: resting blood pressure (in mm Hg on admission to the hospital)
  5. #12 chol: serum cholestrol in mg/dl      
  6. #16 fbs: fasting blood sugar > 120 mg/dl (1= true; 0= false)     
  7. #19 restecg: resting ECG results (0= normal; 1= having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV))  
  8. #32 thalach: maximum heart rate achieved 
  9. #38 exang: exercise induced angina (1= Yes; 0= No)   
  10. #40 oldpeak: ST depression induced by exercise relative to rest 
  11. #41 slope: the slope of the peak exercise ST segment (1= upsloping; 2= flat; 3= downsloping)     
  12. #44 ca: number of major vessels (0-3) colored by flourosopy       
  13. #51 thal: 3= normal; 6= fixed defect; 7= reversable defect      
  14. #58 num: diagnosis of heart disease (angiographic disease status, 0= <50% diameter narrowing; 1= >50% diameter narrowing)(the predicted attribute)


# Overview

missing values represented with value -9.0
Class Distribution:
        Database:   |   0 | 1 | 2 | 3 | 4 | Total
          Cleveland: | 164 | 55 | 36 | 35 | 13 |  303
          Hungarian: | 188 | 37 | 26 | 28 | 15  | 294
        Switzerland: |  8 | 48 | 32 | 30  | 5  | 123
      Long Beach VA: | 51 | 56 | 41 | 42 | 10 | 200
