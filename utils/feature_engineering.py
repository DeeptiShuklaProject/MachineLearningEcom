def create_features(df):
    # Example: Create a new feature
    df['total_bill'] = df['total_bill'].apply(lambda x: x * 1.1)
    return df
