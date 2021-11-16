"""
FASTGenomics Platform Updater
"""

__copyright__ = "Copyright, Comma Soft AG"
__maintainer__ = "Ralf Karle"
__email__ = "ralf.karle@comma-soft.com"

from fastgenomics import FASTGenomicsClient
import json
import logging
import os
import glob
import shutil
import tempfile
from typing import List

logger = logging.getLogger(__name__)
log_level = logging.WARN


class FASTGenomicsPlatformUpdater(FASTGenomicsClient):
    """ uploads updates to a platform 

    directory structure
        ./analysistypes             - all json files will be uploaded as analysis type
        ./analysistemplates         - all json files will be uploaded as analysis templates
        ./datasettypes              - all json files will be uploaded as dataset type
        ./locations                 - all json files will be uploaded as location
        ./webclient                 - the content will be uploaded as customizesation
        ./ids                       - the content will be uploaded as customizesation
    """

    @staticmethod
    def set_log_level(level):
        """ set the loglevel """
        global log_level
        log_level = level
        log_format = "[%(asctime)s] - %(message)s"
        logging.basicConfig(level=log_level, format=log_format)
        logger.setLevel(level)

    def __init__(self, environment_directory: str):
        super().__init__()
        self.environment_directory: str = environment_directory

    def _get_content(self, file: str) -> str:
        with open(file, "r", encoding='utf-8') as f:
            return f.read()

    def _get_all_files(self, subdirectory: str) -> List[str]:
        directory = self.environment_directory + "/" + subdirectory + "/*.json"
        return glob.glob(directory)

    def update_datasettypes(self):
        """ update dataset types """
        try:
            logger.info("updating datasettypes...")
            files = self._get_all_files("datasettypes")
            for file in files:
                id = os.path.basename(file)
                logger.info(f"  datasettype '{id}'")

                json_content = self._get_content(file)

                resp = self.generic_put_json(self.get_backend_url(
                    "api/datasettypes"), json_content)

        except Exception as err:
            raise Exception(f"Exception while deploying dataset types {err}")

    def update_analysistypes(self):
        """ update analysis types """
        try:
            logger.info("updating analysistypes...")
            files = self._get_all_files("analysistypes")
            for file in files:
                id = os.path.basename(file)
                logger.info(f"  analysistype '{id}'")

                json_content = self._get_content(file)

                resp = self.generic_put_json(self.get_backend_url(
                    "api/analysistypes"), json_content)

        except Exception as err:
            raise Exception(f"Exception while deploying analysis types {err}")

    def update_analysistemplates(self):
        """ update analysis templates """
        try:
            logger.info("updating analysistemplates...")
            files = self._get_all_files("analysistemplates")
            for file in files:
                id = os.path.basename(file)
                logger.info(f"  analysistemplate '{id}'")

                json_content = self._get_content(file)

                o = json.loads(json_content)

                resp = self.generic_get(
                    self.get_backend_url("api/analysistemplates"))
                templates = resp.json()["list"]

                id = None
                for t in templates:
                    if t["shortTitle"] == o["shortTitle"]:
                        id = t["id"]
                        logger.debug(f"found existing analysistemplate '{id}'")
                        break

                if id is None:
                    logger.debug(
                        f"creating analysistemplate with short title '{o['shortTitle']}'")
                    resp = self.generic_post_json(self.get_backend_url(
                        "api/analysistemplates"), json_content)
                    id = resp.text
                else:
                    logger.debug(
                        f"putting analysistemplate with short title '{o['shortTitle']}'")
                    resp = self.generic_put_json(self.get_backend_url(
                        f"api/analysistemplates/{id}"), json_content)

                self.generic_put_json(self.get_backend_url(
                    f"api/analysistemplates/{id}/publish"), json_content)

        except Exception as err:
            raise Exception(
                f"Exception while deploying analysis template {err}")

    def update_locations(self):
        """ update locations """
        try:
            logger.info("updating locations...")
            files = self._get_all_files("locations")
            for file in files:
                id = os.path.basename(file)
                logger.info(f"  location '{id}'")

                json_content = self._get_content(file)

                o = json.loads(json_content)

                resp = self.generic_get(self.get_backend_url("api/location"))
                list = resp.json()

                id = None
                if o.get("id", "") != "":
                    for t in list:
                        if t["id"] == o["id"]:
                            id = t["id"]
                            logger.debug(
                                f"found existing location with id '{id}'")
                            break
                else:
                    for t in list:
                        if t["key"] == o["key"]:
                            id = t["id"]
                            logger.debug(
                                f"found existing location with key'{id}'")
                            break

                if id is None:
                    logger.debug(f"creating location with key '{o['key']}'")
                    resp = self.generic_post_json(self.get_backend_url(
                        "api/location"), json_content)
                else:
                    logger.debug(f"updating location '{id}'")
                    resp = self.generic_put_json(self.get_backend_url(
                        f"api/location/{id}"), json_content)

        except Exception as err:
            raise Exception(f"Exception while deploying locations {err}")

    def reindex(self):
        """ re index all """
        try:
            logger.info("reindexing...")

            logger.info("  reindexing datasets")
            self.generic_patch_json(self.get_backend_url(
                "api/datasets/elastic/reindex"), "")

        except Exception as err:
            raise Exception(
                f"Exception while reindexing {err}")

    @staticmethod
    def _make_archive(source, destination):
        base = os.path.basename(destination)
        name = base.split('.')[0]
        format = base.split('.')[1]
        shutil.make_archive(name, format, source)
        shutil.move('%s.%s' % (name, format), destination)

    def upload_backend_customization(self):
        """ upload a customization """
        try:
            tmpFile = ""
            logger.info("uploading backend customization...")

            directory = self.environment_directory + "/webclient"
            if not os.path.exists(directory):
                logger.debug("no backend customization found")
                return

            tmpFile = tempfile.gettempdir() + "/custom.zip"
            if os.path.exists(tmpFile):
                os.remove(tmpFile)

            FASTGenomicsPlatformUpdater._make_archive(directory, tmpFile)

            response = self.generic_post_file(self.get_backend_url(
                "api/customization"), "custom.zip", tmpFile, "application/zip").text.strip('"')
            logger.info(f"   {response}")

        except Exception as err:
            raise Exception(
                f"Exception while deploying webclient customization {err}")
        finally:
            if tmpFile != "" and os.path.exists(tmpFile):
                os.remove(tmpFile)

    def upload_ids_customization(self):
        """ upload a ids customization """
        try:
            tmpFile = ""
            logger.info("uploading identity server customization...")

            directory = self.environment_directory + "/ids"
            if not os.path.exists(directory):
                logger.debug("no ids customization found")
                return

            tmpFile = tempfile.gettempdir() + "/custom.zip"
            if os.path.exists(tmpFile):
                os.remove(tmpFile)

            FASTGenomicsPlatformUpdater._make_archive(directory, tmpFile)

            response = self.generic_post_file(self.get_identityserver_url(
                "/api/customization"), "custom.zip", tmpFile, "application/zip").text.strip('"')
            logger.info(f"   {response}")

        except Exception as err:
            raise Exception(
                f"Exception while deploying ids customization {err}")
        finally:
            if tmpFile != "" and os.path.exists(tmpFile):
                os.remove(tmpFile)

    def update(self):
        logger.info(f"processing directory '{self.environment_directory}'")
        targetUrl = self.get_platform_url("")
        logger.info(f"targeting {targetUrl}")

        self.update_locations()

        self.upload_ids_customization()
        self.upload_backend_customization()

        self.update_analysistemplates()
        self.update_datasettypes()
        self.update_analysistypes()

        self.reindex()
        logger.info("done.")
