import json

genre_list = [{'fd':'jf','kj':'jkd'},{'fd':'jf','kj':'jkd'}]
str_dumps = json.dumps(genre_list)
str_loads = json.loads(str_dumps)

print genre_list, type(genre_list)
print str_dumps, type(str_dumps)
print str_loads, type(str_loads)


