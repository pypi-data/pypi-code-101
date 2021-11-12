from multiprocessing.dummy import Process, Queue, Manager
from queue import Empty
from datetime import datetime


class Logger:
    class FULL:
        pass

    class INFO:
        pass

    class DEBUG:
        pass

    class ERROR:
        pass

    def __init__(self, file, file_mod: tuple = (FULL, ), stdout_mode: tuple = (FULL, )):
        if file:
            self._file_path = file

        self._file_mod = file_mod
        self._stdout_mode = stdout_mode

        self._finish = False
        self._logger_queue: Queue = Manager().Queue()
        self._process: Process = Process(target=self._worker)
        self._process.name = "Logger Thread"
        self._process.start()

    def __enter__(self):
        return self

    def inf(self, s: str):
        self._logger_queue.put(f"{datetime.now()} \033[32mINFO:\033[0m {s}")

    def err(self, s: str):
        self._logger_queue.put(f"{datetime.now()} \033[31mERROR\033[0m: {s}")

    def dbg(self, s: str):
        self._logger_queue.put(f"{datetime.now()} \033[34mDEBUG:\033[0m {s}")

    def _worker(self):
        self.dbg(f"Starting log worker: {self._process.name}")
        with open(self._file_path, "w") as log_file:
            self.dbg(self._file_path)
            while not self._logger_queue.empty() or not self._finish:
                try:
                    string = self._logger_queue.get(block=True)
                except Empty:
                    continue

                if self.FULL in self._stdout_mode:
                    print(string)
                if self.DEBUG in self._stdout_mode:
                    if "DEBUG" in string:
                        print(string)
                if self.ERROR in self._stdout_mode:
                    if "ERROR" in string:
                        print(string)
                if self.INFO in self._stdout_mode:
                    if "INFO" in string:
                        print(string)

                if self.FULL in self._file_mod:
                    print(string, file=log_file)
                if self.DEBUG in self._file_mod:
                    if "DEBUG" in string:
                        print(string, file=log_file)
                if self.ERROR in self._file_mod:
                    if "ERROR" in string:
                        print(string, file=log_file)
                if self.INFO in self._file_mod:
                    if "INFO" in string:
                        print(string, file=log_file)

    def __del__(self):
        self._finish = True
        self._process.join()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._finish = True
        self._process.join()
