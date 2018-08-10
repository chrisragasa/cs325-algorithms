#File Object - Read
#Using context manager ... This will automatically close file when done.
with open('data.txt', 'r') as f:
    array = []
    for line in f:
    	line = line.split()
    	if line:
    		line = [int(i) for i in line]
    		array.append(line)

class Coin:
	count = 0
	def __init__(self, type):
		self.type = type

def makeMinChange(coinDenominationList, totalChange, minCoinsArr, coinsUsedArr):
	for i in range(totalChange + 1):
		coinCount = i
		newCoin = 1
		for j in [c for c in coinDenominationList if c <= i]:
			if minCoinsArr[i - j] + 1 < coinCount:
				coinCount = minCoinsArr[i - j] + 1
				newCoin = j
		minCoinsArr[i] = coinCount
		coinsUsedArr[i] = newCoin
	return minCoinsArr[totalChange]

def printCoins(coinDenominationList, coinsUsedArr, totalChange):
	coinArr = coinDenominationList
	myArr = []
	for i in coinArr:
		newCoin = Coin(i)
		myArr.append(newCoin)

	coin = totalChange
	while coin > 0:
		thisCoin = coinsUsedArr[coin]

		for j in range(len(myArr)):
			if myArr[j].type == thisCoin:
				myArr[j].count += 1

		coin = coin - thisCoin

	coinCount = []
	for k in range(len(myArr)):
		coinCount.append(myArr[k].count)

	return coinCount

def write_to(arr_in, f_in):
	for i in arr_in:
		f_in.write(str(i) + " ")
	f_in.write("\n")

def print_execution_time(denominationList, changeAmount, coinCount, coinsUsed):
	import timeit
	start = timeit.default_timer()
	makeMinChange(denominationList,changeAmount,coinCount,coinsUsed)
	stop = timeit.default_timer()
	print("List = " + str(denominationList) + " Change = " + str(changeAmount) + " Time " + str(stop - start))

def main():
		#Runtimes as a function of A
		amnt = 1500
		clist = list(range(1,6))
		coinsUsed = [0]*(amnt+1)
		coinCount = [0]*(amnt+1)

		print_execution_time(clist, amnt, coinCount, coinsUsed)
		




if __name__ == "__main__":
	main()