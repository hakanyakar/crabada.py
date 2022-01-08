from typing import cast
from src.common.types import Tus
from src.helpers.General import secondOrNone, thirdOrNone
from src.strategies.mining.HighestMpStrategy import HighestMpStrategy
from src.common.clients import crabadaWeb2Client
from sys import argv

# VARS
gameId = secondOrNone(argv)
maxPrice = cast(Tus, int(thirdOrNone(argv))) or 20

if not gameId:
    print('Provide a game ID')
    exit(1)

game = crabadaWeb2Client.getMine(gameId)
strategy = HighestMpStrategy(game, crabadaWeb2Client, strict=False, maxPrice=maxPrice)  # setting strict=True will throw error if mine is not reinforceable

# TEST FUNCTIONS
def testHighestMpStrategy() -> None:

    print('>>> CRAB REINFORCEMENT WITH AUTOMATIC SELECTION')
    try:
        print(strategy.getCrab()) # Will print note if mine is not reinforceable
    except Exception as e:
        print('ERROR RAISED: ' + e.__class__.__name__ + ': ' + str(e))

    print('>>> FIRST CRAB REINFORCEMENT')
    print(strategy._getCrab1())
    exit()
    try:
        print(strategy._getCrab1())
    except Exception as e:
        print('ERROR RAISED: ' + e.__class__.__name__ + ': ' + str(e))

    print('>>> SECOND CRAB REINFORCEMENT')
    try:
        print(strategy._getCrab2())
    except Exception as e:
        print('ERROR RAISED: ' + e.__class__.__name__ + ': ' + str(e))

# EXECUTE
testHighestMpStrategy()