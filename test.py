import logging
from CreditCard_Defaults.pipeline.pipeline import Pipeline
from CreditCard_Defaults.exception import DefaultException


def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()

    except Exception as error:
        logging.error(error)


if __name__ == "__main__":
    main()
