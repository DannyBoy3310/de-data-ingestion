import inspect
from argparse import Namespace

import pyspark.sql
from pyspark.sql.functions import lit, sha2, md5, to_date, col, concat

from ingestion.utils.connect_DB import connect_DB
from ingestion.utils.getLogger import Logger


def upload_to_audit(
    logger: Logger,
    arguments: Namespace,
    dataframe: pyspark.sql.DataFrame,
    column_name,
    salt_value,
):
    logger.func_call(inspect.stack()[0][3], "Initiated")
    conn_status = connect_DB(logger, arguments)

    if conn_status:
        audit_data = dataframe.select(
            col(column_name).alias("clear_val"),
            sha2(
                concat(md5(lit(salt_value)), sha2(column_name, numBits=256)),
                numBits=256,
            ).alias("hash_val"),
            to_date(lit(arguments.execution_date),'yyyy-MM-dd').alias("created_dt"),
        )
        properties = {
            "user": arguments.audit_username,
            "password": arguments.audit_password,
            "driver": "org.postgresql.Driver",
        }
        audit_data.write.jdbc(
            url=f"jdbc:postgresql://{arguments.audit_host}:{int(arguments.audit_port)}/{arguments.audit_schema}",
            properties=properties,
            table=f"{arguments.audit_dbname}.{arguments.audit_tablename}",
            mode="append",
        )
    return None
