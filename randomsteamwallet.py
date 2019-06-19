import string, random, os


def generate(size = 5, char = string.ascii_uppercase + string.digits):
	return ''.join(random.choice(char) for i in range(size))

input = input("input length : ")

for i in range(int(input)):
    hmm = generate() + "-" + generate() + "-" + generate()
    print(hmm)
    with open("result.txt", 'a') as out:
        out.write(hmm + '\n')
        out.close()