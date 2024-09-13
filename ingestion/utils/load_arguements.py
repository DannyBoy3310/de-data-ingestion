from argparse import ArgumentParser, Namespace

def load_arguments():

    args = ArgumentParser()

    args.add_argument(
        '--entity-name',
        dest='entity_name'
    )

    return args.parse_args()
