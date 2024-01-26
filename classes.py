import random
import uuid


class Player:
	def __init__(self):
		self.id = str(uuid.uuid4())
		self.history = []
		self.seed = random.Random().random()
		self.currentRanking = PlayerRanking()

	def startNewRound(self):
		self.seed = random.Random().random()
		self.history.append(self.currentRanking)
		self.currentRanking = PlayerRanking()

	def getHistoricalPriorityScores(self):
		summation = 0
		for historicalRank in self.history:
			summation += historicalRank.getPriorityScore()
		return summation


	def __str__(self):
		idString = " ".join(["Player ID:",self.id])
		seedString = " ".join(["Current seed:", str(self.seed)])
		currentRanking = "\n".join(["Current ranking:",str(self.currentRanking)])



class RankPlacement:
	def __init__(self, rankedCubeCount, placedIndex, placedCubeId):
		self.rankedCubeCount = rankedCubeCount
		self.placedCubeIndex = placedIndex
		self.placedCubeId = placedCubeId
	
	def getPriorityScore(self):
		score = 0
		# TODO: We should have some way to balance out
		# having only a couple cubes ranked and getting none of them
		# versus having 10 ranked and getting your 8th pick.
		if(self.rankedCubeCount > 0):
			score = placedCubeIndex / rankedCubeCount
		return score


class PlayerRanking:
	def __init__(self):
		self.rankedCubes = []
		self.vetoedCubes = []
		self.avoidPlayedCubes = True

	def __str__(self):
		ranked = "\n".join(self.rankedCubes)
		vetoed = "\n".join(self.vetoedCubes)
		avoidPlayed = "".join(["Avoid played?: ",str(avoidPlayedCubes)])
		return "\n".join([ranked,vetoed,avoidPlayed])

class Cube:
	def __init__(self):
		self.id = str(uuid.uuid4())

class CubePod:
	MAX_PLAYERS = 8
	def __init__(self, cubeId):
		self.id = cubeId
		self.players = []


class Round:
	def __init__(self):
		self.players = {}
		self.cubes = {}