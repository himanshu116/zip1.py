import re
from urllib.request import *
sites ="yahoo  rediff flipkart".split()
print(sites)
for i in sites:
	print("searching",i,"sites...")
	u=urlopen("http://"+i+".com")
	content=u.read()
	title=re.findall
	for j in title