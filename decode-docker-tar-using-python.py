import tarfile
import json

# todo: parse parameters and use image file

# check if supplied json is valid
def isJson(string):
    try:
        json.loads(string)
    except ValueError as e:
        #print(e)
        return False
    return True

# open tarfile (from docker save file)
with tarfile.open("815c8c75dfc0.tar", "r") as tf:
    
    # reading manifest data
    manifestData = tf.extractfile("manifest.json").read()
    #print("Manifest:", manifestData)
    
    # decoding config key
    json1 = manifestData.decode('utf8').replace("'", '"')
    json1_data = json.loads(json1)[0]
    configKey = json1_data["Config"]

    # reading config data referenced in manifest data
    configData = tf.extractfile(configKey).read()
    #print("Config:", configData)

    # decoding config data ase json / dictionary - works in theory, some quoting issues to be valid json
    json2 = configData.decode('utf8').replace("'", '"')
    print(isJson(json2))

    for member in tf:
        # extracting version
        if member.get_info()["name"].endswith("json"):
            print(member.get_info()["name"])
            versionData = tf.extractfile(member.get_info()["name"]).read()
            print(versionData)