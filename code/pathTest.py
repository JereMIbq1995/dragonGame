board = [
[1,1,1,0,1,1,2,1],
[0,0,0,0,1,0,0,1],
[0,1,1,1,0,0,1,1],
[0,1,1,1,0,1,1,1],
[0,0,0,0,0,0,1,1],
[1,0,0,1,1,0,1,1],
[1,0,0,1,0,0,1,1],
[0,0,0,0,0,1,1,1],
[1,1,0,1,1,1,1,1],
]

position = (8,2)

#find line
end = (0,0)
i = 0
for row in board:
    j = 0
    for block in row:
        if block == 2:
            end = (i,j)
        j+=1
    i+=1

slope = (end[1]-position[1])/(end[0]-position[0])

print(slope)

while position != end:
    pass