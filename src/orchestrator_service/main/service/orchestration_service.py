import time
import requests


def trigger_model_workflow():
    print('Calling model workflow!')
    trigger_io_fileservice()
    trigger_model()
    return "Model executed succesfully"


def trigger_io_fileservice():
    print('Calling IO file service')
    time.sleep(3)
    return True


def trigger_model():
    print('Calling Model execution')
    print(requests.get('http://r-model-training:9090/r_model_training'))
    return True
