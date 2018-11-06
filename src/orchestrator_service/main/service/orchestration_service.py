import time


def trigger_io_fileservice():
    print('Calling IO file service')
    time.sleep(5)
    return True


def trigger_model():
    print('Calling Model execution')
    time.sleep(5)
    return True
