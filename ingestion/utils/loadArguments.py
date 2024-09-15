from argparse import ArgumentParser, Namespace


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
        "--execution-date",
        dest="execution_date",
        required=True,
    )
    return args.parse_args()
