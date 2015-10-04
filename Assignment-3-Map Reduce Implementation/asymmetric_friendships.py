import MapReduce
import sys
import json

mr = MapReduce.MapReduce()


def mapper(record):
    # key: document identifier
    # value: document contents
    person = record[0]
    friend = record[1]
    record.sort()
    mr.emit_intermediate(str(record[0]+','+record[1]),1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    person = key.split(',')
    p = tuple(person)
    for friend in list_of_values:
      total=total+1
    if total==1:
      mr.emit((person[0],person[1]))
      mr.emit((person[1],person[0]))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
