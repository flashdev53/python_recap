import json
config = {"service": "nginx", "replicas": 3}
with open("config.json", "w") as f:
    json.dump(config, f)
with open("config.json", "r") as f:
    loaded = json.load(f)
print("Loaded Config:", loaded)
