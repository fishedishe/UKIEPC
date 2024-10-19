from collections import Counter

word_1 = input().lower()
word_2 = input().lower()
output = ""

# loop double pointer
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    one = word_1.count(i)
    two = word_2.count(i)

    if one > two:
        output += i * one
    else:
        output += i * two
    
print(output)
    

# count = Counter(word_1)
# count2 = Counter(word_2)
# found = False

# for pointer in count:
#     if found:
#         pass
#     elif count[pointer] > count2[pointer]:
#         found = True
#         primary = word_1
#         secondary = word_2
#     elif count[pointer] < count2[pointer]:
#         found = True
#         primary = word_2
#         secondary = word_1
#     else:
#         pass

# if found == False:
#     primary = word_1
#     secondary = word_2

# for char in primary:
#     outputArr.append(char)
# for char in secondary:
#     if char not in primary:
#         outputArr.append(char)
# for char in outputArr:
#     output = output + char
# print(output)