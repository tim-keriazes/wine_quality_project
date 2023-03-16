from sklearn.model_selection import train_test_split
import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

import acquire
from helpers.util import make_valid_py_id
from helpers.prep import train_test_validate_split

SEED = 13

def wrangle_data(dataset):
    '''
    Standardizes the acquiring and preparing of a wine dataset to ensure compatibility between models that are built.
    '''
    # Acquire the correct dataset determined by the dataset argument
    if dataset == 'red':
        df = acquire.red_get_data()
        df['type'] = 'red'
    elif dataset == 'white':
        df = acquire.white_get_data()
        df['type'] = 'white'
    elif dataset == 'both':
        df = acquire.both_get_data()
    else:
        raise Exception("Invalid dataset. Expected one of ['red', 'white', 'both']")

    # Rename columns
    df.columns = [make_valid_py_id(col) for col in df]

    # Drop duplicates
    df = df.drop_duplicates()

    return df

def wrangle_data_and_split(dataset, seed=SEED):
    df = wrangle_data(dataset)
    train, validate, test = train_test_validate_split(df, seed=seed)
    return train, validate, test

def split(df, target_var, seed=SEED):
    '''
    This function takes in the dataframe and target variable name as arguments and then
    splits the dataframe into train (56%), validate (24%), & test (20%)
    It will return a list containing the following dataframes: train (for exploration), 
    X_train, X_validate, X_test, y_train, y_validate, y_test
    '''
    # split df into train_validate (80%) and test (20%)
    train_validate, test = train_test_split(df, test_size=.20, random_state=seed)
    # split train_validate into train(70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=seed)

    # create X_train by dropping the target variable 
    X_train = train.drop(columns=[target_var])
    # create y_train by keeping only the target variable.
    y_train = train[[target_var]]

    # create X_validate by dropping the target variable 
    X_validate = validate.drop(columns=[target_var])
    # create y_validate by keeping only the target variable.
    y_validate = validate[[target_var]]

    # create X_test by dropping the target variable 
    X_test = test.drop(columns=[target_var])
    # create y_test by keeping only the target variable.
    y_test = test[[target_var]]

#     partitions = [train, X_train, X_validate, X_test, y_train, y_validate, y_test]
    return train, X_train, X_validate, X_test, y_train, y_validate, y_test    