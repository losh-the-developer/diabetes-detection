#Description: This program optimizes a stock portfolio

#Import the python libraries
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import streamlit as st

#Create a title and a subtitle
st.write("""
# Diabetes detection
Detect if someone has diabetes using machine learning and python!
""")

#open and display an image on web app
image = Image.open('C:/Users/Loshan/projects/diabetes/SD_DiabetesWebBanner.jpg')
st.image(image, caption = 'ML', use_column_width=True)

#get the data
df = pd.read_csv('C:/Users/Loshan/projects/diabetes/diabetes.csv')

#set a subheader

st.subheader('Data Information')

#show data as a table
st.dataframe(df)

#show stats on the data
st.write(df.describe())

#show data as a chart
chart = st.bar_chart(df)

#split data into independent x and y variables
X = df.iloc[:, 0:8].values
Y = df.iloc[:,-1].values

#split the dataset into 75% training and 25% testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)


#Get feature input from the user
def get_user_input():
    pregnancies = st.sidebar.slider('pregnancies', 0, 14, 3)
    glucose = st.sidebar.slider('glucose', 0, 199, 177)
    blood_pressure = st.sidebar.slider('blood_pressure', 0, 122, 72)
    skin_thickness = st.sidebar.slider('skin_thickness', 0, 99, 3)
    insulin = st.sidebar.slider('insulin', 0.0, 846.0, 30.0)
    BMI = st.sidebar.slider('BMI', 0.0, 67.1, 32.0)
    DPF = st.sidebar.slider('DPF', 0.078, 2.42, 0.3725)
    age = st.sidebar.slider('age', 21, 81, 29)

    #store a dictionary into a variable
    user_data = {
        'pregnancies' : pregnancies,
        'glucose' : glucose,
        'blood_pressure': blood_pressure,
        'skin_thickness': skin_thickness,
        'insulin': insulin,
        'BMI': BMI,
        'DPF': DPF,
        'age': age
    }

    #transform the data into a data frame
    features = pd.DataFrame(user_data, index = [0])
    return features

#store the users input data into a variable
user_input = get_user_input()

#set a subheader and display the users input
st.subheader('user Input:')
st.write(user_input)

#create and train the model
RandomForestClassifier = RandomForestClassifier()
RandomForestClassifier.fit(X_train, Y_train)

#show the models metrics
st.subheader('Model Test Accuracy Score: ')
st.write(str(accuracy_score(Y_test, RandomForestClassifier.predict(X_test)) * 100) + '%' )

#store the models predictions in a variable
prediction = RandomForestClassifier.predict(user_input)

#set a subheader and display the classification
st.subheader('Classification: ')
st.write(prediction)