import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

load_diabetes=pickle.load(open("Diabetes_Classifier.sav","rb"))
#load_lung=pickle.load(open(r"C:\Users\DELL\Desktop\AI_ML_DL\ML_Streamlit\Multi_Disease_Prediction_App\Lung_Cancer_Classifier_new.sav","rb"))
load_heart=pickle.load(open("Heart_Disease_Classifier.sav","rb"))




def diabetes_prediction(ip1):
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
        ip1=np.asarray(ip1)
        ip1=ip1.reshape(1,-1)
        prediction1=load_diabetes.predict(ip1)

        if prediction1[0]==1:
            st.write("Patient is Diabetic")
        else:
            st.write("Patient is healthy")
        
        
def heart_prediction(ip2):
        #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
        ip2=np.asarray(ip2)
        ip2=ip2.reshape(1,-1)
        prediction2= load_heart.predict(ip2)
        
        if prediction2==1:
            st.write("Patient has Heart Disease")
        else:
            st.write("Patient is healthy")
        
        

        
        
def main():
    st.sidebar.title("Pages")
    page = st.sidebar.radio("",["Home","Predictions"],index=0)
    if page=="Home":
        st.title("MULTIPLE DISEASE PREDICTION SYSTEM")
        #image=Image.open(r"C:\Users\DELL\Desktop\AI_ML_DL\ML_Streamlit\Multi_Disease_Prediction_App\cover.jpeg")
        st.image("cover.jpeg",width=750)
        
   
    disease=""
    if page=="Predictions":
        st.sidebar.subheader("Select Disease")
        disease = st.sidebar.selectbox("",["Diabetes","Heart Disease"])



#DIABETES
    if disease=="Diabetes":
        #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
          st.title("Diabetes Prediction")
          p=st.slider("Pregnancies",0,17,2)
          g=st.slider("Glucose",0,199,120)
          bp=st.slider("Blood Pressure",0,122,69)
          ST=st.slider("SkinThickness",0,100,20)
          i=st.slider("Insulin",0,846,79)
          BMI=st.slider("BMI",0.0,68.0,32.0)
          dpf=st.slider("DiabetesPedigreeFunction",0.070,2.5,0.47)
          age=st.slider("Age",21,81,21)
      
          if st.button("Result"):
              st.write("Result :")
              r=diabetes_prediction([p,g,bp,ST,i,BMI,dpf,age])
              #st.success(r)
     
        
#HEART DISEASE
    if disease=="Heart Disease":
        #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
           st.title("Heart Disease Prediction")
           age=st.slider("Age",29,77,54)
           
           sex=st.radio("Sex",["Male","Female"],index=0)
           if sex=="Male":
               sex=1
           else:
               sex=0
               
           cp=st.radio("Chest Pain ",["Typical angina","Atypical angina","Non- anginal pain","Asymptomatic"],index=3)
           if cp=="Typical angina":
               cp=0
           elif cp=="Atypical angina":
               cp=1
           elif cp=="Non- anginal pain":
               cp=2
           elif cp=="Asymptomatic":
               cp=3
               
           tbps=st.slider("Patient's level of blood pressure at resting mode in mm/HG ",94,200,131)
           chol=st.slider("Serum cholesterol in mg/dl",120,570,250)
           fbs=st.slider("Fasting Blood Sugar",50,200,100)
           if fbs>120:
               fbs=1
           else:
               fbs=0
               
           ecg=st.selectbox("ECG at rest",["Normal","Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)","Showing probable or definite left ventricular hypertrophyby Estes' criteria"],index=0)
           if ecg=="Normal":
               ecg=0
           elif ecg=="Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)":
               ecg=1
           elif ecg=="Showing probable or definite left ventricular hypertrophyby Estes' criteria":
               ecg=2
           
           thalach=st.slider("Maximum heart rate achieved",70,205,90)
           
           exang=st.radio("Angina induced by exercise",["Yes","No"],index=1)
           if exang=="Yes":
               exang=1
           else:
               exang=0
           
           oldpeak=st.slider("Exercise induced ST-depression in relative with the state of rest",0.0,7.0)
           
           slope=st.radio("ST segment measured in terms of slope during peak exercise",["Up sloping","Flat","Down sloping"],index=2)
           if slope=="Up sloping":
              slope=0
           elif slope=="Flat":
               slope=1
           elif slope=="Down sloping":
               slope=2
           
           ca=st.slider("The number of major vessels",0,3)
           
           thal=st.selectbox("Thalassemia",["Null","Normal blood flow","Fixed defect (no blood flow in some part of the heart)","Reversible defect (a blood flow is observed but it is not normal"],index=0)
           if thal=="Null":
               thal=0
           elif thal=="Normal blood flow":
               thal=1
           elif thal=="Fixed defect (no blood flow in some part of the heart)":
               thal=2
           elif thal=="Reversible defect (a blood flow is observed but it is not normal":
               thal=3
        
       
           if st.button("Result"):
               st.write("Result :")
               r=heart_prediction([age,sex,cp,tbps,chol,fbs,ecg,thalach,exang,oldpeak,slope,ca,thal])


#LUNG CANCER
   
            
      
#if __name__=='__main__':
main()
      






#HEART DISEASE
#Age:     Patients Age in years (Numeric)
# 2] Sex:     Gender (Male : 1; Female : 0) (Nominal)
# 3] cp:      Type of chest pain experienced by patient. This term categorized into 4 category.
#              0 typical angina, 1 atypical angina, 2 non- anginal pain, 3 asymptomatic (Nominal)
# 4] trestbps: patient's level of blood pressure at resting mode in mm/HG (Numerical)
# 5] chol:     Serum cholesterol in mg/dl (Numeric)
# 6] fbs:      Blood sugar levels on fasting > 120 mg/dl represents as 1 in case of true and 0 as false (Nominal)
# 7] restecg:  Result of electrocardiogram while at rest are represented in 3 distinct values 0 : Normal 1:
#              having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
#              2: showing probable or definite left ventricular hypertrophyby Estes' criteria (Nominal)
# 8] thalach:  Maximum heart rate achieved (Numeric)
# 9] exang:    Angina induced by exercise 0 depicting NO 1 depicting Yes (Nominal)
# 10]oldpeak:  Exercise induced ST-depression in relative with the state of rest (Numeric)
# 11]slope:    ST segment measured in terms of slope during peak exercise 0: up sloping; 1: flat; 2: down sloping(Nominal)
# 12]ca:       The number of major vessels (0–3)(nominal)
# 13]thal:     A blood disorder called thalassemia 0: NULL 1: normal blood flow 2: fixed defect (no blood flow in some part of the heart)
#              3: reversible defect (a blood flow is observed but it is not normal(nominal)
# 14]target:   It is the target variable which we have to predict 1 means patient is suffering from heart disease and 0 means patient is normal.
  

