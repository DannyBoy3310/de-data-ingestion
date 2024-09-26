from argparse import ArgumentParser, Namespace

from pkg_resources import require


def load_arguments():

    args = ArgumentParser()

    args.add_argument(
        "--entity-name",
        dest="entity_name",
        required=True,
    )

    args.add_argument(
        "--source-bucket",
        dest="source_bucket",
        required=True,
    )
    args.add_argument(
        "--source-dir",
        dest="source_dir",
        required=True,
    )
    args.add_argument(
        "--source-file-name",
        dest="source_file_name",
        required=True,
    )
    args.add_argument(
        "--metadata-bucket",
        dest="metadata_bucket",
        required=True,
    )
    args.add_argument(
        "--metadata-dir",
        dest="metadata_dir",
        required=True,
    )

    args.add_argument(
        "--filename-ingestion-metadata",
        dest="filename_ingestion_metadata",
        required=True,
    )

    args.add_argument(
        "--filename-entity-metadata",
        dest="filename_entity_metadata",
        required=True,
    )

    args.add_argument(
        "--target-bucket",
        dest="target_bucket",
        required=True,
    )
    args.add_argument(
        "--target-dir",
        dest="target_dir",
        required=True,
    )
    args.add_argument(
        "--run-mode",
        dest="run_mode",
        required=True,
    )
    args.add_argument(
        "--audit-username",
        dest="audit_username",
        required=True,
    )
    args.add_argument(
        "--audit-password",
        dest="audit_password",
        required=True,
    )
    args.add_argument(
        "--audit-port",
        dest="audit_port",
        required=True,
    )
    args.add_argument("--audit-schema", dest="audit_schema", required=True)
    args.add_argument("--audit-dbname", dest="audit_dbname", required=True)
    args.add_argument("--audit-host", dest="audit_host", required=True)
    args.add_argument("--audit-tablename", dest="audit_tablename", required=True)
    args.add_argument(
        "--execution-date",
        dest="execution_date",
        required=True,
    )
    return args.parse_args()
