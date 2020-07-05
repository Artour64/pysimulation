worldX=32
worldY=24

grid=list()

class Tile:
	pass

for x in range(worldX):
	grid.add(list())
	for y in range(worldY):
		grid[y].add(Tile())
		
