import streamlit as st
import pandas as pd
import snowflake.connector

#conn = st.connection("snowflake")
#df = conn.query("SELECT MENU_ITEM_NAME, COST_OF_GOODS_USD FROM tasty_bytes_sample_data.raw_pos.menu LIMIT 10 ;", ttl="10m")


ctx = snowflake.connector.connect(account = "CRRSXRD-GW87182",
password='Fantasys.92',
user = "clementmsikadata",
role = "ACCOUNTADMIN",
warehouse = "COMPUTE_WH",
database = "tasty_bytes_sample_data",
schema = "raw_pos")

query = "SELECT MENU_ITEM_NAME, COST_OF_GOODS_USD FROM tasty_bytes_sample_data.raw_pos.menu LIMIT 10 ;"
 
cur = ctx.cursor()

cur.execute(query)

def fetch_pandas(cur, sql):
    cur.execute(sql)
    rows = 0
    while True:
        dat = cur.fetchmany(50000)
        if not dat:
            break
        df = pd.DataFrame(dat, columns=cur.description)
        rows += df.shape[0]
        
    df.columns = [item[0] for item in df.columns]
        
    return df

df = fetch_pandas(cur, query)

st.write("""
# Welcome to Ae Jung restaurant !
""")

for row in df.itertuples():
    st.write(f"{row.MENU_ITEM_NAME} 's price :{row.COST_OF_GOODS_USD}:")


