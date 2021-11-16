import pygplates
import numpy as np
import pandas as pd
from time import process_time
from scipy.spatial import cKDTree
from scipy.spatial.transform import Rotation as scpRot


class PlateInfo(object):
    """
    This class is the main entry point to interact with plate evolution. It is used to compute the uplift, subsidence in converging and diverging regions as well as the informations regarding plate topologies.

    """

    def __init__(self):

        # Get plates information at start time
        t0 = process_time()
        self.interpT = np.zeros(self.npoints)
        self.updatePlates()
        if self.verbose:
            print(
                "\n-- Create plate informations (%0.02f seconds)"
                % (process_time() - t0),
                flush=True,
            )

    def updatePlates(self):
        """
        The following function encompasses all the required functions used for moving plates and assigning plate informations as the model evolve through time.
        """

        # Define plate IDs and rotations using pygplates information
        t0 = process_time()
        self._getPlateIDs()
        self._getRotations()
        if self.verbose:
            print(
                "Get plate indices & rotations (%0.02f seconds)"
                % (process_time() - t0),
                flush=True,
            )

        return

    def _getRotations(self):
        """
        To move tectonic plates, we create a rotation quaternion for each plate, and apply rotations to all vertices based on their plate ids.

        We use the library pygplates to assign plate ids to vertices. Pygplates requires a list of point features for each vertex on our sphere and assigns plate ids to those.
        """

        rotationModel = pygplates.RotationModel(self.rotationsDirectory)

        self.rotations = {}
        for plateId in np.unique(self.plateIds):
            stageRotation = rotationModel.get_rotation(
                int(self.tNow - self.dt), int(plateId), int(self.tNow)
            )
            stageRotation = stageRotation.get_euler_pole_and_angle()

            axisLatLon = stageRotation[0].to_lat_lon()
            axis = self._polarToCartesian(1, axisLatLon[1], axisLatLon[0])
            angle = stageRotation[1]
            self.rotations[plateId] = scpRot.from_quat(self._quaternion(axis, angle))

        return

    def _getPlateIDs(self):
        """
        To specify which tectonic plate a particular vertex on our sphere belongs to, we create a list of Plate Ids where each vertex is given a number based on which plate they belong to.
        """

        if self.interpZ is not None:
            self.elev = self.interpZ.copy()

        # Read plate IDs from gPlates exports
        velfile = self.paleoVelocityPath + "/vel" + str(int(self.tNow)) + "Ma.xy"
        data = pd.read_csv(
            velfile,
            sep=r"\s+",
            engine="c",
            header=None,
            na_filter=False,
            dtype=float,
            low_memory=False,
        )
        data = data.drop_duplicates().reset_index(drop=True)
        llvel = data.iloc[:, 0:2].to_numpy()
        gplateID = data.iloc[:, -1].to_numpy().astype(int)
        vtree = cKDTree(llvel)
        dist, ids = vtree.query(self.lonlat, k=1)
        self.plateIds = gplateID[ids]

        return
