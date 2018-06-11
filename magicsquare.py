
def main():

	print("Welcome to Magic Square Tester - 2017")
	cond = 'Y'
	while cond == 'Y':
		square = builder()
		tester(square)
		cond = input('Test another Magic Square? Y/N: ')

	

def builder():
	num0 = input('enter top-left number: ')
	num1 = input('enter top-middle number: ')
	num2 = input('enter top-right number: ')
	num3 = input('enter middle-left number: ')
	num4 = input('enter middle number: ')
	num5 = input('enter middle-right number: ')
	num6 = input('enter bottom-left number: ')
	num7 = input('enter bottom-middle number: ')
	num8 = input('enter bottom-rigt number: ')

	square = [[num0,num1,num2],
			  [num3,num4,num5],
			  [num6,num7,num8]]
	return square

def tester(square):

	sum = int(square[0][0]) + int(square[0][1]) + int(square[0][2])
	sum += int(square[1][0]) + int(square[1][1]) + int(square[1][2])
	sum += int(square[2][0]) + int(square[2][1]) + int(square[2][2])
	sum += int(square[0][0]) + int(square[1][1]) + int(square[2][2])
	sum += int(square[0][0]) + int(square[1][0]) + int(square[2][0])
	sum += int(square[0][1]) + int(square[1][1]) + int(square[2][1])
	sum += int(square[0][2]) + int(square[1][2]) + int(square[2][2])
	sum += int(square[0][2]) + int(square[1][1]) + int(square[2][0])

	if sum == 120:
		print('Wow! A Magic Square')
	else:
		print('Ouch! Not a Magic Square')


main()