import itertools 

def solve_59():
	f = open('cipher1.txt')
	encrypted = next(f).split(',')
	encrypted = [int(i) for i in encrypted]
	f.close()

	a_ascii = ord('a')
	z_ascii = ord('z')

	ascii_list = range(a_ascii, z_ascii+1)

	possible_passwords = itertools.product(ascii_list, ascii_list, ascii_list)

	password = [0,0,0]
	
	for a,b,c in possible_passwords:
		password[0] = a
		password[1] = b
		password[2] = c

		tmp = [0]*len(encrypted)
		for i, char in enumerate(encrypted):
			tmp[i] = chr(char^password[i%3])

		str_tmp = ''.join(tmp)
	
		is_translation = True


		is_translation &= 'in' in str_tmp
		is_translation &= 'the' in str_tmp
		is_translation &= 'is' in str_tmp
		is_translation &= 'an' in str_tmp
		is_translation &= 'to' in str_tmp
		is_translation &= 'all' in str_tmp
		
		if is_translation:
			translation = str_tmp

	return sum([ord(char) for char in translation])
