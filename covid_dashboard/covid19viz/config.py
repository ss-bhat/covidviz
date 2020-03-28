import os
from configparser import ConfigParser
from covid19viz.utils import errors
import logging

log = logging.getLogger(__name__)


class DashConfigParser:
    """
    This parses the config from config.ini file and return the flatted dictionary object
    """
    config_file_name = "config.ini"
    config_file = '{}/{}'.format(os.getcwd(), config_file_name)

    @staticmethod
    def parse():
        """
        This function parses each section of the config and adds it to a dictionary.
        If parsing and db connection fails stop the execution and give message to check ini file.
        :return:
        """
        log.info("Getting App config from current working directory.. ")
        log.info("Config file: {}".format(DashConfigParser.config_file))
        config = dict()
        if not os.path.isfile(DashConfigParser.config_file_name):
            raise errors.DashConfigError("Config ini files not found")

        log.info("Parsing config...")
        _config = ConfigParser()
        try:
            _config.read(DashConfigParser.config_file)
            for section in _config.sections():
                log.info("Parsing the config section: {}".format(section))

                # Each item in a section.
                for _item in _config.items(section):
                    _key = _item[0]
                    _val = _item[1]
                    config[_key.strip()] = _val.strip()

            return config

        except Exception as e:
            log.error("Something wrong while parsing the config from ini file")
            log.error(e)
            raise errors.DashConfigError("Error in configuration...")
