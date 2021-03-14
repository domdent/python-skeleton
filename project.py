import argparse
import logging
from configparser import ConfigParser

from source import main

LOG_FORMAT = "%(asctime)s [%(levelname)s][%(filename)s:%(funcName)s] %(message)s"

def parse_args():
    parser = argparse.ArgumentParser("Basic config parser")
    parser.add_argument(
        "--config", dest="config", help="The config file path"
    )
    return parser.parse_args()


def parse_config(config_path):
    config = ConfigParser()
    config.read(config_path)
    return config


def setup_logging(config):
    """ Setup basic root logger """
    log_level = config.get("logging", "log_level")
    log_path = config.get("logging", "log_path")
    handler = logging.FileHandler(log_path)
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_level.upper()))
    logger.addHandler(handler)


if __name__ == "__main__":
    args = parse_args()
    config = parse_config(args.config)
    setup_logging(config)
    logging.info("Starting program...")
    main.run(config)
    logging.info("Exiting program...")
