import streamlit as st
import pickle
import pandas as pd
from datetime import datetime
from app import load_model_and_predict


file_path = 'C:/Users/mariy/Downloads/Question 5 - ML-20240829T070211Z-001/Question 5 - ML/pipelines/xgboost_model.pkl'
history_file = 'C:/Users/mariy/Downloads/Question 5 - ML-20240829T070211Z-001/Question 5 - ML/history.csv'

model = pickle.load(open(file_path, 'rb'))


html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Sales Forecast ML App </h2>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)

store = st.text_input('Store','ABC / XYZ')
item_dept = st.text_input('Item Department','Household')
date = st.date_input('Date', datetime(2022, 2, 1))


safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Your forest is safe</h2>
       </div>
    """
danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Your forest is in danger</h2>
       </div>
    """

if st.button('Predict'):
    if history_file is not None:
        prediction = load_model_and_predict(store, item_dept, date, history_file)
        st.write(f"Predicted item quantity for {store} - {item_dept} on {date}: {prediction}")
    else:
        st.error('Please upload a historical data CSV file.')
