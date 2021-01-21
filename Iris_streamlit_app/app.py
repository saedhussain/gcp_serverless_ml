import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Load the trained iris model
model = pickle.load(open('./iris_model_jan_2020_v1.pkl','rb'))

def main():

    # Title of the app page
    st.title('Iris Flower Prediction App')

    # Add a heading for input features
    st.subheader('Enter Flower Feature For Predictions')

    # Rquest for input fatures, but replod with some default values
    sepal_lenght   = st.text_input('Sepal Len (cm)', 2.0)
    sepal_width    = st.text_input('Sepal Width (cm)', 3.0)
    petal_length   = st.text_input('Petal Len (cm)', 4.0)
    petal_width    = st.text_input('Petal Width (cm)', 5.0)


    # Get predictions when the button is pressed
    if st.button('Get Prediction'):

        # run predictions
        pred = model.predict(np.array([[float(sepal_lenght),float(sepal_width),float(petal_length),float(petal_width)]]))

        st.text('Predicted Flower:' + pred[0])


if __name__ == "__main__":
    main()
