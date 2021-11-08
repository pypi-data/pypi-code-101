from logging import Logger
from pyspark.sql import DataFrame

from featurestorebundle.feature.FeatureStore import FeatureStore
from featurestorebundle.feature.FeatureDataMerger import FeatureDataMerger
from featurestorebundle.feature.FeaturesStorage import FeaturesStorage
from featurestorebundle.feature.TablePreparer import TablePreparer
from featurestorebundle.feature.FeaturesPreparer import FeaturesPreparer
from featurestorebundle.feature.writer.FeaturesWriterInterface import FeaturesWriterInterface
from featurestorebundle.db.TableNames import TableNames


class FeatureStoreWriter(FeaturesWriterInterface):
    def __init__(
        self,
        logger: Logger,
        feature_store: FeatureStore,
        table_preparer: TablePreparer,
        features_preparer: FeaturesPreparer,
        feature_data_merger: FeatureDataMerger,
        table_names: TableNames,
    ):
        self.__logger = logger
        self.__feature_store = feature_store
        self.__table_preparer = table_preparer
        self.__features_preparer = features_preparer
        self.__feature_data_merger = feature_data_merger
        self.__table_names = table_names

    def write_latest(self, features_storage: FeaturesStorage, archive=False):
        features_data = self.prepare_features(features_storage)
        feature_list = features_storage.feature_list
        entity = features_storage.entity

        table = f"{self.__table_names.get_db_name(entity.name)}.{self.__table_names.get_latest_table_name(entity.name)}"
        metadata_path = self.__table_names.get_latest_metadata_path(entity.name)
        pk_columns = [entity.id_column]
        feature_store_type = "databricks"

        self.__feature_data_merger.merge(
            entity,
            feature_list,
            features_data,
            pk_columns,
            table,
            metadata_path,
            feature_store_type,
        )

    def write_historized(self, features_storage: FeaturesStorage):
        features_data = self.prepare_features(features_storage)
        feature_list = features_storage.feature_list
        entity = features_storage.entity

        table = f"{self.__table_names.get_db_name(entity.name)}.{self.__table_names.get_historized_table_name(entity.name)}"
        metadata_path = self.__table_names.get_historized_metadata_path(entity.name)
        pk_columns = [entity.id_column, entity.time_column]
        feature_store_type = "databricks"

        self.__feature_data_merger.merge(
            entity,
            feature_list,
            features_data,
            pk_columns,
            table,
            metadata_path,
            feature_store_type,
        )

    def prepare_features(self, features_storage: FeaturesStorage) -> DataFrame:
        return self.__features_preparer.prepare(features_storage)
