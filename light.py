#!/usr/bin/python3
import time
import colorama
from colorama import Fore
from colorama import Style
import json

crossroad = 3
sec = 15
sign={}
colorama.init()
for i in range(1,crossroad+1,1):
	if i == 1:
		c = 'GREEN'
		t = sec
	else:
		c = 'RED'
		t = sec*(i-1)
	sign[f'L{i}'] = {'C':c,'T':t}
#gg = Fore.GREEN

while True:
	s = ''
	#tm = {'GREEN':[],'RED':[]}
	#tm['RED'].append(sign[k]['T'])

	for k in sign:
		if sign[k]['C'] == 'GREEN' and sign[k]['T'] <= 5:
			s += Fore.YELLOW + f"\t{sign[k]['T']}\t"
		elif sign[k]['C'] == 'GREEN':
			s += Fore.GREEN + f"\t{sign[k]['T']}\t"
		else:
			s += Fore.RED + f"\t{sign[k]['T']}\t"
	print(s,end='\r')

	for ss in sign:
		sign[ss]['T'] -= 1
		if sign[ss]['T'] <= 0 and sign[ss]['C'] == 'GREEN':
			sign[ss]['T'] = (crossroad-1)*sec
			sign[ss]['C'] = 'RED'
		elif sign[ss]['T'] <= 0 and sign[ss]['C'] == 'RED':
			sign[ss]['T'] = sec
			sign[ss]['C'] = 'GREEN'
		#tm.append(sign[ss]['T'])
		

	time.sleep(1)