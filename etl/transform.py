def transform_data(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df = df.dropna()
    return df
