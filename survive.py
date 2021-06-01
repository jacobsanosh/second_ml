import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse',False)


st.title("welcome")
st.sidebar.header("this is an sise bar")

datas =pd.read_csv('titanic.csv/titanic.csv')
new_data =datas.head(10)
st.table(new_data)

st.header("passenger and thei survive")
sns.barplot(x='PassengerId',y='Survived',hue='Survived',data=new_data)
st.pyplot()



#box plot
st.header("passenger and fare chart")
sns.jointplot(x='PassengerId',y='Fare',data=new_data)
st.pyplot()

st.header("pair plot")
sns.pairplot(new_data,hue='Survived',palette='Set1')
st.pyplot()

st.balloons()