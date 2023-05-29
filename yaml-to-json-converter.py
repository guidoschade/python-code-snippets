import yaml
import json

# read in yaml file
with open('config.yaml', 'r') as yaml_file:
    configuration = yaml.safe_load(yaml_file)

# write json file to disk
with open('config.json', 'w') as json_file:
    json.dump(configuration, json_file)

# printing resulting json output formatted
out = json.dumps(json.load(open('config.json')), indent=2)
print(out)