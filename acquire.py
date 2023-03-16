import os
import requests
import pandas as pd

ids = {
    # Google drive file ids for building download urls
    'white': '14BJY5EBlyxuELN_diunepjAnDBDsjtlh',
    'red': '1NT2qJuMDwcz2devXVL5jUMPKe4K70awO'
}

paths = {
    'white': 'data/winequality-white.csv',
    'red' :'data/winequality-red.csv',
    'both': 'data/winequality-both.csv'
}

def gdrive_url(file_id):
    """Gets a google drive download url for a specific file ID"""
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    return url

def download(url, path):
    """Downloads the binary content from a url to the specified path."""
    import requests
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Error: Status {response.status_code}')
    with open(path, 'wb') as f:
        f.write(response.content)

def red_get_data():
    path = paths['red']
    if not os.path.exists(path):
        url = gdrive_url(ids['red'])
        download(url, path)
    df = pd.read_csv(path, delimiter=';')
    df = df.drop_duplicates()
    return df


def white_get_data():
    path = paths['white']
    if not os.path.exists(path):
        url = gdrive_url(ids['white'])
        download(url, path)
    df = pd.read_csv(path, delimiter=';')
    df = df.drop_duplicates()
    return df

def both_get_data():
    path = paths['both']
    if not os.path.exists(path):
        white = white_get_data()
        red = red_get_data()
        red['type'] = 'red'
        white['type'] = 'white'
        df = pd.concat([red, white])
        df.to_csv(path, index=False)
    else:
        df = pd.read_csv(path)
    df = df.reset_index().drop(columns='index')
    df = df.drop_duplicates()
    return df
