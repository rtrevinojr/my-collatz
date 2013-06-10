

# ----
# generates 1000 lines of test code
# ----

import random
import StringIO

def random_gen() :
	
	cnt = 0
	out = open('RanGen.out', 'w')
	while cnt < 1000 :
	    
	    i = random.randint(1, 1000)
	    j = random.randint(i = i + 1, 1001)
	    out.write( str(i) + " " + str(j) + "\n" )
	    cnt = cnt + 1

random_gen()


	
