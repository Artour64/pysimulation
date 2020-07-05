worldX=32
worldY=24




class Entity:
	eType="entity"
	name="name"
	pic=""
	foodmax=0
	food=0
	foodrate=0;
	
	hungerDamage=0
	
	healthmax=0
	health=0
	healthrate=0;
	
	def tickCommon():
		food-=foodrate
		if(food<0):
			food=0
			health-=hungerDamage
		health+=healthrate
	
	def tick():
		tickCommon()
		tickSpecial()
	
	def tickSpecial():#tick specific to sub classes. overide it
		pass
	
	def initCommon():
		name=eType
	
	def initHealthy():
		initCommon()
		food=foodmax
		health=healthmax
	

class Plant(Entity):
	foodmax=10
	foodrate=-1
	
	healthmax=10
	healthmax=1

class TileEnv:
	pass

class Tile:
	x=0
	y=0
	env=TileEnv()
	entity=list()

grid=list()
for x in range(worldX):
	grid.append(list())
	for y in range(worldY):
		t=Tile()
		grid[x].append(t)
		t.x=x
		t.y=y

def tick():
	for x in grid:#x is row
		for y in x:#y is tile
			for c in y.entity:#c is entity
				c.tick()#entity tick
	
