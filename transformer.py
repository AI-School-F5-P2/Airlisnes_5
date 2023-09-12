#Script transformer
import numpy as np

def transform_gender(df):
    df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})  
    return df

def transform_customer_type(df):
    df['Customer Type'] = df['Customer Type'].map({'Loyal Customer': 1, 'disloyal Customer': 0})
    return df

def transform_travel_type(df):
    df['Type of Travel'] = df['Type of Travel'].map({'Business travel': 1, 'Personal Travel': 0})
    return df

def transform_satisfaction(df):
    df['satisfaction'] = df['satisfaction'].map({'satisfied': 1, 'neutral or dissatisfied': 0})
    return df

def transform_class(df):
    class_mapping = {'Eco': 0, 'Eco Plus': 1, 'Business': 2}
    df['Class'] = df['Class'].map(class_mapping)
    return df


def transform_categorical_columns(df):
    df = df.drop(['Unnamed: 0', 'id'], axis=1)    
    df = transform_gender(df)
    df = transform_customer_type(df)
    df = transform_travel_type(df)
    df = transform_satisfaction(df)
    df = transform_class(df)
    return df
   
"""
def transform_numerical_columns(df):
    numeric_columns = df.select_dtypes(include=[np.number])
    
    df[numeric_columns.columns] = df[numeric_columns.columns].fillna(df.mean())
    
"""

def transform_data(df):
    df = transform_categorical_columns(df)
    #df = transform_numerical_columns(df)

    return df

   