from argparse import Namespace

import pyspark.sql
import inspect

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit, sha2

from ingestion.env import FrameworkConstants
from ingestion.utils.getLogger import Logger


def encrypt_pii(dataframe: pyspark.sql.DataFrame, arguments: Namespace, logger:Logger, ingestion_metadata: pyspark.sql.Row, entity_metadata: DataFrame):

    logger.func_call(inspect.stack()[0][3], 'Initiated')

    if ingestion_metadata[FrameworkConstants.IngestionConstants.STAGING.value].lower() == 'hash':
        columns_to_hash = entity_metadata.filter(col(FrameworkConstants.EntityConstants.COLUMN_SECURITY.value) == lit('PII')).select(col(FrameworkConstants.EntityConstants.COLUMN_NAME.value)).collect()
        for column in columns_to_hash:
            dataframe = dataframe.withColumn(column[0],sha2(column[0],numBits=256))

    logger.func_call(inspect.stack()[0][3], 'Completed !!')

    return dataframe

