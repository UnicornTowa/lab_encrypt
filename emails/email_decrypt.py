letters = 'bcdefghijklmnopqrstuvwxyz'

to_pos = {}
ind = 0
for symbol in letters:
    to_pos[symbol] = ind
    ind += 1


def caesar(string, shift):
    res = ''
    for letter in string:
        letter = str(letter)
        if letter in letters:
            res += letters[(to_pos[letter] + int(shift)) % 25]
        else:
            res += letter
    return res


def domain(string):
    return str(string.split('@')[1].split('.')[1])


domains = set()

domains.add('com')
domains.add('biz')
domains.add('net')
domains.add('info')
domains.add('org')

with open('encrypted_emails.txt') as f:
    with open('decrypted_emails.txt', 'w') as rf:
        for line in f:
            line = str(line).rstrip()
            for i in range(25):
                i += 1
                shifted = caesar(line, i)
                if domain(shifted) in domains:
                    rf.write(shifted + '\n')
                    break