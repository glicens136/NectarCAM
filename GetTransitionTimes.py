#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#%%python - ServerCacoLogic.1.log
from datetime import datetime
import sys

# getting the name of the logfile

print(sys.argv)
filename = "ServerCacoLogic.log"


if len(sys.argv) > 2:
    filename = sys.argv[1]
elif len(sys.argv)==1:
    print("Usage: GetTransitionTimes logfilename")
    print("Using default logfile")


delta_seconds=0
previous_seconds=0

with open(filename, encoding='utf-8') as entree: 
    for line in entree:
        # line contient déjà un retour à la ligne
#        print(line, end='')
        lin2 = line.strip()
        index = lin2.find("CaCo New State")
        if index>0:
            print("Present state: ",lin2[index+16:])
            date,time_str, rest = lin2.split(maxsplit=2)
            print("Date:", time_str)
            t = datetime.strptime(time_str, "%H:%M:%S.%f")

            total_seconds = (
                t.hour * 3600 +
                t.minute * 60 +
                t.second +
                t.microsecond / 1_000_000
            )
            print("Time in seconds:", total_seconds)
            delta_seconds = total_seconds-previous_seconds
            print("Transition time:", delta_seconds)
            previous_seconds = total_seconds



# In[ ]:




