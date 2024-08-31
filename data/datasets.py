import pandas as pd
from sqlalchemy import create_engine

def load_data(file_path):
    return pd.read_csv(file_path)

def save_data_to_postgres(df, table_name, db_url):
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

