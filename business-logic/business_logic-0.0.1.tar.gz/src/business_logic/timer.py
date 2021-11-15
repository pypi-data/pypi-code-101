import time


class Timer(object):
    def __init__(self, description):
        self.description = description

    # def __enter__(self):
    #     self.start = time()
    #
    # def __exit__(self, type, value, traceback):
    #     self.end = time()
    #     print(f"{self.description}: {self.end - self.start}")
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.elapsed = time.perf_counter() - self.start
