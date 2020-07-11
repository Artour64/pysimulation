import random

worldX=32
worldY=24

class Entity:
	eType="entity"
	pic=""
	
	foodmax=0
	foodrate=0;
	hungerDamage=0
	healthmax=0
	healthrate=0;
	
	def __init__(self):
		self.name="eType"
		self.food=0
		self.health=0
	
	def tickCommon(self):
		self.food-=self.foodrate
		if(self.food<0):
			self.food=0
			self.health-=self.hungerDamage
		self.health+=self.healthrate
	
	def tick(self):
		self.tickCommon()
		self.tickSpecial()
	
	def tickSpecial(self):#tick specific to sub classes. overide it
		pass
	
	def initCommon(self):
		self.name=self.eType
	
	def initHealthy(self):
		self.initCommon()
		self.food=self.foodmax
		self.health=self.healthmax
	

class Plant(Entity):
	eType="plant"
	pic="grass.png"
	foodmax=10
	foodrate=-1
	
	healthmax=10
	healthmax=1

class TileEnv:
	pass

class Tile:
	x=0
	y=0
	def __init__(self):
		self.env=TileEnv()
		self.entity=list()

grid=list()
for x in range(worldX):
	grid.append(list())
	for y in range(worldY):
		t=Tile()
		grid[x].append(t)
		t.x=x
		t.y=y
		#print((id(t),id(t.entity)))

def worldGen():
	for i in range(64):
		randX = random.randrange(worldX)
		randY = random.randrange(worldY)
		grid[randX][randY].entity.append(Plant())
		
def printworld():
	s="\n"
	for x in grid:
		for y in x:
			e=y.entity
			s+=str(id(e))+","
		s+="\n"
	print(s)

def tick():
	for x in grid:#x is row
		for y in x:#y is tile
			for c in y.entity:#c is entity
				c.tick()#entity tick
	
