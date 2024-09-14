from pyspark.sql import SparkSession
import inspect

def create_spark_session(arguments, logger):

    logger.start_func(inspect.stack()[0][3], 'initiated')
    spark = (
        SparkSession.builder.appName(f"Ingestion_{arguments.entity_name}")
        .config(
            "spark.jars",
            "https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar",
        )
        .enableHiveSupport()
        .getOrCreate()
    )
    spark._jsc.hadoopConfiguration().set(
        "fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem"
    )
    # This is required if you are using service account and set true,
    spark._jsc.hadoopConfiguration().set("fs.gs.auth.service.account.enable", "true")
    spark._jsc.hadoopConfiguration().set(
        "google.cloud.auth.service.account.enable", "true"
    )

    spark._jsc.hadoopConfiguration().set(
        "google.cloud.auth.service.account.json.keyfile",
        "/Users/ranjithm/PycharmProjects/Daniel/de_ingestion/de-data-ingestion/security/leafy-stock-435514-e0-83d62a88be90.json"
    )

    logger.spark_session('Initiated', arguments)
    logger.start_func(inspect.stack()[0][3], 'Completed !!')

    return spark
