#File Object - Read
#Using context manager ... This will automatically close file when done.
with open('amount.txt', 'r') as f:
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

def main():
	f_out = open('change.txt', 'w')
	coinArr = 0
	coinAmt = 1
	for i in range(len(array) / 2):
		amnt = array[coinAmt][0]
		clist = array[coinArr]
		coinsUsed = [0]*(amnt+1)
		coinCount = [0]*(amnt+1)

		write_to(array[coinArr], f_out)
		write_to(array[coinAmt], f_out)

		minCoinsUsed = [makeMinChange(clist,amnt,coinCount,coinsUsed)]
		
		write_to(printCoins(clist, coinsUsed, amnt), f_out)
		write_to(minCoinsUsed, f_out)

		coinArr += 2
		coinAmt += 2


if __name__ == "__main__":
	main()