import pandas as pd
import numpy as np
import streamlit as st
df=pd.read_excel("online offline sales.xlsx")
df["Profit"]=df["Total Selling Value"]-df["Total Buying Value"]
df_saletype=df.groupby("SALE TYPE")["Profit"].sum()
#df_saletype=df_saletype.reset_index()
m1=df_saletype.idxmax()
st.header("Profit Summery")
st.metric("Profit",f"₹{df['Profit'].sum():,.2f}")
col1,col2=st.columns(2)

with col1:
    st.markdown("<h3 style='color: green;'>Profit With Sales Type</h3>", unsafe_allow_html=True)
    st.markdown("_"+m1+" performed better than offline sales._")
    tab1,tab2=st.tabs(["Charts","Data"])

    #st.write("Profit With Sales Type")
    with tab2:
        st.write(df_saletype)
    with tab1:
        st.bar_chart(df_saletype)
with col2:
    df_pmt=df.groupby("PAYMENT MODE")["Total Selling Value"].sum()
    st.markdown("<h3 style='color: green;'>Payment mode</h3>", unsafe_allow_html=True)
    tab1,tab2=st.tabs(["Charts","Data"])
    with tab2:
        st.write(df_pmt)
    with tab1:
        st.bar_chart(df_pmt,color="#ffaa0088")

