import inspect
from datetime import datetime

import pyspark.sql

from pyspark.sql.functions import lit, to_date


def save_to_target(dataframe: pyspark.sql.DataFrame, arguments, logger):

    logger.func_call(inspect.stack()[0][3], "Initiated")

    data_count = dataframe.count()

    target_dest = f"gs://{arguments.target_bucket}/{arguments.target_dir}/"

    logger.message(f"Data Count before saving to Destination: {data_count}")

    ingestion_date = datetime.strptime(arguments.execution_date, "%Y-%m-%d").strftime(
        "%Y%m%d"
    )

    dataframe = dataframe.withColumn("INGESTION_DATE", lit(ingestion_date))

    logger.message(f"Writing data to Lake: {target_dest}")

    dataframe.write.mode(
        "append" if arguments.run_mode.lower() != "full" else "overwrite"
    ).partitionBy("INGESTION_DATE").parquet(path=target_dest)

    logger.func_call(inspect.stack()[0][3], "Completed !!")
