"""
Runtime tweaks
"""
import psutil


def get_max_threads() -> int:
    """
    gets number of cpu threads
    @return: cpu thread count
    """
    return psutil.cpu_count()


def get_cache_size() -> int:
    """
    gets a cache size depending on available and total memory
    @return: cache size
    """
    # get free size in KB
    total = int(psutil.virtual_memory().total / 1024)
    avail = int(psutil.virtual_memory().available / 1024)
    return __nearest_power_of_two(max([1024 * 1024, int(total / 4), int(avail / 2)]))


# if you want a power of 2 by force
def __nearest_power_of_two(number: int) -> int:
    """
    Gets the nearest power of 2 from given number

    @param number: a number
    @return: a power of 2
    """
    exp = number.bit_length()
    # next greater power of 2
    greater_value = 1 << exp
    # next smaller power of 2
    smaller_value = 1 << (exp - 1)
    if abs(greater_value - number) > abs(smaller_value - number):
        return smaller_value
    return greater_value
