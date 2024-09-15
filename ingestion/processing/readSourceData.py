import inspect

import pyspark.sql

from ingestion.env import FrameworkConstants
from ingestion.utils.getLogger import Logger


def read_source_data(
    spark: pyspark.sql.SparkSession,
    file_name,
    arguments,
    logger: Logger,
    ingestion_metadata,
):

    logger.func_call(inspect.stack()[0][3], mode="initiated")

    if ingestion_metadata[FrameworkConstants.IngestionConstants.FILE_FORMAT.value].lower() == "csv":
        dataframe = spark.read.csv(
            f"gs://{arguments.source_bucket}/{arguments.source_dir}/{file_name}csv",
            header=True,
        )
    elif (
        ingestion_metadata[FrameworkConstants.IngestionConstants.FILE_FORMAT.value].lower()
        == "json"
    ):
        dataframe = spark.read.json(
            f"gs://{arguments.source_bucket}/{arguments.source_dir}/{file_name}json",
            multiLine=True,
        )
    elif (
        ingestion_metadata[FrameworkConstants.IngestionConstants.FILE_FORMAT.value].lower()
        == "parquet"
    ):
        dataframe = spark.read.parquet(
            f"gs://{arguments.source_bucket}/{arguments.source_dir}/{file_name}parquet",
        )
    else:
        raise ValueError(
            f"Unacceptable File Format : {ingestion_metadata[FrameworkConstants.IngestionConstants.FILE_FORMAT.value].lower() }"
        )

    dataframe = dataframe.toDF(*[col.upper().strip() for col in dataframe.columns])

    logger.func_call(inspect.stack()[0][3], mode="Completed")

    return dataframe
