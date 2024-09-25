import inspect
from argparse import Namespace
from datetime import datetime

from pyspark.sql import Row
import re
from ingestion.env import FrameworkConstants
from ingestion.utils.getLogger import Logger


def form_file_name(logger: Logger, arguments: Namespace, ingestion_metadata: Row):
    logger.func_call(inspect.stack()[0][3], "Initiated")
    file_naming_convention = ingestion_metadata[
        FrameworkConstants.IngestionConstants.FILE_NAMING_CONVENTION.value
    ]
    regex_pattern = r"_*__(.*?)__*_"
    date_regex = re.search(regex_pattern, file_naming_convention).group(0)

    old_date_format = date_regex
    logger.message(f"Date Regex : {old_date_format}")
    for key, value in FrameworkConstants.DateFormat.YEAR.value.items():
        if key in date_regex:
            date_regex = date_regex.replace(key, value)
    for key, value in FrameworkConstants.DateFormat.MONTH.value.items():
        if key in date_regex:
            date_regex = date_regex.replace(key, value)
    for key, value in FrameworkConstants.DateFormat.DAY.value.items():
        if key in date_regex:
            date_regex = date_regex.replace(key, value)

    new_date_format = date_regex.replace("__", "")

    file_date = datetime.strptime(arguments.execution_date, "%Y-%m-%d").strftime(
        new_date_format
    )

    logger.message(f"The File Date : {file_date}")

    file_name = file_naming_convention.replace(old_date_format, file_date)

    logger.message(
        f"The Source File Name : {file_name}{ingestion_metadata[FrameworkConstants.IngestionConstants.FILE_FORMAT.value].lower()}"
    )

    logger.func_call(inspect.stack()[0][3], "Completed")

    return file_name
