import pandas as pd


class IOFileService:
    def __init__(self):
        pass

    def get_data(self, file_path):
        # TODO: MAKE THIS COME FROM CONFIG
        return pd.read_csv(file_path)
