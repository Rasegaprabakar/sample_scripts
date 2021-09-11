import json
import os
json_dict = json.load(open('data10.json','r'))


uniq_keys = []
for _dict in json_dict['results']:
    keys = _dict.keys()
    fin_keys_set = set(uniq_keys).union(set(keys))
    uniq_keys = list(fin_keys_set)

print(uniq_keys)
