import time


def trigger_model_workflow():
    print('Calling model workflow!')
    trigger_io_fileservice()
    trigger_model()
    return "Model executed succesfully"


def trigger_io_fileservice():
    print('Calling IO file service')
    time.sleep(5)
    return True


def trigger_model():
    print('Calling Model execution')
    time.sleep(5)
    return True
