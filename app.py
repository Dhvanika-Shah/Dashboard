import pandas as pd
import numpy as np
import streamlit as st

st.title("My Chatbot")

#st.components.v1.iframe(
#    "https://www.chatbase.co/Mge9vJCIojYk1OZv5HHmk/help",
 #   height=600
#)


chat_widget = """
<script>
(function(){if(!window.chatbase||window.chatbase("getState")!=="initialized"){window.chatbase=(...arguments)=>{if(!window.chatbase.q){window.chatbase.q=[]}window.chatbase.q.push(arguments)};window.chatbase=new Proxy(window.chatbase,{get(target,prop){if(prop==="q"){return target.q}return(...args)=>target(prop,...args)}})}const onLoad=function(){const script=document.createElement("script");script.src="https://www.chatbase.co/embed.min.js";script.id="Mge9vJCIojYk1OZv5HHmk";script.domain="www.chatbase.co";document.body.appendChild(script)};if(document.readyState==="complete"){onLoad()}else{window.addEventListener("load",onLoad)}})();
</script>

"""

st.components.v1.html(chat_widget, height=0, scrolling=False)

# Load Excel file
df = pd.read_excel("online offline sales.xlsx")

# Calculate Profit
df["Profit"] = df["Total Selling Value"] - df["Total Buying Value"]
st.button("Mybot")
# Profit by Sales Type
df_saletype = df.groupby("SALE TYPE")["Profit"].sum()
top_sale_type = df_saletype.idxmax()

st.header("Profit Summary")
st.metric("Total Profit", f"₹{df['Profit'].sum():,.2f}")

col1, col2 = st.columns(2)

# --- COL 1: Sales Type ---
with col1:
    st.markdown("<h3 style='color: green;'>Profit by Sales Type</h3>", unsafe_allow_html=True)
    st.markdown(f"_{top_sale_type} performed better than offline sales._")

    tab_sales_chart, tab_sales_data = st.tabs(["Charts", "Data"])

    with tab_sales_data:
        st.write(df_saletype)

    with tab_sales_chart:
        st.bar_chart(df_saletype)

# --- COL 2: Payment Mode ---
with col2:
    df_payment = df.groupby("PAYMENT MODE")["Total Selling Value"].sum()

    st.markdown("<h3 style='color: green;'>Payment Mode Analysis</h3>", unsafe_allow_html=True)

    tab_pay_chart, tab_pay_data = st.tabs(["Charts", "Data"])

    with tab_pay_data:
        st.write(df_payment)

    with tab_pay_chart:
        st.bar_chart(df_payment)




