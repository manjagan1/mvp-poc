import pandas as pd


class IOFileService:
    def __init__(self):
        print('reading file')

    def get_data(self):
        # TODO: MAKE THIS COME FROM CONFIG
        return pd.read_csv('path/to/file')

