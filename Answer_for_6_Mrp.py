import json
import re


today,yesterday,tday_mfile,yday_mfile = [],[],[],[]

def getJSON(file, day):
    with open(file, 'r+') as f_path:
        for line in f_path:
            day.append(json.loads(line))
    return day

today_file = getJSON('C:\\Users\dell\Downloads\DW_Json\\today.json.gz_out', today)
yesterday_file = getJSON('C:\\Users\dell\Downloads\DW_Json\\yesterday.json.gz_out', yesterday)

for line in today_file[0:10]:
        try:
                if (line["mrp"] == "0") or (re.match("^\d+?\.\d+?$", line["mrp"]) is None) or (line["mrp"] == None):
                        line["mrp"] = "NA"
        except TypeError:
                line["mrp"] = "NA"
        tday_mfile.append(line)

for line in yesterday_file[0:10]:
        try:
                if (line["mrp"] == "0") or (re.match("^\d+?\.\d+?$", line["mrp"]) is None) or (line["mrp"] == None):
                        line["mrp"] = "NA"
        except TypeError:
                line["mrp"] = "NA"
        yday_mfile.append(line)

open("normalmrp_t.json", 'a').close()
open("normalmrp_y.json", 'a').close()

with open("C:\\Users\dell\Downloads\DW_Json\\normalmrp_t.json", "w") as f:
    json.dump(tday_mfile, f)

with open("C:\\Users\dell\Downloads\DW_Json\\normalmrp_y.json", "w") as f:
    json.dump(yday_mfile, f)