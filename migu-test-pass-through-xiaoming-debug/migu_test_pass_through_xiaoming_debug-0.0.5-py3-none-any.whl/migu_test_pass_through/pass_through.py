from copy import deepcopy


class PassThrough(object):
    def __init__(self):
        pass

    def on_init(self, data):
        pass

    def run(self, data):
        print(f"data = {data}")
        return deepcopy(data),