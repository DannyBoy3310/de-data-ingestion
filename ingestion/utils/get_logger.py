import logging


class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO,format='%(asctime)s -- %(message)s')
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.INFO)

    def spark_session(self, mode, args):
        self.logger.info(f"Spark Session {mode} for {args.entity_name}")

    def message(self, msg):
        self.logger.info(msg)

    def start_func(self, function, mode):
        self.logger.info(f"{function} {mode} !!! ")

