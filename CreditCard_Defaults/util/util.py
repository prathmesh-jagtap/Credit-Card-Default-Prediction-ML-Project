import os
import sys
import yaml
import dill
import numpy as np
import pandas as pd
from CreditCard_Defaults.constant import DATASET_SCHEMA_COLUMNS_KEY
from CreditCard_Defaults.exception import DefaultException


def write_yaml_file(file_path: str, data: dict = None):
    """Creates yaml file 

    Args:
        file_path (str): location of file in our directory
        data (dict, optional): Data which is in form of dictionary.

    Raises:
        DefaultException: raise default error
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as yaml_file:
            if data is not None:
                yaml.dump(data, yaml_file)
    except Exception as error:
        raise DefaultException(error, sys) from error


def read_yaml_file(file_path: str) -> dict:
    """Reads a YAML file and returns the contents as a dictionary.

    Args:
        file_path (str): location of read file.

    Raises:
        DefaultException: default error.

    Returns:
        dict: the values of all keys which we want to fetch.
    """

    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as error:
        raise DefaultException(error, sys) from error


def save_numpy_array_data(file_path: str, array: np.array):
    """Save numpy array data to file

    Args:
        file_path (str): location of file where we have to save our data.
        array (np.array): array of data.

    Raises:
        DefaultException: raise default error.
    """

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as error:
        raise DefaultException(error, sys) from error


def load_numpy_array_data(file_path: str) -> np.array:
    """load numpy array data from file

    Args:
        file_path (str): location of file to load.

    Raises:
        DefaultException: Default error.

    Returns:
        np.array: np.array data loaded.
    """

    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as error:
        raise DefaultException(error, sys) from error


def save_object(file_path: str, obj):
    """
    file_path: str
    obj: Any sort of object
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as error:
        raise DefaultException(error, sys) from error


def load_object(file_path: str):
    """
    file_path: str
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as error:
        raise DefaultException(error, sys) from error


def load_data(file_path: str, schema_file_path: str) -> pd.DataFrame:
    try:
        datatset_schema = read_yaml_file(schema_file_path)

        schema = datatset_schema[DATASET_SCHEMA_COLUMNS_KEY]

        dataframe = pd.read_csv(file_path)

        error_messgae = ""

        for column in dataframe.columns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])
            else:
                error_messgae = f"{error_messgae} \nColumn: [{column}] is not in the schema."
        if len(error_messgae) > 0:
            raise Exception(error_messgae)
        return dataframe

    except Exception as error:
        raise DefaultException(error, sys) from error
