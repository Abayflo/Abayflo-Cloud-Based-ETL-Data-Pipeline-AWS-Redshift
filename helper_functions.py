import pandas as pd

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names and drop missing values."""
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df.dropna(inplace=True)
    return df

# Example usage
# df = pd.read_csv('data/sample_data.csv')
# cleaned_df = clean_sales_data(df)