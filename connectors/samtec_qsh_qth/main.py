#!/usr/bin/env python3
import os, csv

dir_path = os.path.dirname(os.path.realpath(__file__))

name = "samtec_qsh_qth"
with open(os.path.join(dir_path, f"{name}.csv"),'w') as fp:
    writer = csv.writer(fp,delimiter=',')
    writer.writerow([name])
    writer.writerow(["Name","Pin",'Side'])
    for i in range(1,65):
        writer.writerow([str(i),str(i),'left'])
