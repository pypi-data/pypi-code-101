"""The dataset.py module."""
import dataclasses
import logging
import os
import re
import time
import typing as t
import warnings
from pathlib import Path

import flywheel
import pandas as pd
from fw_utils import AnyPath
from joblib import Parallel, delayed
from tqdm.notebook import tqdm

from .utils import validate_path

log = logging.getLogger(__name__)


@dataclasses.dataclass
class DownloadInfo:
    destination: str = None
    template_path: str = None
    manifest_file_path: str = None
    dataset_file_paths: list = None


# TODO: use core-api definition when found.
DEFAULT_QUERY_FILE_SPEC = {
    "container": "acquisition",
    "filter": {"regex": False, "value": "*.*"},
    "analysis_filter": None,
    "format": None,
    "match": "all",
    "process_files": False,
    "filename": "*.*",
}

QUERY_TO_DATAVIEW_MAP = {"column": "src", "alias": "dst", "type": "type"}


class Dataset:
    def __init__(
        self,
        api_key: t.AnyStr,
        fw_project: t.AnyStr,
        dataview: t.Optional[t.AnyStr] = None,
    ):
        """

        Args:
            api_key (str): A flywheel API key.
            fw_project (str): A flywheel project path in group/project format
            dataview (str): A dataview label defined for that project (optional)
        """
        self._api_key = api_key
        self._project_path = fw_project
        self._download_info = DownloadInfo()
        self._project = None
        self._dataview = None
        self._dataframe = None
        self._client = None
        self._destination = None
        self._query = None
        self._manifest_file_path = None
        self._dataset_file_paths = []
        self._init_client()
        if dataview:
            self.use_view(label=dataview)

    @property
    def client(self) -> flywheel.Client:
        if not self._client:
            self._client = self._init_client()
        return self._client

    def _init_client(self) -> flywheel.Client:
        """Returns a flywheel.Client."""
        if not self._client:
            self._client = flywheel.Client(self._api_key)
            domain = self._client.get_config().site.api_url.split("/")[2]
            user = self._client.get_current_user().email
            log.info(f"Logged in to {domain} as {user}")
        return self._client

    @property
    def project(self) -> flywheel.Project:
        if not self._project:
            self._project = self.client.lookup(self._project_path)
        return self._project

    def _reset_view_frame(self):
        """Reset ``_dataview`` and ``_df`` attributes"""
        self._dataview = None
        self._dataframe = None

    @property
    def dataview(self) -> flywheel.DataView:
        """Returns the dataview."""
        return self._dataview

    def list_views(self):
        if self.project is None:
            raise ValueError("project attribute must be defined.")
        views = self.client.get_views(self.project.id)
        viewsf = [
            {"id": view["_id"], "label": view.label, "description": view["description"]}
            for view in views
        ]
        return pd.DataFrame(viewsf)

    def get_view(self, label: t.AnyStr = None, id_: t.AnyStr = None):
        """Returns the matching DataView in project from label or ID.

        Args:
            label (str): The label of the DataView.
            id_ (str): The ID of the DataView.

        Returns:
            flywheel.DataView: The matching DataView

        Raises:
            ValueError: When ID is not in project or when more than 1 or 0 dataview(s)
                are matching.
        """

        if not label and not id_:
            raise ValueError("label or id must be defined")

        if id_:
            view = self.client.get_view(id_)
            if view.parent not in ["site", self.project.id]:
                return ValueError(f"DataView ID {id_} not in project.")
        else:
            views = self.client.get_views(self.project.id)
            views = [v for v in views if v.label == label]
            if len(views) > 1:
                raise ValueError(
                    f"Found more than 1 DataView matching label {label} " f"in project."
                )
            elif len(views) == 0:
                raise ValueError(
                    f"Found 0 DataView matching label {label} " f"in project."
                )
            else:
                view = views[0]
        return view

    def use_view(self, label: t.AnyStr = None, id_: t.AnyStr = None):
        """Set internal dataview to the view matching label or id."""
        self._reset_view_frame()
        self._dataview = self.get_view(label=label, id_=id_)

    def execute_view(self):
        """Pull the view as a dataframe."""
        if self.dataview:
            with warnings.catch_warnings():
                warnings.simplefilter(action="ignore", category=FutureWarning)
                # TODO: add caching ?
                self._dataframe = self.client.read_view_dataframe(
                    self.dataview, self.project.id
                )
        else:
            log.warning("dataview attribute must be defined to execute a view")

    @property
    def dataframe(self) -> pd.DataFrame:
        """Returns the dataview as a pandas dataframe."""
        if self._dataframe is None:
            self.execute_view()
        return self._dataframe

    def destination(self, destination=None):
        if destination is not None:
            self._destination = destination
            return
        return self._destination

    def query(
        self,
        query: t.Union[t.List[t.AnyStr], t.List[dict]] = None,
        file_spec: t.Dict = None,
        include_ids: bool = False,
        include_labels: bool = False,
    ):
        """Set the internal dataview based on query arguments.
        #TODO: Find reference for file_spec and improve docstring.

        Args:
            query (str): List containing the columns to query without aliases
                e.g. ``["subject", "subject.mlset"]`` or with aliases e.g.
                ``[{'column': 'subject.mlset', 'alias':'ml_set'},
                {'column': 'subject.label', 'alias':'subject'}]``
            file_spec (dict):
            include_ids (bool): If True, include ids (default: False).
            include_labels (bool): If True, include labels (default: False).
        """
        if query is None:
            raise ValueError("query is empty")

        self._reset_view_frame()
        self._query = query
        file_spec = DEFAULT_QUERY_FILE_SPEC if not file_spec else file_spec
        columns = self._translate_query_to_dataview_columns(query)
        builder = flywheel.ViewBuilder(
            container=file_spec["container"],
            filename=file_spec["filename"],
            match=file_spec["match"],
            process_files=file_spec["process_files"],
            include_ids=include_ids,
            include_labels=include_labels,
        )
        for c in columns:
            builder.column(**c)
        self._dataview = builder.build()

    @staticmethod
    def _translate_query_to_dataview_columns(query):
        # TODO: assess if that mapping is really required
        # we might be better of just using the existing dataview one
        columns = []
        for item in query:
            if isinstance(item, str):
                column = {"src": item}
            elif isinstance(item, dict):
                for k in item.keys():  # validate key
                    if k not in QUERY_TO_DATAVIEW_MAP.keys():
                        raise KeyError(
                            f"Unsupported key {k}. Supported keys are {QUERY_TO_DATAVIEW_MAP.keys()}"
                        )
                column = {QUERY_TO_DATAVIEW_MAP[k]: v for k, v in item.items()}
            else:
                raise ValueError(f"item type not supported, ")
            columns.append(column)
        return columns

    def filter(self, exp: str = None):
        """Filter dataframe in place."""
        self.dataframe.query(exp, inplace=True)
        return self.dataframe

    def to_json(self):
        return self.dataframe.to_dict(orient="records")

    def to_csv(self, csv_path: AnyPath = None):
        self.dataframe.to_csv(csv_path)

    def get_folder_size(self, folder):
        total_size = os.path.getsize(folder)
        for item in os.listdir(folder):
            itempath = os.path.join(folder, item)
            if os.path.isfile(itempath):
                total_size += os.path.getsize(itempath)
            elif os.path.isdir(itempath):
                total_size += self.get_folder_size(itempath)
        return total_size

    def _set_destination_file_paths(self, destination, template_path):

        template_path = validate_path(
            template_path, valid_fields=list(self.dataframe.columns)
        )
        file_paths = self.dataframe.apply(
            lambda row: str(
                (Path(destination) / template_path.format(**row.to_dict())).resolve()
            ),
            axis=1,
        )

        if file_paths.duplicated().any():
            self._duplicate_file_paths = file_paths.duplicated()
            raise ValueError(f"Duplicated file paths found : {file_paths}")
        else:
            self._dataframe = self._dataframe.assign(file_path=file_paths)

    @staticmethod
    def download_file(api_key, file_id, dst_file):
        from fw_core_client import CoreClient

        core_client = CoreClient(
            api_key=api_key, client_name="temporary", client_version="0.0.0"
        )
        if not Path(dst_file).parent.exists():
            Path(dst_file).parent.mkdir(parents=True)
        with open(dst_file, "wb") as writer:
            resp = core_client.get(f"/files/{file_id}/download?ticket", stream=True)
            writer.write(resp.content)

    @staticmethod
    def _validate_df_for_download(df: pd.DataFrame):
        """Raises if dataframe not valid for download because columns are missing."""
        if "file_id" not in df.columns:
            raise ValueError("file_id must be a column of the dataframe")
        if "file_path" not in df.columns:
            raise ValueError("file_path must be a column of the dataframe")

    def _write_subfolder_manifests(
        self, destination: AnyPath, subfolders: t.List[str], df: pd.DataFrame
    ):
        """Write a csv for each subfolder generated by template_path."""
        self._dataset_file_paths = []
        subfolder = subfolders[0]
        destination = Path(destination)
        for val in df[subfolder].unique():
            dataset = df[df[subfolder] == val]
            dst_csv = destination / val / f"{val}.csv"
            dataset.to_csv(dst_csv, index=False)
            self._dataset_file_paths.append(str(destination / val / f"{val}.csv"))
            if len(subfolders) > 2:
                self._write_subfolder_manifests(
                    destination / val, subfolders[1:], dataset
                )

    def download(
        self,
        destination: t.AnyStr = None,
        template_path: t.AnyStr = None,
        dry_run: bool = False,
        n_jobs: int = -2,
    ):
        # TODO: replace with fw export hosted
        """Downloads files and populates the dataframe file_path column.

        Args:
            destination (str): Root folder where to download files.
            template_path (str): Template path where file will be downloaded from
                root folder (e.g. '{subject.ml_set}/{file.name}'). Field used must be
                in the dataframe columns.
            dry_run (bool): If True, do not download (default: False).
            n_jobs (int): Number of job in run in parallel (default: -2, e.g. max - 1)
        """
        if not destination:
            raise ValueError("destination is undefined")
        if not template_path:
            raise ValueError("template_path is undefined")

        self._destination = Path(destination)
        if not self._destination.exists():
            self._destination.mkdir(parents=True, exist_ok=True)

        self._set_destination_file_paths(self._destination, template_path)

        start_time = time.monotonic()
        if not dry_run:
            self._validate_df_for_download(self.dataframe)
            # splitting dataframe into n_workers to avoid having
            # to re-instantiate the client for each download
            # n_worker = os.cpu_count() + n_jobs if n_jobs < 0 else n_jobs
            # dataframe_split = np.array_split(self.dataframe.copy(), n_worker)
            # Parallel(n_jobs, prefer="threads")(
            #     delayed(self._download_df_chunk)(self._api_key, df)
            #     for df in tqdm(dataframe_split)
            # )
            # TODO: Fix progress bar for parrallel download
            Parallel(n_jobs)(
                delayed(self.download_file)(self._api_key, r.file_id, r.file_path)
                for _, r in tqdm(self.dataframe.iterrows(), total=len(self.dataframe))
            )
            self.dataframe.to_csv(self._destination / "manifest.csv", index=False)
            self._manifest_file_path = str(
                (self._destination / "manifest.csv").resolve()
            )
            regex = re.compile(r"\{([^}]+)\}")
            subfolders = regex.findall(template_path)
            self._write_subfolder_manifests(destination, subfolders, self.dataframe)

            end_time = time.monotonic()
            end_size = self.get_folder_size(destination)
            MB_factor = 1024 ** 2
            print("Seconds:", end_time - start_time)
            print("Transfered MB:", end_size / MB_factor)
            mbs = end_size / (end_time - start_time) / MB_factor
            print("MB/Sec:", mbs)

            self._download_info = DownloadInfo(
                destination=destination,
                template_path=template_path,
                manifest_file_path=str((self._destination / "manifest.csv").resolve()),
                dataset_file_paths=self._dataset_file_paths,
            )

    def target_schema(self, target_schema=None):
        if target_schema is not None:
            self._target_schema = target_schema
            return
        return self._target_schema

    def generate_target_schema(self):
        if self._dataframe is None:
            raise ValueError("You must first defined a dataview or a query")

        properties = []
        for col in self._dataview["columns"]:
            property = {}
            property["column"] = col["dst"]
            if col.type is not None:
                property["type"] = col["type"]
            properties.append(property)
        self._target_schema = {"properties": properties}

    def validate(self):
        if self._target_schema is not None:
            # check to see that all target schema columns are accounted for
            columns = [col["dst"] for col in self._dataview["columns"]]
            missing_columns = []
            for required in [prop for prop in self._target_schema["properties"]]:
                if required["column"] not in columns:
                    missing_columns.append(required)
            if len(missing_columns):
                print(
                    "ERROR: your query does not satisfy the requirements of the target schema\n"
                )
                print("the following properties were not found in your query\n")
                for required in missing_columns:
                    print(required)
            # warn regarding extra columns not in target schema

    def export(self):
        if self._target_schema is None:
            self.generate_target_schema()
        config = {
            "project": {"project": self._project_path, "project_id": self._project.id},
            "query": {
                "query": self._query,
                "dataview": self._dataview,
            },
            "download": dataclasses.asdict(self._download_info),
            # "process": {"container": self._container, "commands": self._commands},
            "target_schema": self._target_schema,
        }
        return config

    def manifest_file_path(self):
        return self._manifest_file_path

    def dataset_file_paths(self):
        return self._dataset_file_paths

    def print_dir(self, path=None, include_files=False):

        if path is None and self._destination is not None:
            path = str(self._destination)
        else:
            path = "."
        for dirpath, dirnames, filenames in os.walk(path):
            directory_level = dirpath.replace(path, "")
            directory_level = directory_level.count(os.sep)
            indent = " " * 4
            print("{}{}/".format(indent * directory_level, os.path.basename(dirpath)))

            if include_files:
                for f in filenames:
                    print("{}{}".format(indent * (directory_level + 1), f))

    def __repr__(self):
        domain = self._client.get_config().site.api_url.split("/")[2]
        if self._dataframe is not None:
            return self._dataframe
        else:
            return f"{type(self).__name__} ({domain})"
