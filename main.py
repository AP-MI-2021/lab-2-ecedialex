import math

def is_prime(nr):
	'''
	Determinca daca un numar citit este prim.
	Input: nr -numar intreg , citit de la tastatura
	Output: True - daca numarul este prim
			Fasle - daca numarul nu este prim
	'''
	if nr < 2:
		return False
	for i in range(2, nr): # 2, 3, ..., nr - 1
		if nr % i == 0:
			return False

	return True

def get_largest_prime_below(n) -> int:
	'''
	Determina primul numar prim mai mic decat un numar citit
	Input: n - numar intreg , citit de la tastatura.
	Output: minim - ultimul număr prim mai mic decât un număr dat.
	'''
	ok=0
	for i in range(n-1,1,-1):
		if is_prime(i):
			return i
	return 0
def test_get_largest_prime_below():
	assert get_largest_prime_below(5) == 3
	assert get_largest_prime_below(2) == 0
	assert get_largest_prime_below(1) == 0
	assert get_largest_prime_below(-1) == 0
	assert get_largest_prime_below(666013) == 665993
	assert get_largest_prime_below(18) == 17
def perfect_square(n):
	'''
	Determina daca un numar dat este patrat perfect
	Input: n -numar pozitiv , citit de la tastatura
	Output: True - daca numarul este patrat perfect
			Fasle - daca numarul nu este patrat perfect
	'''
	x=math.sqrt(n)
	if int(x)**2 == n:
		return True
	return False

def get_perfect_squares(start: int, end: int) -> list[int]:
	'''
	Afișează toate pătratele perfecte dintr-un interval închis dat.
	Input: start - nr intreg , citit de la tastatura
			 end - nr intreg citit de la tastatura
	Output: Afiseaza toate patratele perfecte din intervalul [start,end]
	'''
	list=[]
	if start > end:
		start,end=end,start
	for i in range (start, end+1):
		if perfect_square(i):
			list.append(i)
	if len(list) !=0:
		return list
	else:
		return False
def test_get_perfect_squares():
	assert get_perfect_squares(3,10) == [4,9]
	assert get_perfect_squares(10,3) == [4,9]
	assert get_perfect_squares(0,0) == [0]
	assert get_perfect_squares(1,1) == [1]
	assert get_perfect_squares(2,4) == [4]
	assert get_perfect_squares(1,100) == [1,4,9,16,25,36,49,64,81,100]
def main():

	while True:
		print('1. Găsește ultimul număr prim mai mic decât un număr dat.	')
		print('2. Afișează toate pătratele perfecte dintr-un interval închis dat.')
		print('x. Exit')
		optiune = input('Alegeti o optiune: ')
		if optiune == '1':
			numar = int(input('Dati numarul: '))
			print(get_largest_prime_below(numar))

		elif optiune == '2':
			start = int(input('Primul numar : '))
			end = int(input('Al doilea numar : '))
			if get_perfect_squares(start,end) :
				print(get_perfect_squares(start,end))
			else:
				print(f"nu exista patrate perfecte intre {start} si {end}. ")

		elif optiune == 'x':
			break
		else:
			print('Optiune invalida.')

test_get_largest_prime_below()
test_get_perfect_squares()
main()