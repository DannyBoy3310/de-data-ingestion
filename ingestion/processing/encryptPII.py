from argparse import Namespace

import pyspark.sql.functions
import inspect

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit, sha2, md5, concat

from ingestion.env import FrameworkConstants
from ingestion.source.getSaltValue import get_salt_value
from ingestion.utils.getLogger import Logger
from ingestion.utils.uploadToAudit import upload_to_audit


def encrypt_pii(
    dataframe: pyspark.sql.DataFrame,
    arguments: Namespace,
    logger: Logger,
    ingestion_metadata: pyspark.sql.Row,
    entity_metadata: DataFrame,
):

    logger.func_call(inspect.stack()[0][3], "Initiated")

    if (
        ingestion_metadata[FrameworkConstants.IngestionConstants.STAGING.value].lower()
        == "hash"
    ):
        columns_to_hash = (
            entity_metadata.filter(
                col(FrameworkConstants.EntityConstants.COLUMN_SECURITY.value)
                == lit("PII")
            )
            .select(col(FrameworkConstants.EntityConstants.COLUMN_NAME.value))
            .collect()
        )
        salt_value = get_salt_value(logger, arguments)
        for column in columns_to_hash:
            upload_to_audit(logger, arguments, dataframe, column[0], salt_value)
            dataframe = dataframe.withColumn(
                column[0],
                sha2(
                    concat(md5(lit(salt_value)), sha2(column[0], numBits=256)),
                    numBits=256,
                ),
            )

    logger.func_call(inspect.stack()[0][3], "Completed !!")
    return dataframe
