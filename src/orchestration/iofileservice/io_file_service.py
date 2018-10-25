import pandas as pd


class IOFileService:
    def __init__(self):
        pass

    def get_data(self):
        # TODO: MAKE THIS COME FROM CONFIG
        return pd.read_csv('./data/cs-training_Transactional.csv')

