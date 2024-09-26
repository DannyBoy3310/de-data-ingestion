import inspect
from google.cloud import secretmanager
from ingestion.env.config import salt_key, project_id


def get_salt_value(logger, arguments):
    logger.func_call(inspect.stack()[0][3], "initiated")

    client = secretmanager.SecretManagerServiceClient()
    request_id = f"projects/{project_id}/secrets/{salt_key}/versions/1"
    secret_val = client.access_secret_version(request={"name": request_id})

    logger.func_call(inspect.stack()[0][3], "Completed ")

    return secret_val.payload.data.decode("utf-8")
