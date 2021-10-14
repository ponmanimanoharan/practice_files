tail_position = 0
dog_on = True
tail_movement = 0
"""if tail_position == 0:
    t_p += 1
    print(t_p)
else:
    t_p += 0
    print(t_p)
"""
"""while dog_on == True:
    if tail_position == 0:
        tail_position = 1
        print(tail_position)
    else:
        tail_position = 0
        print(tail_position)
    dog_on = False
"""
# while loop example
while tail_movement <= 5:
    if tail_position == 0:
        tail_position = 1
        print(tail_position, tail_movement)
    else:
        tail_position = 0
        print(tail_position,tail_movement)
    #dog_on = False
    tail_movement +=1
print("\n")
# for loop example
for tail_movement in range(6):
    if tail_position == 0:
        tail_position = 1
        print(tail_position)
    else:
        tail_position = 0
        print(tail_position)
# range command with limit
for tail_movement in range(6,18):
    print("The dog moved the tail" + " " + str(tail_movement))
print("\n")
# range command wth skip (backward or forward)
for tail_movement in range(6,18, 2):
    print("The dog moved the tail" +" " +  str(tail_movement))