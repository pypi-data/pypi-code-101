import geopandas as gpd
from pydantic import validator
from typing import Optional, Dict, List

from google.cloud import bigquery
from google.cloud.exceptions import NotFound

from iggyenrich.iggy_data_package import IggyDataPackage, infer_bounds


class BQIggyDataPackage(IggyDataPackage):
    iggy_version_id: str
    parcel_prefix: str
    gcp_project: str
    parcels_dataset: str = "boundary_crosswalks"
    iggy_dataset: str = "deliverables"
    iggy_prefix: Optional[str] = "unified"
    client: Optional[bigquery.Client] = None
    parcel_table: Optional[str] = None
    boundary_tables: Optional[Dict[str, str]] = {}
    parcel_data: Optional[bigquery.Table] = None
    boundary_data: Optional[Dict[str, bigquery.Table]] = {}

    @validator("parcel_table", always=True)
    def set_parcel_table(cls, v, values):
        return (
            v
            or f"{values['gcp_project']}.{values['parcels_dataset']}.{values['parcel_prefix']}_parcels_{values['iggy_version_id']}"
        )

    def load(self, boundaries: List[str] = [], features: List[str] = []) -> None:
        """Check connections to tables and set `boundary_tables`"""
        self.client = bigquery.Client(project=self.gcp_project)

        # check parcels table
        try:
            self.parcel_data = self.client.get_table(self.parcel_table)
            print(f"Found parcel table {self.parcel_table}")
        except NotFound:
            raise Exception(f"Parcel table {self.parcel_table} not found")

        # infer boundaries to load
        bounds_features_to_load = infer_bounds(boundaries, features)
        print(f"Will load boundaries {bounds_features_to_load.keys()}...")

        # load boundaries
        for boundary, boundary_features in bounds_features_to_load.items():
            bnd_table_id = self.boundary_data.get(boundary)
            if not bnd_table_id:
                bnd_table_id = (
                    f"{self.gcp_project}.{self.iggy_dataset}.{self.iggy_prefix}_{boundary}_{self.iggy_version_id}"
                )
            try:
                self.boundary_data[boundary] = self.client.get_table(bnd_table_id)
                print(f"Found boundary table {bnd_table_id}")
            except NotFound:
                raise Exception(f"Boundary table {bnd_table_id} not found")

    def enrich(
        self,
        points: Optional[gpd.GeoDataFrame] = None,
        points_table: Optional[str] = None,
        output_table: Optional[str] = None,
        dry_run: bool = False,
    ) -> gpd.GeoDataFrame:
        """Run BQ queries to enrich a BQ table or geo dataframe. Optionally print queries
        without running them (set `dry_run = True`)"""
        # TODO: separate BigQueryTable class so that we can instantiate from config

        pass
