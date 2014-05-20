import os
import sys
import json
import glob
import imp

from datetime import datetime

from experiment import Experiment, ExperimentList

EXPERIMENTS_DIR = os.path.join(os.path.dirname(__file__), "experiments")
RESULTS_DIR     = os.path.join(os.path.dirname(__file__), "results")
DATA_DIR        = os.path.join(os.path.dirname(__file__), "data")

def get_result_file():
    result_file = "result-%s.json" % (datetime.now().isoformat())
    return os.path.join(RESULTS_DIR, result_file)

def get_input_file(experiment_name):
    input_file = "%s.txt" % (experiment_name)
    return os.path.join(DATA_DIR, input_file)

def load_experiments():
    # look for experiments in experiments directory
    for path in glob.glob(os.path.join(EXPERIMENTS_DIR,'[!_]*.py')):
        # get name of file and path
        name, ext = os.path.splitext(os.path.basename(path))
        # load the experiment
        imp.load_source(name, path)

    # return dict of experiment names and classes
    return ExperimentList.experiments

def run():
    experiments = load_experiments()

    if not os.path.exists(RESULTS_DIR):
        print "Creating results directory in %s" % (RESULTS_DIR)
        os.makedirs(RESULTS_DIR)

    result_file = get_result_file()
    result_file = open(result_file, "w")
    results = {}

    for name, Exp in experiments.items():
        input_file = get_input_file(name)

        if not os.path.isfile(input_file):
            print "No input file found for %s. Skipping test." % (name)
            continue

        print "Reading input from %s" % (input_file)
        input_file = open(input_file)
        
        print "Running %s test." % (name)
        exp = Exp(input_file)
        exp.run()

        input_file.close()

        results[name] = exp.results

    json.dump(results, result_file)
    result_file.close()

    print "All experiments over. Check results."