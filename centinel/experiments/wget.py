import os
import logging
import time
from centinel.experiment import Experiment
''' This experiment is beign written to detect censorship on the basis of length if a web-page. 
In this experiment we ran wget command to download and save a web page and,
then check file stat to get the size of downloaded page and append into the result for evaluation.'''

class CensorShipExperiment(Experiment):
    name = "wget" #Name of the experiment
	
    def __init__(self, input_file):
        self.input_file  = input_file
        self.results = []

    def run(self):
        for line in self.input_file:
            self.host = line.strip()
            self.wget_test()

    def wget_test(self):
        result = {
            "host" : self.host,	#First field in JSON object 
        }

        logging.info("Running wget to %s" % self.host)
        response = os.system("wget -O " + self.host+ " "+self.host) #Run wget command to download the index.html page of the request host and save that page as the same name of the host.
	size_info = os.stat(self.host) #Get the size of the webpage saved
	size = size_info.st_size
	print size
        if size != 0 && response == 0: # we will get response equal to 0 only when wget dont get any errors
            result["success"] = 'true'
	    result["size"] = size
        else:
            result["success"] = 'false'
	    result["size"] = 0
        self.results.append(result)
