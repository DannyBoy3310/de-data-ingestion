import inspect

import psycopg2
from click import option

from ingestion.utils.getLogger import Logger


def connect_DB(logger: Logger, args):
    logger.func_call(inspect.stack()[0][3], "Initiated")

    try:
        conn = psycopg2.connect(
            host=args.audit_host,
            database=args.audit_schema,
            user=args.audit_username,
            password=args.audit_password,
            port=args.audit_port,
            options=f"-c search_path={args.audit_dbname}",
        )
        conn.autocommit = True
        conn.cursor()
    except psycopg2.errors.ConnectionException:
        raise ConnectionError("Audit Database cannot be connected !!!")

    logger.message("Connection to Audit DB Successful !!!")
    logger.func_call(inspect.stack()[0][3], "Completed ")

    return True
