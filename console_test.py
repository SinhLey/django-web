word = 'Mama told me to play it cool'

for i in range(len(word)*2 - 1):
    for j in range(len(word)):
        print(word[j:i+1])

