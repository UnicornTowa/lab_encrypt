letters = 'бвгдежзийклмнопрстуфхцчшщъыьэюя'

to_pos = {}
ind = 0
for symbol in letters:
    to_pos[symbol] = ind
    ind += 1


def caesar(string, shift):
    res = ''
    string = str(string).lower()
    for letter in string:
        letter = str(letter)
        if letter in letters:
            res += letters[(to_pos[letter] + int(shift)) % 31]
        else:
            res += letter
    return res


def domain(string):
    return str(string.split(' ')[-1].split('.')[0])

with open('encrypred_address.txt') as f:
    with open('decrypted_address.txt', 'w') as rf:
        for line in f:
            line = str(line).rstrip().lower()
            for i in range(31):
                i += 1
                shifted = caesar(line, i)
                if domain(shifted) == 'кв':
                    rf.write(shifted + '\n')
                    break