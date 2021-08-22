#!/usr/bin/env python3
from subprocess import check_output
from re import findall

def get_cputemp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return float(findall("\d+\.\d+",temp)[0])

#cpu_temp=get_cputemp()
#print(cpu_temp)
