import os
import yaml
import fnmatch

class Config:

    def __init__(self):
        config_file = None
        for root, dirname, filenames in os.walk(os.getcwd()):
            for filename in fnmatch.filter(filenames, ".pcconfig"):
                config_file = f"{root}/{filename}"
                break
        config = {}
        try:
            with open(config_file, "r") as fh:
                config = yaml.safe_load(fh)
        except TypeError:
            # No config, so just move on
            pass
        self.__set_settings(config)

    def __set_settings(self, config: dict = {}):
        # TODO: Need better way to handle non-extant
        #       configuration file
        if "storage" not in config:
            config["storage"] = {}
        for setting in config:
            setattr(self, setting, config[setting])
