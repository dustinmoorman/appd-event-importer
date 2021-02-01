# AppD Event Importer

A tool to take data outside of AppD and pull it into AppD as events.  This repo is meant to be a starting point for data ingress into AppD, as well as demonstrate the ease of working with the AppDynamics API for custom events, and intended to be extended and modified to fit your data storage requirements by providing an easy way to extract data with Python.


## Usage

1. `mv accountName.txt.dist accountName.txt` and replace it with your Global Account Name
2. `mv apiKey.txt.dist apiKey.txt` and replace the contents with your Analytics API Key
3. Run `python3 run.py`
