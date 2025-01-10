import streamlit as st
import pandas as pd


conn = st.connection("snowflake")
df = conn.query("SELECT MENU_ITEM_NAME, COST_OF_GOODS_USD FROM tasty_bytes_sample_data.raw_pos.menu LIMIT 10 ;", ttl="10m")

 
st.write("""
# Welcome to Ae Jung restaurant !
""")

for row in df.itertuples():
    st.write(f"{row.MENU_ITEM_NAME} 's price :{row.COST_OF_GOODS_USD}:")


