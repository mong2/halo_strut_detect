import csv
import os


class CsvWriter(object):
    def __init__(self, config):
        self.filename = config.filename

    def write(self, order, data):
        if os.path.exists("reports/%s.csv" % (self.filename)):
            return self.append_dict(order, data)
        return self.write_dict(order, data)

    def write_dict(self, order, data):
        with open("reports/%s.csv" % (self.filename), "wb") as f:
            writer = csv.DictWriter(f, order)
            writer.writeheader()
            writer.writerow(data)

    def append_dict(self, order, data):
        with open("reports/%s.csv" % (self.filename), "a") as f:
            writer = csv.DictWriter(f, order)
            writer.writerow(data)
