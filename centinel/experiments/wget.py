import os
import logging

from centinel.experiment import Experiment

class CensorShipExperiment(Experiment):
    name = "wget"

    def __init__(self, input_file):
        self.input_file  = input_file
        self.results = []

    def run(self):
        for line in self.input_file:
            self.host = line.strip()
            self.wget_test()

    def wget_test(self):
        result = {
            "host" : self.host,
        }

        logging.info("Running wget to %s" % self.host)
        response = os.system("wget " + self.host + " | grep \"Length:\" "+ " >results.txt 2>&1")

        if response != 0:
            result["success"] = 'true'
        else:
            result["success"] = 'false'

        self.results.append(result)
	print response
