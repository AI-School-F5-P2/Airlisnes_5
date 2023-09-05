#Script transformer

def transform_gender(df):
    df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
    print("After transform_gender:")
    print(df['Gender'].head())  # Agrega esta línea para imprimir los primeros valores de la columna
    return df

def transform_customer_type(df):
    df['Customer Type'] = df['Customer Type'].map({'Loyal Customer': 1, 'disloyal Customer': 0})
    print("After transform_customer_type:")
    print(df['Customer Type'].head())
    return df

def transform_travel_type(df):
    df['Type of Travel'] = df['Type of Travel'].map({'Business travel': 1, 'Personal Travel': 0})
    print("After transform_travel_type:")
    print(df['Type of Travel'].head())
    return df

def transform_satisfaction(df):
    df['satisfaction'] = df['satisfaction'].map({'satisfied': 1, 'neutral or dissatisfied': 0})
    print("After transform_satisfaction:")
    print(df['satisfaction'].head())
    return df

def transform_class(df):
    class_mapping = {'Eco': 0, 'Eco Plus': 1, 'Business': 2}
    df['Class'] = df['Class'].map(class_mapping)
    print("After transform_class:")
    print(df['Class'].head())
    return df


def transform_categorical_columns(df):
    df = df.drop(['Unnamed: 0', 'id'], axis=1)    
    df = transform_gender(df)
    df = transform_customer_type(df)
    df = transform_travel_type(df)
    df = transform_satisfaction(df)
    df = transform_class(df)

    return df