__author__ = 'eaboytes'
import yaml
import json

mylist=[1,2,3,4,5,"somestring","anotherstring",{"ip1":"10.1.1.1","ip2":"10.2.2.2"}]
#print mylist

print yaml.dump(mylist, default_flow_style=False)

with open("exercise6.yml", "w") as f:
    f.write(yaml.dump(mylist, default_flow_style=False))

with open("exercise6.json", "w") as g:
    json.dump(mylist, g)
