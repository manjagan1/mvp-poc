import pandas as pd


def transform_data(df):
    # Standard-transform a column
    df['NumberRealEstateLoansOrLines'] = (df['NumberRealEstateLoansOrLines'] - df[
        'NumberRealEstateLoansOrLines'].mean()) / df['NumberRealEstateLoansOrLines'].std()

    # Create a new feature
    df['LinesPerAge'] = df['NumberOfOpenCreditLinesAndLoans'] / df['AgeInBank']

    # Remove outliers from DebtRatio
    # Find outliers with std method
    mask = abs(df['DebtRatio'] - df['DebtRatio'].mean() / df['DebtRatio'].std()) < 3
    df = df[mask]

    return df
