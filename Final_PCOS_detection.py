# -*- coding: utf-8 -*-
''

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import sklearn.metrics
from sklearn.metrics import DistanceMetric

# loading the saved models

#working_dir = os.path.dirname(os.path.abspath(__file__))
filename1 = 'trained_model_lgr_lasso.sav'
filename2 = 'trained_model_gnb_lasso.sav'
filename3 = 'trained_model_lda_lasso.sav'
filename4 = 'trained_model_rfc_lasso.sav'

pcos_model1= pickle.load(open(filename1, 'rb'))
pcos_model2= pickle.load(open(filename2, 'rb'))
pcos_model3= pickle.load(open(filename3, 'rb'))
pcos_model4= pickle.load(open(filename4, 'rb'))


#pcos_model1= pickle.load(open(f'{working_dir}/trained_model_lgr_lasso.sav', 'rb'))
#pcos_model2= pickle.load(open(f'{working_dir}/trained_model_gnb_lasso.sav', 'rb'))
#pcos_model3= pickle.load(open(f'{working_dir}/trained_model_lda_lasso.sav', 'rb'))
#pcos_model4= pickle.load(open(f'{working_dir}/trained_model_rfc_lasso.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('PCOS Prediction System',
                          
                          ['PCOS Prediction Model-1',
                           'PCOS Prediction Model-2',
                          'PCOS Prediction Model-3',
                          'PCOS Prediction Model-4'],
                        #   'PCOS Prediction Model-4',
                        #   'PCOS Prediction Model-6'],
                           icons=['person','person','person', 'person'],
                            default_index=0)
 
if (selected == 'PCOS Prediction Model-1'):
    
    # page title
    st.title('PCOS Prediction')
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        Cycle = st.number_input('Regular/Irregular Cycle')
        
    with col2:
        Weight_gain = st.number_input('Weight increased/Or not')
    
    with col1:
        hair_growth = st.number_input('Excessive_Hair_growth/Or not')
    
    with col2:
        Skin_darkening = st.number_input('Darkenened skin/or not')
        
    
    with col1:
        FollicleNo_L = st.number_input('No of Follicle Left')
    
    
    with col2:
        FollicleNo_R  = st.number_input('No of Follicle Right')
    
    
    
    
    # code for Prediction
    pcos_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('PCOS Prediction Result'):
        pcos_prediction = pcos_model1.predict([[Cycle, Weight_gain, hair_growth, Skin_darkening,FollicleNo_L, FollicleNo_R]])
        
        if (pcos_prediction[0] == 0):
          pcos_diagnosis = 'The person does not have pcos'
        else:
          pcos_diagnosis = 'The person have risk of pcos'
        
    st.success(pcos_diagnosis)




#
if (selected == 'PCOS Prediction Model-2'):
    
    # page title
    st.title('PCOS Prediction')
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        Cycle = st.number_input('Regular/Irregular Cycle')
        
    with col2:
        Weight_gain = st.number_input('Weight increased/Or not')
    
    with col1:
        hair_growth = st.number_input('Excessive_Hair_growth/Or not')
    
    with col2:
        Skin_darkening = st.number_input('Darkenened skin/or not')
        
    
    with col1:
        FollicleNo_L = st.number_input('No of Follicle_L')
    
    
    with col2:
        FollicleNo_R  = st.number_input('No of Follicle_R')
    
    
    
    
    # code for Prediction
    pcos_diagnosis2 = ''
    
    # creating a button for Prediction
    
    if st.button('PCOS Prediction Result'):
        pcos_prediction = pcos_model2.predict([[Cycle, Weight_gain, hair_growth, Skin_darkening,FollicleNo_L, FollicleNo_R]])
        
        if (pcos_prediction[0] == 0):
          pcos_diagnosis2 = 'The person does not have pcos'
        else:
          pcos_diagnosis2 = 'The person have risk of pcos'
        
    st.success(pcos_diagnosis2)

    
    #model-3
    
    
    
    
if (selected == 'PCOS Prediction Model-3'):
    
    # page title
    st.title('PCOS Prediction')
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        Cycle = st.number_input('Regular/Irregular Cycle')
        
    with col2:
        Weight_gain = st.number_input('Weight increased/Or not')
    
    with col1:
        hair_growth = st.number_input('Excessive_Hair_growth/Or not')
    
    with col2:
        Skin_darkening = st.number_input('Darkenened skin/or not')

    
    with col1:
        FollicleNo_L = st.number_input('No of Follicle_L')
    
    
    with col2:
        FollicleNo_R  = st.number_input('No of Follicle_R')
    
    
    
    
    # code for Prediction
    pcos_diagnosis3 = ''
    
    # creating a button for Prediction
    
    if st.button('PCOS Prediction Result'):
        pcos_prediction = pcos_model3.predict([[Cycle, Weight_gain, hair_growth, Skin_darkening,FollicleNo_L, FollicleNo_R]])
        
        if (pcos_prediction[0] == 0):
          pcos_diagnosis3 = 'The person does not have pcos'
        else:
          pcos_diagnosis3 = 'The person have risk of pcos'
        
    st.success(pcos_diagnosis3)

  

if (selected == 'PCOS Prediction Model-4'):
    
    # page title
    st.title('PCOS Prediction')
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        Cycle = st.number_input('Regular/Irregular Cycle')
        
    with col2:
        Weight_gain = st.number_input('Weight increased/Or not')
    
    with col1:
        hair_growth = st.number_input('Excessive_Hair_growth/Or not')
    
    with col2:
        Skin_darkening = st.number_input('Darkenened skin/or not')
        
    
    with col1:
        FollicleNo_L = st.number_input('No of Follicle Left')
    
    
    with col2:
        FollicleNo_R  = st.number_input('No of Follicle Right')
    
    
    
    
    # code for Prediction
    pcos_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('PCOS Prediction Result'):
        pcos_prediction = pcos_model4.predict([[Cycle, Weight_gain, hair_growth, Skin_darkening,FollicleNo_L, FollicleNo_R]])
        
        if (pcos_prediction[0] == 0):
          pcos_diagnosis = 'The person does not has pcos'
        else:
          pcos_diagnosis = 'The person has pcos'
        
    st.success(pcos_diagnosis)


