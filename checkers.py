colors = ('' , '+', ' ')
board = []
for x in range(8):
    if x%2==0: color = 1
    else: color = -1
    for y in range(8):
        board.append(colors[color])
        color *= -1
print board




