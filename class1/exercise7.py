__author__ = 'eaboytes'
import yaml
import json
from pprint import pprint as pp

with open("exercise6.yml") as f:
    yaml_list=yaml.load(f)

with open("exercise6.json") as g:
    json_list=json.load(g)

print "This is the yaml list"
pp(yaml_list)
print " "
print "This is the json list"
pp(json_list)
