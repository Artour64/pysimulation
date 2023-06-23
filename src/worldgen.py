import random
import world
import tileEnvironment as tenv

dCache = None

adjoffsets = [[0,1],[0,-1],[1,0],[-1,0]]

def gen_bit(w):
	import render as r
	global dCache
	
	data = dCache
	if dCache == None:
		data = world.World().grid
		
		for x in data:
			for y in range(len(x)):
				x[y] = tenv.allset()
		dCache=data
	
	did = False
	lowLen = tenv.allLen
	lowList = []
	
	for x in range(len(data)):
		for y in range(len(data[x])):
			if w.grid[x][y].env.type == "none":
				filter_square(w.grid,data,x,y)
				thisLen = len(data[x][y])
				if thisLen == 1:
					w.grid[x][y].env = tenv.getTile(list(data[x][y])[0])
					r.renderTile(w.grid[x][y])
					did = True
				elif thisLen == 0:
					#print("backtrack not implemented")
					pass
				elif not did:
					if thisLen == lowLen:
						lowList.append(w.grid[x][y])
					elif thisLen <= lowLen:
						lowList = [w.grid[x][y]]
						lowLen = thisLen
	
	if not did and len(lowList) > 0:
		tile = random.choice(lowList)
		choiceList = []
		for c in data[tile.x][tile.y]:
			t = tenv.getTile(c)
			if t.weight > 0:
				for i in range(t.weight - 1):
					choiceList.append(c)
		tile.env = tenv.getTile(random.choice(choiceList))
		r.renderTile(tile)
					

def filter_square(w,data,x,y):
	global adjoffsets
	adj = set()
	for c in adjoffsets:
		x2 = x + c[0]
		y2 = y + c[1]
		if x2 > -1 and y2 > -1:
			if x2 < len(data) and y2 < len(data[x]):
				t = w[x2][y2].env.type
				if t != "none":
					adj.add(t)

	if len(adj) > 0:
		for c in adj:
			data[x][y].intersection_update(tenv.getTile(c).rules)
	

