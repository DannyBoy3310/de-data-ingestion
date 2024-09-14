import inspect

import pyspark.sql

from ingestion.utils.get_logger import Logger


def read_dataframe_as_csv(spark: pyspark.sql.SparkSession, arguments, logger: Logger):

    logger.start_func(inspect.stack()[0][3],mode="initiated")
    dataframe = spark.read.csv(
        f"gs://{arguments.source_bucket}/{arguments.source_dir}/{arguments.source_file_name}.csv",
        header=True,
    )
    dataframe = dataframe.toDF(*[col.upper().strip() for col in dataframe.columns])

    logger.start_func(inspect.stack()[0][3],mode="Completed")

    return dataframe
