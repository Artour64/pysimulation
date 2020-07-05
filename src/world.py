worldX=32
worldY=24

grid=list()

class Tile:
	x=0
	y=0
	pass

for x in range(worldX):
	grid.append(list())
	for y in range(worldY):
		t=Tile()
		grid[x].append(t)
		t.x=x
		t.y=y
		
