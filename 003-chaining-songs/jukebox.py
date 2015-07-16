#!/usr/bin/python
import json
import re
import random
import itertools


json_data = open("song-library.json").read()
data = json.loads(json_data)

newlist = []
oldlist = []
# creat list of songs
for item in data:
	song = item['song']
	# clean up song titles to be able to determine last letter
	clean = re.findall(r'\w+', song)
	song = " ".join(clean)
	oldlist.append(song)

c = itertools.cycle(oldlist)
word = random.choice(oldlist)
newlist.append(word)
search = word[-1].upper()
nextitem = c.next()
for i in range(4):
	if nextitem[0] == nextitem[-1]:
		nextitem = c.next()
	else:
		while (not nextitem.startswith(search)):
			nextitem = c.next()
		newlist.append(nextitem)
		while nextitem in oldlist: oldlist.remove(nextitem)
		search = nextitem[-1].upper()

print newlist
