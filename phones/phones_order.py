dict_phones = {}
with open('decrypted_phones.txt') as f:
    for line in f:
        line = line.split(':')
        key = line[0]
        value = line[1].rstrip()
        dict_phones[key] = value

ordered_phones = []
with open('ordered_hashes.txt') as f:
    for line in f:
        ordered_phones.append(line.rstrip())
with open('ordered_phones.txt', 'w') as f:
    for key in ordered_phones:
        f.write(dict_phones[key] + '\n')
