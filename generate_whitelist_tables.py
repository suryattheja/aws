import json

if __name__ == "__main__":

  with open("whitelist_tables.json","r") as f:
    json_input = json.load(f)

  whitelist=[]
  for rule in json_input["TableStatistics"]:
    if("temp" not in rule["TableName"]):
      whitelist.append((rule["SchemaName"],rule["TableName"]))

  with open("/Users/suryatamraparni/workspace/dms_whitelist/include/include_tables.csv","w") as f:
    for tup in whitelist:
      f.write(tup[0]+","+tup[1]+"\n")

