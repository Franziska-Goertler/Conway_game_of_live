import numpy as np
from PIL import Image

rule_90=np.array ([
	False,# <− 0000 = 0
	True, # <− 0001 = 1
	False,# <− 0010 = 2
	True, # <− 0011 = 3
	True, # <− 0100 = 4
	False,# <− 0101 = 5
	True, # <− 0110 = 6
	False,# <− 0111 = 7
	False,# <− 1000 = 8
	True, # <− 1001 = 9
	False,# <− 1010 =10
	True, # <− 1011 =11
	True, # <− 1100 =12
	False,# <− 1101 =13
	True, # <− 1110 =14
	False # <− 1111 =15
])
rule_shift_right=np.array ([
	False,# <− 0000 = 0
	False, # <− 0001 = 1
	False,# <− 0010 = 2
	False, # <− 0011 = 3
	False, # <− 0100 = 4
	False,# <− 0101 = 5
	False, # <− 0110 = 6
	False,# <− 0111 = 7
	True,# <− 1000 = 8
	True, # <− 1001 = 9
	True,# <− 1010 =10
	True, # <− 1011 =11
	True, # <− 1100 =12
	True,# <− 1101 =13
	True, # <− 1110 =14
	True # <− 1111 =15
])
rule_extinct=np.array ([
	False,# <− 0000 = 0
	False, # <− 0001 = 1
	False,# <− 0010 = 2
	True, # <− 0011 = 3
	False, # <− 0100 = 4
	False,# <− 0101 = 5
	False, # <− 0110 = 6
	True,# <− 0111 = 7
	False,# <− 1000 = 8
	True, # <− 1001 = 9
	True,# <− 1010 =10
	True, # <− 1011 =11
	True, # <− 1100 =12
	True,# <− 1101 =13
	True, # <− 1110 =14
	True # <− 1111 =15
])
rule = rule_extinct
print(f"true:{sum(rule)}, total:{len(rule)}")


evolution_steps = 200
vector_size_x = 300
vector_size_y = 300

state = np.random.choice([True ,False],size= (vector_size_x,vector_size_y) )
state *= np.random.choice([True ,False],size= (vector_size_x,vector_size_y) )


for i in range( evolution_steps ):
	pict = Image.fromarray(state)
	pict.save(f"evolution_{i}.png")
	state = rule[
		1*np.roll(state ,-1,0)+		
		2*np.roll(state ,-1,1)+
		4*np.roll(state ,+1,0)+
		8*np.roll(state ,+1,1)
	]
	print(f"i: {i}, alive: {sum(sum(state))/(vector_size_x*vector_size_y)}")

	
pict = Image.fromarray(state)
pict.save(f"evolution_{i}.png")
