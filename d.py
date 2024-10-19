q = 1
test = [0, 0, 0]
possible = [1, 2, 3, 4, 5, 6, 7, 8]

answers = {
    1: [0, 0, 0, 0],
    2: [0.0, 0.5, 0.0, -0.5],
    3: [0.5, 0.0, -0.5, 0.0],
    4: [0.25, 0.25, 0.25, 0.25],
    5: [0.5, 0.5, -0.5, -0.5],
    6: [0.5, 0.5, 0.5, -0.5],
    7: [0.5, 0.5, -0.5, 0.5],
    8: [0.75, 0.75, -0.25, -0.25]
}

if test[0] == 0:
    possible.remove(2)
    possible.remove(5)
    possible.remove(6)
    possible.remove(8)
    
    if test[1] == 0:
        possible.remove(3)
        possible.remove(7)

        if test[2] == 0:
            possible.remove(4)

elif test[1] == 0:
    possible.remove(1)
    possible.remove(3)
    possible.remove(4)
    possible.remove(7)
    

    if test[2] == 0:


elif test[2] == 0:
    possible.remove(4)
    possible.remove(6)
    possible.remove(7)
    possible.remove(8)

print(possible)