# Heart-Disease-Prediction
This repository contains the data analysis of 4 databases concerning heart disease diagnosis.

The data source:
     1. Cleveland Clinic Foundation (processed.cleveland.data)
     2. Hungarian Institute of Cardiology, Budapest (processed.hungarian.data)
     3. V.A. Medical Center, Long Beach, CA (processed.va.data)
     4. University Hospital, Zurich, Switzerland (processed.switzerland.data)

Each dataset has the same instance format with 14 attributes (original 76 attributes, here we use the processed version)
The authors of the databases have requested:
that any publications resulting from the use of the data include the names of the principal investigator responsible for the data collection at each institution.  They would be:
       1. Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
       2. University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
       3. University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
       4. V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.

The goal is to predict presence of heart disease in the patient, where the presence as 4 and no presence as 0.

#Number of Instances: 
        Database:    # of instances:
          Cleveland: 303
          Hungarian: 294
        Switzerland: 123
      Long Beach VA: 200

#Attribute Information:
   -- Only 14 used
      -- 1. #3  (age)       
      -- 2. #4  (sex)       
      -- 3. #9  (cp)        
      -- 4. #10 (trestbps)  
      -- 5. #12 (chol)      
      -- 6. #16 (fbs)       
      -- 7. #19 (restecg)   
      -- 8. #32 (thalach)   
      -- 9. #38 (exang)     
      -- 10. #40 (oldpeak)   
      -- 11. #41 (slope)     
      -- 12. #44 (ca)        
      -- 13. #51 (thal)      
      -- 14. #58 (num)       (the predicted attribute)
