import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Smartphone Price Predictor")
# Main page content
st.image('mobile.png', use_column_width=True)

# brand
Company = st.selectbox('Brand',df['Brand'].unique())

# year
Released_Year = st.selectbox('Released Year',df['Released Year'].unique())

# OS
Operating_System = st.selectbox('OS',df['OS'].unique())

# size
Display = st.number_input('Display (Inches)')

# Camera
Camera = st.number_input('Camera (MP)')

# resolution
Camera_Resolution= st.selectbox('Camera Resolution',df['Camera Resolution'].unique())

# Ram
Ram = st.number_input('Ram (GB)')

# Battery
Battery = st.number_input('Battery (mAh)')



if st.button('Predict Price'):
    query = np.array([Company, Released_Year, Operating_System, Display, Camera, Camera_Resolution, Ram, Battery])
    query = query.reshape(1, -1)
    st.title("The predicted price of this configuration mobile is " + str(int(np.exp(pipe.predict(query)[0]))) + ' TK.')
