import uuid
import os
import sys
import pandas as pd
from collections import namedtuple
from datetime import datetime
from threading import Thread
from typing import List
from multiprocessing import Process
from CreditCard_Defaults.config.configuration import Configuration
from CreditCard_Defaults.logger import logging, get_log_file_name
from CreditCard_Defaults.exception import DefaultException

from CreditCard_Defaults.entity.artifact_entity import ModelPusherArtifact, DataIngestionArtifact, ModelEvaluationArtifact
from CreditCard_Defaults.entity.artifact_entity import DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact
from CreditCard_Defaults.entity.config_entity import DataIngestionConfig, ModelEvaluationConfig
from CreditCard_Defaults.component.data_ingestion import DataIngestion
# from CreditCard_Defaults.component.data_validation import DataValidation
# from CreditCard_Defaults.component.data_transformation import DataTransformation
# from CreditCard_Defaults.component.model_trainer import ModelTrainer
# from CreditCard_Defaults.component.model_evalution import ModelEvaluation
# from CreditCard_Defaults.component.model_pusher import ModelPusher
from CreditCard_Defaults.constant import EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME


class Pipeline:

    def __init__(self, config: Configuration = Configuration()) -> None:
        try:
            self.config = config

        except Exception as error:
            raise DefaultException(error, sys) from error

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(
                data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as error:
            raise DefaultException(error, sys) from error

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as error:
            raise DefaultException(error, sys) from error
