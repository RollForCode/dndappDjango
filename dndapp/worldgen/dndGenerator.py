import worldgen.charGen as charGen
import worldgen.buildingGen as buildingGen
import random


def genChar(chars=0, toGen=10, seed=0):
	charlist =[]
	#generate seed if not supplied
	if seed == 0:
		seed = random.randint(0,9999999)

	#set the seed, then, generate npc seed1s
	random.seed(seed)
	npcGenSeeds = [random.randint(0,9999999) for _ in range(toGen)]

	if chars == 0 or not chars:	
		for i, NpcSeed in enumerate(npcGenSeeds):
			charlist.insert(0,(charGen.generateRace(NpcSeed)))
	else:	
		for i, NpcSeed in enumerate(npcGenSeeds):
			charlist.insert(0,(charGen.generateRace(NpcSeed, chars)))
	return charlist

def genBuilding(buildings=0):
	buildingList =[]
	buildingList = buildingGen.generateBuilding()
	return buildingList