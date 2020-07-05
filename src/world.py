worldX=32
worldY=24

grid=list()

class Entity:
	pass

class TileEnv:
	pass

class Tile:
	x=0
	y=0
	env=TileEnv()
	entity=list()

for x in range(worldX):
	grid.append(list())
	for y in range(worldY):
		t=Tile()
		grid[x].append(t)
		t.x=x
		t.y=y
		
