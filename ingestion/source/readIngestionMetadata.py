import inspect
from argparse import Namespace

from pyspark.sql import SparkSession
from pyspark.sql.functions import trim, col, upper, lit

from ingestion.env import FrameworkConstants
from ingestion.utils.getLogger import Logger


def read_ingestion_metadata(
    spark: SparkSession, arguments: Namespace, logger: Logger, type: str
):
    logger.func_call(inspect.stack()[0][3], "Initiated")
    metadata_data = spark.read.csv(
        path=f"gs://{arguments.metadata_bucket}/{arguments.metadata_dir}/{arguments.filename_ingestion_metadata if type.lower().strip() == 'ingestion' else arguments.filename_entity_metadata}",
        header=True,
        inferSchema=True,
    )

    metadata_data = metadata_data.toDF(
        *[column.upper().strip() for column in metadata_data.columns]
    )

    for column in metadata_data.columns:
        metadata_data = metadata_data.withColumn(column, trim(column).alias(column))

    metadata_data = metadata_data.where(
        trim(upper(col(FrameworkConstants.IngestionConstants.ENTITY_NAME.value)))
        == lit(arguments.entity_name.upper().strip())
    )

    if type.lower().strip() == "ingestion":
        metadata_data = metadata_data.first()
    logger.func_call(inspect.stack()[0][3], "Completed")

    return metadata_data
