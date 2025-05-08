import psycopg2
import pandas as pd

def load_to_redshift(df, table_name, conn_params):
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (order_id, customer, amount, order_date)
            VALUES (%s, %s, %s, %s)
        """, tuple(row))
    conn.commit()
    conn.close()
