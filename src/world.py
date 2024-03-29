import random
import entity
import tileEnvironment as tenv
import worldgen

#default size
worldX=32
worldY=24

worldX=119
worldY=63

class Tile:
	def __init__(self):
		self.x=0
		self.y=0
		self.env=tenv.TileEnv()
		self.entity=list()
		
class World:
	def __init__(self,x=worldX,y=worldY):
		self.makeGrid()
	
	def makeGrid(self,x=worldX,y=worldY):
		self.worldX=x
		self.worldY=y
		self.grid=list()
		for x in range(self.worldX):
			self.grid.append(list())
			for y in range(self.worldY):
				t=Tile()
				self.grid[x].append(t)
				t.x=x
				t.y=y
				#print((id(t),id(t.entity)))

	def worldGenOld(self):
		randX = random.randrange(self.worldX)
		randY = random.randrange(self.worldY)
		for i in range(64):#generate plants
			attemps=0
			while(len(self.grid[randX][randY].entity)>0):
				randX = random.randrange(self.worldX)
				randY = random.randrange(self.worldY)
				attemps+=1
				if(attemps>100):
					break
			if(attemps>100):
					break
			self.grid[randX][randY].entity.append(entity.Plant())
	
	def worldGen(self):
		pass
			
	
	def tickOld(self):
		for x in self.grid:#x is row
			for y in x:#y is tile
				for c in y.entity:#c is entity
					c.tick()#entity tick

	def tick(self):
		worldgen.gen_bit(self)
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
	
	#the out of bounds check is the purpose of this method
	def tileAt(self,x,y):
		if x < 0 or y < 0:
			return None
			
		g = self.grid
		if x >= len(g):
			return None
		
		g = g[x]
		if y >= len(g):
			return None
			
		return g[y]
	
