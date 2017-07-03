import re
import sys
dic={} #empty dict.

pattern = re.compile("(^(.*?)\s)") #Regular expression defined
try:
    filename = input("Enter a file name to get the count: ") 
    fp=open(filename)
except IOError:
    print("No such file found")
    sys.exit()

with open(filename) as fp:
    sys.stdout=open("records_"+filename,"w") 
    for line in fp:
        matchobject=pattern.search(line) #searching the pattern thorugh regex 
        if (matchobject):
            dic[matchobject.group(1)]=dic.get(matchobject.group(1),0)+1 # appending each (key,value) into dictionary by group if object matches
            
for k in sorted(dic.keys()):  # alphabetically sorted data
    print ("%s%d" % (k, dic[k])); #collecting and printing the string and it's count in dic./

sys.stdout.close()
