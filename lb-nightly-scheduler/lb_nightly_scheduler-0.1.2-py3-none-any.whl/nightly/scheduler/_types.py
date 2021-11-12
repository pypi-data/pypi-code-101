###############################################################################
# (c) Copyright 2020-2021 CERN for the benefit of the LHCb Collaboration      #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "LICENSE".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################
import os
from contextlib import contextmanager
from typing import Union

import luigi
from lb.nightly.configuration import Package, Project, Slot
from lb.nightly.configuration import get as _get
from lb.nightly.configuration import service_config
from lb.nightly.utils.Repository import connect


class ArtifactTarget(luigi.target.Target):
    def __init__(
        self, project: Union[Project, Package, Slot], stage: str, platform: str = ""
    ):
        from lb.nightly.db.database import Database

        conf = service_config()
        artifacts_repo = conf.get("artifacts", {}).get("uri") or os.environ.get(
            "LBNIGHTLY_ARTIFACTS_REPO"
        )
        self.repo = connect(artifacts_repo)
        self.stage = stage
        self.artifact_name = project.artifacts(stage, platform)
        self.project = project.name
        self.docname = Database.docname(
            project if isinstance(project, Slot) else project.slot
        )

    def artifact_ready(self):
        return self.repo.exist(self.artifact_name)

    def summary_ready(self):
        import lb.nightly.db

        if self.stage == "checkout":
            summary = (
                lb.nightly.db.connect()[self.docname]
                .get("checkout", {})
                .get("projects", {})
                .get(self.project, {})
            )
            return "artifact" in summary

        else:
            return True

    @contextmanager
    def acquire_lock(self):
        """
        Context manager to prevent that multiple tasks try to produce the same
        artifact.
        """
        import lb.nightly.db

        with lb.nightly.db.connect().lock(
            self.artifact_name.replace("/", ":"), info={"artifact": self.artifact_name}
        ) as doc_id:
            yield doc_id

    def exists(self):
        return self.summary_ready() and self.artifact_ready()


class SlotParameter(luigi.parameter.Parameter):
    def parse(self, slot: str):
        """
        Expect a string like "[flavour/]slotname[/build_id]" and return the slot
        instance.
        """
        return _get(slot)

    def serialize(self, slot: Slot):
        """"""
        return slot.id()


class ProjectParameter(luigi.parameter.Parameter):
    def parse(self, project: str):
        """
        Expect a string like "[flavour/]slotname[/build_id]/project" and return the slot
        instance.
        """
        return _get(project)

    def serialize(self, project: Union[Project, Package]):
        """"""
        return project.id()
