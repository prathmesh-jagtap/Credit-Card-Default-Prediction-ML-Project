import logging
from datetime import datetime
import os
import pandas as pd
# from CreditCard_Defaults.constant import get_current_time_stamp

LOG_DIR = "logs"


def get_log_file_name():
    return f"log_{get_current_time_stamp}"


LOG_FILE_NAME = get_log_file_name()

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode='W',
                    format="[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s^;%(message)s",
                    level=logging.INFO
                    )


def get_log_dataframe(file_path):
    data = []
    with open(file_path) as log_file:
        for line in log_file.readline():
            data.append(line.split("^;"))

    log_df = pd.DataFrame(data)
    columns = ['Time Stamp', 'Log Level', 'Line Number',
               'File Name', 'Function Name', 'Message']
    log_df.columns = columns

    log_df['log_message'] = log_df['Time Stmap'].astype(
        str) + ":$" + log_df["Message"]
    return log_df[["log_message"]]
