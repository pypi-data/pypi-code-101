from typing import List
import matplotlib.pyplot as plt


class Bar:
    def __init__(self, x: List[float], y: List[float]) -> None:
        """
        Constructor for the bar class. Serves as a wrapper around
        matplotlib's bar charts.

        Args:
            x (List[float]): The values to be plotted with
            respect to the x-axis.
            y (List[float]): The values to be plotted with
            respect to the y-axis.
        """
        self.x = x
        self.y = y

    def plot(self) -> None:
        """
        Renders the bar chart using matplotlib api.

        """
        # TODO: Pretty barebones in terms of flexibility.
        # What else should go here? :,)
        plt.figure()
        plt.bar(self.x, self.y, width=0.1, color='black')
        plt.xlabel('m/z', fontweight='bold', color='black',
                   fontsize='13', horizontalalignment='center')
        plt.ylabel('Signal Intensity', fontweight='bold',
                   color='black', fontsize='13', horizontalalignment='center')
        plt.show()


class Bar3D:
    def __init__(self, x: List[float], y: List[float], z: List[float]) -> None:
        """
        Constructor for the Bar3D class. Serves as a wrapper
        around matplotlib's 3d bar projection.

        Args:
            x (List[float]): The values to be plotted with respect
            to the x-axis.
            y (List[float]): The values to be plotted with respect
            to the y-axis.
            z (List[float]): The values to be plotted with respect
            to the z-axis.
        """
        self.x = x
        self.y = y
        self.z = z

    def plot(self) -> None:
        """
        Renders the 3D bar chart projection.

        """

        # Pretty barebones in terms of flexibility
        # What else do we need here??

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        zpos = [0 for i in self.x]
        dx = [1 for i in self.x]
        dy = [1 for i in self.x]

        ax.bar3d(self.x, self.y, zpos, dx, dy, self.z, color='#FFADF5')

        ax.set_xlabel('m/z')
        ax.set_ylabel('Retention Time')
        ax.set_zlabel('Signal Intensity')
        plt.show()
