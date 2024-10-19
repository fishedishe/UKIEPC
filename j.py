NumComputers = int(input())
originalNet = []
newNet = []
throughPut = []
priorityCons = []

for i in range(NumComputers -1):
    net = input()
    net = net.split(" ")
    originalNet.append(net)

connections = int(input())

for i in range(connections):
    net = input()
    net = net.split(" ")
    if 10 in net:
        priorityCons.append(net)
    throughPut.append(net)
    
if len(priorityCons) == NumComputers:
    # Check to see if no computer has more than 3 connections
    for con in priorityCons:
        if con
    # Also check to see that all computers are connected
    
else:
    # Return the original connections