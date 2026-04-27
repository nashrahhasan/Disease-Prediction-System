# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

#E:/PCOS Project/trained_model_bnb_lasso.sav
pcos_model1= pickle.load(open('E:/PCOS Project/trained_model_bnb_lasso.sav', 'rb'))
pcos_model2= pickle.load(open('E:/PCOS Project/trained_model_gnb_lasso.sav', 'rb'))
pcos_model3= pickle.load(open('E:/PCOS Project/trained_model_lda_lasso.sav', 'rb'))
#pcos_model4= pickle.load(open('D:/1-MIT/MIT_Project/PCOS_model/Saved_model2/rfc_pc_model.sav', 'rb'))
#pcos_model5 = pickle.load(open('D:/1-MIT/MIT_Project/PCOS_model/Saved_model2/svm_pc_model.sav', 'rb'))
#pcos_model6 = pickle.load(open('D:/1-MIT/MIT_Project/PCOS_model/Saved_model2/Lda_pc_model.sav', 'rb'))
#pcos_model = pickle.load(open('D:/1-MIT/MIT PRoect/PCOS_model/Saved_models/PCOS_model_lasso_knn.sav','rb'))


def pcos_prediction():
    
    
    input_data = (0.013337,	-0.024860,	0.063465,	-0.024783,	0.043788,	0.014857)

# changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction =pcos_model1.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        
        return 'NO risk of Pcos '
    else:
       return'Patient has PCOS '



  
def main():
    
    
    
    # giving a title
    st.title('Web-based PCOS Prediction')
    
    
    # getting the input data from the user

    
    Cycle = st.text_input('Cycle Regular or Irregular')
    Weightgain= st.text_input('Gained weight')
    hairgrowth= st.text_input('Excessive hair growth')
    Skindarkening = st.text_input('Skin darkened')
    #Pimples= st.text_input('Pimples')
   # Fastfood= st.text_input('Eats Fast food')
    FollicleL = st.text_input('Follicule in left ovary')
    FollicleR= st.text_input('Follicule in right ovary')

    
    
    # code for Prediction
    diagnosis1 = ''
    
    # creating a button for Prediction
    
    if st.button('PCOS Test Result'):
        diagnosis1 = pcos_prediction([Cycle,Weightgain, hairgrowth, Skindarkening ,FollicleL,FollicleR])
        
        
    st.success(diagnosis1)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    