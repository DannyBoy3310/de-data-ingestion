from ingestion.processing.encryptPII import encrypt_pii
from ingestion.processing.formFileName import form_file_name
from ingestion.processing.readSourceData import read_source_data
from ingestion.processing.saveToTarget import save_to_target
from ingestion.source.createSparkSession import create_spark_session
from ingestion.source.readIngestionMetadata import read_ingestion_metadata
from ingestion.utils.loadArguments import load_arguments
from ingestion.utils.getLogger import Logger


def ingest_data():
    ingestion_metadata,entity_metadata = read_ingestion_metadata(spark, arguments, logger, 'ingestion'),read_ingestion_metadata(spark, arguments,logger,type='entity')
    file_name = form_file_name(logger,arguments,ingestion_metadata)
    dataframe = read_source_data(spark,file_name,arguments,logger,ingestion_metadata)
    dataframe = encrypt_pii(dataframe,arguments,logger,ingestion_metadata,entity_metadata)
    dataframe.show(1, truncate = False)
    # encrypt_pii(dataframe,arguments,logger,ingestion_metadata)
    save_to_target(dataframe, arguments, logger)

if __name__ == "__main__":
    arguments = load_arguments()
    logger = Logger()
    spark = create_spark_session(arguments, logger)
    ingest_data()
    logger.spark_session('Closing', arguments)