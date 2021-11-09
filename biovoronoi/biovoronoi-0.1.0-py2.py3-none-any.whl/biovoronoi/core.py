import numpy as np
import pandas as pd
from scipy.spatial import Voronoi, ConvexHull


class Core:
    def set_structure(self, structure):
        self.structure = structure

    def calculate_voronoi_obejct(self):
        atoms = self.structure.get_atoms()
        atom_coordinates = np.array([atom.get_coord() for atom in atoms])
        v = Voronoi(atom_coordinates)
        self.voronoi = v

    def calculate_voronoi_volumes(self):
        volumes = []
        for i, atom in enumerate(self.structure.get_atoms()):
            convex = ConvexHull(
                self.voronoi.vertices[
                    self.voronoi.regions[self.voronoi.point_region[i]]
                ]
            )
            volumes.append(convex.volume)
        self.voronoi_volumes = np.array(volumes)

    def create_df(self):
        data = {
            "atom_name": [],
            "atom_serial_number": [],
            "residue_name": [],
            "residue_id": [],
            "volume": [],
        }
        for atom, volume in zip(self.get_structure().get_atoms(), self.voronoi_volumes):
            data["atom_name"].append(atom.get_name())
            data["atom_serial_number"].append(atom.get_serial_number())
            residue = atom.get_parent()
            data["residue_name"].append(residue.get_resname())
            data["residue_id"].append(residue.get_id()[1])
            data["volume"].append(volume)

        df = pd.DataFrame(data)
        self.df = df

    def groupby_residue(self):
        residue_df = self.df.groupby(["residue_id", "residue_name"]).sum()
        self.residue_df = residue_df

    def get_voronoi_vertices(self):
        return self.voronoi.vertices

    def get_voronoi_volumes(self):
        return self.voronoi_volumes

    def get_structure(self):
        return self.structure

    def get_df(self):
        return self.df

    def get_residue_df(self):
        return self.residue_df
