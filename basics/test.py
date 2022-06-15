list_length = int(input('Enter list length: '))

words = []
length = []
for i in range(list_length):
    word = input('Enter word: ')
    words.append(word)

for i in words:
    length.append(len(i))

print(words)
print(length)