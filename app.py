from mylib import *
import threading
import time
from flask import Flask, render_template, request, jsonify, send_from_directory
from crayons import blue,green,red,white,cyan
import numpy as np
from pprint import pprint

app = Flask(__name__)
# init_main() from mylib
here, repository_root = init_main()

# dataset1 = {'data': [{'a': 'a001', 'b': 'b001', 'c': 'c001', 'd': 'd001'}]}
# dataset2 = {'data': [{'a': 'a002', 'b': 'b002', 'c': 'c002', 'd': 'd002'}]}
# dataset3 = {'data': [{'a': 'a003', 'b': 'b003', 'c': 'c003', 'd': 'd003'}]}
# dataset4 = {'data': [{'a': 'a004', 'b': 'b004', 'c': 'c004', 'd': 'd004'}]}

# first = 1
# last = 10
# mylist = list()
# dataset2 = {'data': list()}
# for i in range (first, last+1, 1):
#     item = {'a': str('a'*i), 'b': str('b'*i), 'c': str('c'*i), 'd': str('d'*i)}
#     dataset2['data'].append(item)
# pprint(dataset2)

# load data
import csv
with open('cisco-live.txt') as f:
    a = [{k: str(v).strip() for k, v in row.items()}
        for row in csv.DictReader(f, delimiter='|', skipinitialspace=True)]
print(a[0])
for item in a:
    item['URL'] = f'<a href="{item["URL"]}">Click me</a>'
# use dataset2
dataset2 = {'data': a}

import re
def is_valid_regex(regex):
    try:
        re.compile(regex)
        is_valid = True
    except re.error:
        is_valid = False
    return is_valid

@app.route("/")
def index():
    print(globals().keys())
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("q")
    dataset = request.args.get("dataset")
    # if not q:
    #     return "ERROR: q NOT provided!"
    if not dataset:
        return "ERROR: dataset NOT provided!"
    # assign p with the dataset
    if dataset == 'dataset1':
        p = dataset1['data'].copy()
        columns = ['a', 'b', 'c', 'd']
        return f"ERROR: invalid dataset ({dataset}) !"
    elif dataset == 'dataset2':
        p = dataset2['data'].copy()
        # columns = ['a', 'b', 'c', 'd']
        columns = ['Title', 'URL']
    elif dataset == 'dataset3':
        p = dataset3['data'].copy()
        columns = ['a', 'b', 'c', 'd']
        return f"ERROR: invalid dataset ({dataset}) !"
    elif dataset == 'dataset4':
        p = dataset4['data'].copy()
        columns = ['a', 'b', 'c', 'd']
        return f"ERROR: invalid dataset ({dataset}) !"
    else:
        return f"ERROR: invalid dataset ({dataset}) !"
    df = pd.DataFrame(p)
    df = df.replace(np.nan, '', regex=True)
    df.index += 1
    if not q:
        locdf = df.loc[:]
        print(f"#num of records = {len(locdf)}")
        toh = locdf.to_html().replace("\\n","<br>")
    else:
        if q[0] == "*":
            q = "." + q[:]
        elif q[0] == "?":
            q = "." + q[:]
        elif q[0] == "+":
            q = "." + q[:]
        regex = is_valid_regex(q)
        locdf = df.loc[df['Title'].str.contains(q, case=False, regex=regex), df.columns.isin(columns)]
        print(f"#num of records = {len(locdf)}")
        toh = locdf.to_html().replace("\\n","<br>")
    toh = toh.replace('<tr style="text-align: right;">','<tr style="text-align: left;">')
    toh = toh.replace('<th>', '<th style="min-width: 140px;">')
    toh = toh.replace('<th style="min-width: 40px;">Title</th>', '<th style="width: 100%;">Title</th>')
    toh = toh.replace('&lt;a href','<a href')
    toh = toh.replace('&gt;Click me&lt;/a&gt;', ' target="_blank">Click to download</a>')
    return toh

@app.route("/jquery-3.3.1.min.js")
def jquery():
    return send_from_directory( (here) / "static", "jquery-3.3.1.min.js")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory( (here) / 'static' / 'images',
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

def start_runner():
    def start_loop():
        not_started = True
        count = 0
        while not_started:
            count += 1
            print(cyan(f"** [start_runner_{count:03d}] In start loop **"))
            try:
                r = requests.get('http://127.0.0.1:5000/')
                if r.status_code == 200:
                    print(cyan(f"** [start_runner_{count:03d}] Server started, quiting start_loop **"))
                    not_started = False
                print(cyan(f"** [start_runner_{count:03d}] {r.status_code} **"))
            except:
                print(red(f"** [start_runner_{count:03d}] Server not yet started **"))               
            time.sleep(2)
        print(cyan(f"** [start_runner_{count:03d}] End loop **"))
        if dataset2:
            print(cyan(f"** [start_runner_{count:03d}] #allowed = {len(dataset2['data'])} **"))

    print('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.start()

if __name__ == "__main__":
    start_runner()
    print(cyan(f"** [main_001] before app.run **"))
    app.run(host="0.0.0.0", debug=True)
    print(cyan(f"** [main_002] after app.run **"))
