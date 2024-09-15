from enum import Enum


class FrameworkConstants:

    class IngestionConstants(Enum):

        ENTITY_NAME = "ENTITY_NAME"
        SOURCE_SYSTEM = "SOURCE_SYSTEM"
        FILE_NAMING_CONVENTION = "FILE_NAMING_CONVENTION"
        FREQUENCY = "FREQUENCY"
        FILE_FORMAT = "FILE_FORMAT"
        STAGING = 'STAGING'
        PRIMARY_KEY = 'PRIMARY_KEY'

    class EntityConstants(Enum):
        ENTITY_NAME = "ENTITY_NAME"
        COLUMN_NAME = "COLUMN_NAME"
        DATA_TYPE = "DATA_TYPE"
        DATA_LENGTH = "DATA_LENGTH"
        DATA_SCALE = "DATA_SCALE"
        COLUMN_SECURITY = "COLUMN_SECURITY"
        ADDITIONAL_INFO = "ADDITIONAL_INFO"

    class DateFormat(Enum):
        YEAR = {
            "YYYY": "%Y",
            "YY": "%y",
            "yy": "%y",
        }
        MONTH = {
            "MM": "%m",
            "mm": "%m",
            "MON": "%b",
        }
        DAY = {
            "DD": "%d",
            "dd": "%d",
        }


