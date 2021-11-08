from typing import List, Tuple


class Scope:
    def __init__(self, range: List[float] = None):
        """
        Constructor for Scope Object

        Args:
            range (List[float], optional): Range to be converted into scope.
            Must be in the format: [minmz, maxmz, minrt, maxrt].
            Defaults to None.
        """
        bounds = self.config_mins_maxes(range)
        self.min_mz, self.max_mz, self.min_rt, self.max_rt = bounds

    def config_mins_maxes(self, range: List[float] = None) -> Tuple[float]:
        """
        Configures the Scope's m/z and Retention Time's minimum
        and maximum values.

        Args:
            range (List[float], optional): The values to use for configuration.
            Defaults to None.

        Returns:
            Tuple[float]: The min and max values configured from the
            specified range.
        """
        # TODO: This should be 'private' ??
        if range is None:
            return 0.0, 0.0, 0.0, 0.0

        return range[0], range[1], range[2], range[3]

    def as_string(self) -> str:
        """
        Returns the Scope's properties as a string.
        Tends to be helpful for debugging purposes.

        Returns:
            str: The Scope's properties as a string.
        """
        return f"mz_{self.min_mz}_{self.max_mz}_rt_{self.min_rt}_{self.max_rt}"
