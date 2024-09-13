import pyspark.sql


def read_dataframe_as_csv(spark: pyspark.sql.SparkSession,arguments):

    dataframe = spark.read.csv("gs://de-data-dev-transient/STOCKS/HISTORY/AXISBANK-BSE.csv", header = True)
    dataframe = dataframe.toDF(*[col.upper().strip() for col in dataframe.columns])

    return dataframe