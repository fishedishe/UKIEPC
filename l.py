n = input()
exercises = []
planner = ""
calendar = ""

for i in range(int(n)):
    exercises.append(input())

for i in exercises:
    if "leg" in i:
        planner += "🦿"

    elif "rest" in i:
        planner += "😎"
    
    else:
        planner += "🦾"

while len(calendar) <= 31:
    calendar += planner

string = ""
loops = 0

for i in calendar[:31]:
    if loops == 7:
        loops = 0
        string += "\n"

    string = string + i
    loops += 1

print(string)