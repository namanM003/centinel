import os
import logging
import time
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
        response = os.system("wget -O " + self.host+ " "+self.host)
	#os.system("ls -l "+self.host+" > file_stat.txt")
	size_info = os.stat(self.host)
	size = size_info.st_size
	print size
        if size != 0:
            result["success"] = 'true'
	    result["size"] = size
        else:
            result["success"] = 'false'
	    result["size"] = size	
        self.results.append(result)
#	time.sleep(20)
	print response
