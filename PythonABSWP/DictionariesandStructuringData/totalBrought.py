allPlayers = {'Prasad': {'TTRacket': 2, 'TTBalls': 5, 'CricketBat': 1, 'CricketBalls': 3},
	       'Nilesh': {'CricketBat': 2, 'CricketBalls': 1, 'BasketBall': 1},
	       'Priyanka': {'BadmintonRacket': 2, 'ShuttleCock': 5, 'SquashRacket': 2},
               'Nikita': {'BadmintonRacket': 2, 'SquashBall': 2},
               'Anusha': {'LudoBoard': 1, 'CarromTable': 1, 'CarromCoinsSet': 2}}

def totalBrought(players, accessories):
	numberInTotal = 0
	for k, v in players.items():
		numberInTotal = numberInTotal + v.get(accessories, 0)
	return numberInTotal

print('Number of accessories brought:')
print(' - Cricket Bats	         ' + str(totalBrought(allPlayers, 'CricketBat')))
print(' - Table Tennis Racket   ' + str(totalBrought(allPlayers, 'TTRacket')))
print(' - Table Tennis Balls    ' + str(totalBrought(allPlayers, 'TTBalls')))
print(' - CricketBalls          ' + str(totalBrought(allPlayers, 'CricketBalls')))
print(' - Basketball ball       ' + str(totalBrought(allPlayers, 'BasketBall')))
print(' - Badminton Racket      ' + str(totalBrought(allPlayers, 'BadmintonRacket')))
print(' - Shuttle Cock          ' + str(totalBrought(allPlayers, 'ShuttleCock')))
print(' - Squash Racket         ' + str(totalBrought(allPlayers, 'SquashRacket')))
print(' - Squash Ball           ' + str(totalBrought(allPlayers, 'SquashBall')))
print(' - Ludo Board            ' + str(totalBrought(allPlayers, 'LudoBoard')))
print(' - Carrom Table          ' + str(totalBrought(allPlayers, 'CarromTable')))
print(' - Carrom Coins Set      ' + str(totalBrought(allPlayers, 'CarromCoinsSet')))

