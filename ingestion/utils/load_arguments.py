from argparse import ArgumentParser, Namespace


def load_arguments():

    args = ArgumentParser()

    args.add_argument("--entity-name", dest="entity_name")

    args.add_argument("--source-bucket", dest="source_bucket")
    args.add_argument("--source-dir", dest="source_dir", required=True)
    args.add_argument("--source-file-name", dest="source_file_name")
    args.add_argument('--target-bucket',dest='target_bucket')
    args.add_argument('--target-dir', dest='target_dir')
    args.add_argument('--execution-date', dest='execution_date')
    return args.parse_args()
