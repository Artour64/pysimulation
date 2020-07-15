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
