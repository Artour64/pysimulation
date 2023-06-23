
class TileEnv:
	def __init__(self, tileType="none", rules = set(), weight = 100):
		self.type = tileType
		self.rules = rules
		self.weight = weight

#---------------------------------------------------------
#config

flowerWeight = 10

tiles = {
	TileEnv("forest", {"forest","tree"}),
	TileEnv("tree", {"tree","grass","forest"}),
	TileEnv("sand", {"water","sand","grass"}),
	TileEnv("water", {"water","sand","deepwater"}),
	TileEnv("deepwater", {"water","deepwater"},50),
	TileEnv("tallgrass", {"tallgrass","grass", "rock"}),
	TileEnv("rock", {"rock","grass","tallgrass"},50),
	
	TileEnv(
		"grass",
	 	{
			"grass","tallgrass","sand","tree", "rock",
			"flower1","flower2","flower3",
			"flower4","flower5","flower6"
		},
		1000
	),

	TileEnv("flower1", {"grass"},flowerWeight),
	TileEnv("flower2", {"grass"},flowerWeight),
	TileEnv("flower3", {"grass"},flowerWeight),
	TileEnv("flower4", {"grass"},flowerWeight),
	TileEnv("flower5", {"grass"},flowerWeight),
	TileEnv("flower6", {"grass"},flowerWeight)
}

#config
#---------------------------------------------------------

#autofix
for x in tiles:
	for y in tiles:
		if y.type in x.rules:
			if x.type not in y.rules:
				print("fix: " + x.type + ", " + y.type)
				y.rules.add(x.type)
			


tileTypes = set()
for c in tiles:
	tileTypes.add(c.type)

def allset():
	return tileTypes.copy()

tileDict = dict()
for c in tiles:
	tileDict[c.type] = c

def getTile(s):
	return tileDict[s]

#can be optimized with hash map/ table or dict
def getTileOld(s):
	for c in tiles:
		if c.type == s:
			return c
	return None

allLen = len(allset())
