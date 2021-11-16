from copy import deepcopy


class PassThrough(object):
    def __init__(self):
        pass

    def on_init(self, input_data):
        print(f"on_init, self = {self}, data = {input_data}")
        pass

    def run(self, input_data):
        print(f"run, self = {self}, data = {input_data}")
        return deepcopy(input_data),