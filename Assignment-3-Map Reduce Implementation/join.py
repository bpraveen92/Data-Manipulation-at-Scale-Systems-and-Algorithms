import MapReduce
import sys
import json


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    record_type = record[0]
    record_id = record[1]
    mr.emit_intermediate(record_id, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    l = []
    for v in list_of_values:
      if v[0]=='order':
        l.extend(v)
      else:
        x = list(l)
        x.extend(v)
        mr.emit(x)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
