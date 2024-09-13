from ingestion.extraction.read_dataframe_as_csv import read_dataframe_as_csv
from ingestion.source.create_spark_session import create_spark_session
from ingestion.utils.load_arguements import load_arguments
import logging


if __name__ == "__main__":
    arguments = load_arguments()
    logging.info(f"Creating Spark Session for {arguments.entity_name}")
    spark = create_spark_session(arguments)

    dataframe = read_dataframe_as_csv(spark,arguments)
    dataframe.show(5, truncate = False)

