import json
import ha2lib as ha

f = open("sampleUnivDB.json", "r")
input = json.loads(f.read())

output = ha.ha2(input)

print(json.dumps(output))
