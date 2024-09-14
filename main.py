from ingestion.extraction.read_dataframe_as_csv import read_dataframe_as_csv
from ingestion.extraction.saveToTarget import save_to_target
from ingestion.source.create_spark_session import create_spark_session
from ingestion.utils.load_arguments import load_arguments
from ingestion.utils.get_logger import Logger


if __name__ == "__main__":
    arguments = load_arguments()
    logger = Logger()
    spark = create_spark_session(arguments, logger)
    dataframe = read_dataframe_as_csv(spark,arguments,logger)
    save_to_target(dataframe,arguments,logger)
    logger.spark_session('Closing', arguments)