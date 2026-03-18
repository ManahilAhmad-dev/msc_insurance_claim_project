import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Build path relative to this file
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR.parent / "data" / "insurance.csv"

# Load data
df = pd.read_csv(DATA_PATH)

st.title("Insurance Cost Analytics Dashboard")

# Show dataset
st.subheader("Dataset Overview")
st.write(df.head())

# Filter
smoker_filter = st.selectbox("Select Smoking Status", ["all", "yes", "no"])

filtered_df = df.copy()
if smoker_filter != "all":
    filtered_df = filtered_df[filtered_df["smoker"] == smoker_filter]

# Histogram
st.subheader("Distribution of Charges")
fig, ax = plt.subplots()
sns.histplot(filtered_df["charges"], kde=True, ax=ax)
st.pyplot(fig)

# BMI vs Charges
st.subheader("BMI vs Charges")
fig, ax = plt.subplots()
sns.scatterplot(x="bmi", y="charges", data=filtered_df, hue="smoker", ax=ax)
st.pyplot(fig)

# Boxplot
st.subheader("Charges by Smoking Status")
fig, ax = plt.subplots()
sns.boxplot(x="smoker", y="charges", data=filtered_df, ax=ax)
st.pyplot(fig)