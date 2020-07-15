import random

#defaults
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
	
	def tickCommon(self):
		self.food-=self.foodrate
		if(self.food<0):
			self.food=0
			self.health-=self.hungerDamage
		self.health+=self.healthrate
	
	def tickSpecial(self):#tick specific to sub classes. overide it
		pass
		
	def tick(self):
		self.tickCommon()
		self.tickSpecial()
	
	def initCommon(self):
		self.name=self.eType
	
	def initSpecial(self):
		pass
	
	def initHealthy(self):
		self.initCommon()
		self.initSpecial()
		self.food=self.foodmax
		self.health=self.healthmax
	
	def __init__(self):
		self.initHealthy()

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
	def __init__(self):
		self.x=0
		self.y=0
		self.env=TileEnv()
		self.entity=list()
		
class World:
	def __init__(self):
		self.worldX=worldX
		self.worldY=worldY
		self.grid=list()
		for x in range(self.worldX):
			self.grid.append(list())
			for y in range(self.worldY):
				t=Tile()
				self.grid[x].append(t)
				t.x=x
				t.y=y
				#print((id(t),id(t.entity)))

	def worldGen(self):
		randX = random.randrange(self.worldX)
		randY = random.randrange(self.worldY)
		for i in range(128):
			attemps=0
			while(len(self.grid[randX][randY].entity)>0):
				randX = random.randrange(self.worldX)
				randY = random.randrange(self.worldY)
				attemps+=1
				if(attemps>100):
					break
			if(attemps>100):
					break
			self.grid[randX][randY].entity.append(Plant())
			
	
	def tick(self):
		for x in self.grid:#x is row
			for y in x:#y is tile
				for c in y.entity:#c is entity
					c.tick()#entity tick
	'''	
	def print(self):
		s="\n"
		for x in self.grid:
			for y in x:
				e=y.entity
				s+=str(id(e))+","
			s+="\n"
		print(s)
	#'''
	
