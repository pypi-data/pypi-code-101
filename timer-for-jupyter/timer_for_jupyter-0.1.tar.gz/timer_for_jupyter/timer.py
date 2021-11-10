import time

 

class TimerError(Exception):

    """A custom exception used to report errors in use of Timer class"""

 

class Timer:

    def __init__(self):

        self._start_time = None

 

    def start(self):

        """Start a new timer"""

        if self._start_time is not None:

            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

        print(f'Timer started at: {time.strftime("%Y-%m-%d %H:%M:%S")}')

       

    @staticmethod

    def _parse_time(elapsed_time):

        """Parses elapsed time from seconds to hours, minutes and seconds, static"""

        hours,remaining_seconds = divmod(elapsed_time, 3600)

        minutes, seconds = divmod(remaining_seconds, 60)

        return hours, minutes, seconds  

            

            

    def report(self):

        """Reports the elapsed time"""

        if self._start_time is None:

            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time

        hours, minutes, seconds   = self._parse_time(elapsed_time)

        print(f'Elapsed time: {hours} hours, {minutes} minutes and {round(seconds, 2)} seconds.')

 

 

    def reset(self):

        """Resets and reports the elapsed time"""

        if self._start_time is None:

            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time

        hours, minutes, seconds   = self._parse_time(elapsed_time)

        self._start_time = time.perf_counter()

        print(f'Elapsed time: {hours} hours, {minutes} minutes and {round(seconds, 2)} seconds. Timer resets')  

        

 

       

    def stop(self):

        """stops and reports the elapsed time"""

        if self._start_time is None:

            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time

        hours, minutes, seconds   = self._parse_time(elapsed_time)

        self._start_time = None

        print(f'Elapsed time: {hours} hours, {minutes} minutes and {round(seconds, 2)} seconds. Timer stopped')

        print(f'Timer stoped at: {time.strftime("%Y-%m-%d %H:%M:%S")}')


if __name__=="__main__":
    pass

 