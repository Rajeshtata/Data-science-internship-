import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
file_directory = os.path.dirname(os.path.abspath(__file__))

# absolute path to this file's root directory
parent_directory = os.path.join(file_directory, os.pardir)

# absolute path of directory of interest
dir_of_interest = os.path.join(parent_directory,"resources")

image_path = os.path.join(dir_of_interest, "images", "penguins_image.jpg")
data_path = os.path.join(dir_of_interest, "data", "penguins.csv")


st.title("Dashboard - penguins Data")

img = image.imread(image_path)
st.image(img)

df = pd.read_csv(data_path)
st.dataframe(df)

species = st.selectbox("Select the species:",df["species"].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['species'] == species], x="bill_length_mm")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['species'] == species], y="bill_length_mm")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.histogram(df[df['species'] == species], x="bill_depth_mm")
col1.plotly_chart(fig_3, use_container_width=True)

fig_4 = px.box(df[df['species'] == species], y="bill_depth_mm")
col2.plotly_chart(fig_4, use_container_width=True)


island = st.selectbox("Select the island:",df["island"].unique())

col1, col2 = st.columns(2)



fig_5 = px.histogram(df[df['island'] == island], x="flipper_length_mm")
col1.plotly_chart(fig_5, use_container_width=True)

fig_6 = px.box(df[df['island'] == island], y="flipper_length_mm")
col2.plotly_chart(fig_6, use_container_width=True)

fig_7 = px.histogram(df[df['island'] == island], x="body_mass_g")
col1.plotly_chart(fig_7, use_container_width=True)

fig_8 = px.box(df[df['island'] == island], y="body_mass_g")
col2.plotly_chart(fig_8, use_container_width=True)
