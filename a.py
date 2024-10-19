word_1 = input()
word_2 = input()
outputArr = []
output = ""

if word_1 == word_2:
    print(word_1)
else:
    for char in word_1:
        outputArr.append(char)
    for char in word_2:
        if char not in outputArr:
            outputArr.append(char)
            # make sure that the character is not in the first word before merging it
            # DUPLICATES IN THE SECOND WORD IS FINE
    for char in outputArr:
        output = output + char
    print(output)
    