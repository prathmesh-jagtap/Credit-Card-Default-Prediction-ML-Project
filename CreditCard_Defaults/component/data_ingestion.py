import sys
import os
from zipfile import ZipFile
import pandas as pd
from CreditCard_Defaults.exception import DefaultException
from CreditCard_Defaults.logger import logging
from CreditCard_Defaults.entity.artifact_entity import DataIngestionArtifact
from CreditCard_Defaults.entity.config_entity import DataIngestionConfig
from urllib.request import urlretrieve
from sklearn.model_selection import StratifiedShuffleSplit


class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as error:
            raise DefaultException(error, sys) from error

    def download_CreditCard_data(self,) -> str:
        try:
            # extraction remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            # folder location to download file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir

            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)

            os.makedirs(tgz_download_dir, exist_ok=True)

            defaults_file_name = os.path.basename(download_url)

            tgz_file_path = os.path.join(tgz_download_dir, defaults_file_name)

            logging.info(
                f"Downloading file from :[{download_url}] into :[{tgz_file_path}]")
            urlretrieve(download_url, tgz_file_path)
            logging.info(
                f"File :[{tgz_file_path}] has been downloaded successfully.")
            return tgz_file_path

        except Exception as error:
            raise DefaultException(error, sys) from error

    def extract_tgz_file(self, tgz_file_path: str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir, exist_ok=True)

            logging.info(
                f"Extracting tgz file: [{tgz_file_path}] into dir: [{raw_data_dir}]")

            with ZipFile(tgz_file_path, mode='r') as default_zip_file_obj:
                default_zip_file_obj.extractall(path=raw_data_dir)
            logging.info("Extraction completed")

        except Exception as error:
            raise DefaultException(error, sys) from error

    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            file_name = os.listdir(raw_data_dir)[0]

            defaults_file_path = os.path.join(raw_data_dir, file_name)

            logging.info(f"Reading csv file: [{defaults_file_path}]")
            default_data_frame = pd.read_csv(defaults_file_path)
            default_data_frame.drop(columns=['ID'], axis=1, inplace=True)
            default_data_frame.rename(columns={'PAY_0': 'PAY_1', 'SEX': 'GENDER', 'default.payment.next.month': 'DEFAULTS'},
                                      inplace=True)

            if default_data_frame['GENDER'].dtypes == "O":
                default_data_frame['GENDER'].replace(
                    {'Male': 1, 'Female': 2}, inplace=True)

            logging.info(f"\n{default_data_frame.columns}\n")
            logging.info("Splitting data into train and test")
            strat_train_set = None
            strat_test_set = None

            X = default_data_frame.drop(columns=['DEFAULTS'])
            y = default_data_frame["DEFAULTS"]

            split = StratifiedShuffleSplit(
                n_splits=1, test_size=0.2, random_state=42)

            for train_index, test_index in split.split(X, y):
                strat_train_set = default_data_frame.loc[train_index]
                strat_test_set = default_data_frame.loc[test_index]

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                           file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                          file_name)

            if strat_train_set is not None:
                os.makedirs(
                    self.data_ingestion_config.ingested_train_dir, exist_ok=True)
                logging.info(
                    f"Exporting training datset to file: [{train_file_path}]")
                strat_train_set.to_csv(train_file_path, index=False)

            if strat_test_set is not None:
                os.makedirs(
                    self.data_ingestion_config.ingested_test_dir, exist_ok=True)
                logging.info(
                    f"Exporting test dataset to file: [{test_file_path}]")
                strat_test_set.to_csv(test_file_path, index=False)

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                                            test_file_path=test_file_path,
                                                            is_ingested=True,
                                                            message="Data ingestion completed successfully."
                                                            )
            logging.info(
                f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as error:
            raise DefaultException(error, sys) from error

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            tgz_file_path = self.download_CreditCard_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
            return self.split_data_as_train_test()
        except Exception as error:
            raise DefaultException(error, sys) from error

    def __del__(self):
        logging.info(f"{'='*20}Data Ingestion log completed.{'='*20} \n\n")
