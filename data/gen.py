#!/usr/bin/env python

import os
from os import listdir
from os.path import join

RawDataDir = 'rawdata'
DataDir = 'processed_data'
Commands = ["SMILExtract -C config/energy.conf -I %s -O %s/energy/%s",
        "SMILExtract -C config/emo_large.conf -I %s -O %s/emo_large/%s"]
Emos = ['sad', 'angry', 'happy']
count = {'sad':0, 'angry':0, 'happy':0}

#clean
os.system("mkdir processed_data")
os.system("rm -rf processed_data/*")
os.system("mkdir processed_data/energy")
os.system("mkdir processed_data/energy/happy processed_data/energy/angry processed_data/energy/sad")
os.system("cp -r processed_data/energy processed_data/emo_large")
####

for d in listdir(RawDataDir):
    for f in listdir(join(RawDataDir, d)):
        f_path = join(RawDataDir, d, f)

        lf = f.lower()
        ok = False
        for emo in Emos:
            if(lf.startswith(emo)):
                out_path = emo +'/'+ d +str(count[emo])
                count[emo] = count[emo] + 1
                ok = True
                break
        if ok:
            for s in Commands:
                s = s % (f_path, DataDir, out_path)
                print(s)
                os.system(s)
