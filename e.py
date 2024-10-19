number = 9
heights = [4, 5, 6, 4, 2, 3, 6, 6, 6]
final = []
prev = 0

for i in range(number):
    if i == number-1 and prev <= heights[i]:
        final.append(heights[i])
    elif prev <= heights[i] and heights[i] <= heights[i+1]:
        final.append(heights[i])
        prev = heights[i]
    elif heights[i+1] < prev:
        print(prev)
        final.append(heights[i])
        print(heights[i])
        prev = heights[i]
"""     else:
        heights.remove(i) """
    

print(final)