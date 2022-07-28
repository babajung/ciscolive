r'''
'''
import json
import requests
import configparser
import os
import sys
from pathlib import Path
from urllib.parse import unquote
from urllib.parse import quote
from datetime import datetime, timedelta
import calendar
from crayons import blue,red,green,white,cyan
from pprint import pprint
from prettytable import PrettyTable
import pandas as pd

def utc_to_local(utc_dt):
    # get integer timestamp to avoid precision lost
    timestamp = calendar.timegm(utc_dt.timetuple())
    local_dt = datetime.fromtimestamp(timestamp)
    assert utc_dt.resolution >= timedelta(microseconds=1)
    return local_dt.replace(microsecond=utc_dt.microsecond)

def utc_timestamp_to_local(utc_epoch):
    timestamp = calendar.timegm( datetime.fromtimestamp(utc_epoch).timetuple())
    local_dt = datetime.fromtimestamp(timestamp)
    return local_dt

def read_json(filename):
    try:        
        with open (filename, 'r') as fp:
            data = json.loads(fp.read())
    except:
        data = {}
    finally:
        pass
    return data

def write_json(filename, data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)
    except:
        pass
    finally:
        pass

#------------------------------------------------------------------------------------------

def to_unicode(c):
    t = not (c.isalpha() or c in ['.'])
    return t

def unicode_escape(s):
    return "".join(map(lambda c: rf"\u{ord(c):04x}" if to_unicode(c) else c, s))

#------------------------------------------------------------------------------------------

def dict_tostring(d, keys, delimeter="_"):
    dict_tos = ''
    m = []
    for k, v in d.items():
        if k in keys:
            if type(v) == type(dict()):
                #v_tos=dict_tostring(v, ['id', 'type', 'label'], '/')
                v_tos=dict_tostring(v, ['label'], '/')
            else:
                v_tos = str(v)
            m.append(v_tos)
    dict_tos = delimeter.join(m)
    return dict_tos

def list_tostring(l):
    list_tos = ''
    m = []
    for item in l:
        t = type(item)
        if t == type(str()):
            m.append(str(item))
        elif t == type(0):
            m.append(str(item))
        elif t == type(dict()):
            #m.append(dict_tostring(item, ['id', 'type', 'label']))
            m.append(dict_tostring(item, ['label']))
    list_tos = "|".join(m)
    return list_tos

def tostring(k,v):
    tos = None
    t = type(v)
    if t == type(str()):
        tos = str(v)
    elif t == type(0):
        tos = v
    elif t == type(list()):
        tos = list_tostring(v)
    return tos

def printable(data_list):
    p = []
    for record in data_list:
        r = {}
        for k,v in record.items():
            tos = tostring(k, v)
            # print(f"key\t\t{k}")
            # print(f"value\t\t{tos}")
            # '-'.join(tos.split())
            #tos = '-'.join(tos.split())
            r.update({k:tos})
        p.append(r)
    return p

def read_result_from_file(filename):
    fname = f"{filename}.json"
    filedname = repository_root / fname
    print(green("===> Read data from file {}".format(filedname)))
    r = read_json(filedname)
    return r

def save_result_to_file(r, filename):
    # Save output to file
    fname = f"{filename}.json"
    filedname = repository_root / fname
    output = r
    print(green("===> Save output into file {}".format(filedname)))
    write_json(filedname, output)

    # Use pandas to export data to csv files
    fname = f"{filename}.csv"
    filedname = repository_root / fname
    p = printable(output['data'])
    df = pd.DataFrame(p)
    df.to_csv(filedname)
    print(green("===> Save output into file {}".format(filedname)))

def print_result(r):
    print('-'*80)
    print(cyan(f"** OUTPUT **"))
    print(json.dumps(r, indent=2, sort_keys=True))
    print('-'*80)

def init_main():
    global here
    global repository_root
    here = Path(__file__).parent.absolute() if '__file__' in locals() else Path().parent.absolute()
    repository_root = (here).resolve() / "data"
    return here, repository_root
