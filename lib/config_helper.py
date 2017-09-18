import os
import yaml
from collections import OrderedDict


class ConfigHelper(object):
    def __init__(self):
        config = self.read_yml('configs')
        self.halo_key = config["halo"]["api_key"]
        self.halo_secret = config["halo"]["api_secret_key"]
        self.policy_id = config["halo"]["policy_id"]
        self.filename = config["filename"]
        self.csv_columns = self.construct_dict(config)

    @classmethod
    def read_yml(self, f):
        yml_path = os.path.join(os.path.dirname(__file__), "../configs/%s.yml" % f)
        return yaml.load(file(yml_path, 'r'))

    def construct_dict(self, config):
        d = OrderedDict()
        for col in config["csv_columns"]:
            for k, v in col.items():
                d[k] = v
        return d
