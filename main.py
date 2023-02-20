switches = [False] * 101


def update():
    # Loop through all the people from 1 to 100
    for person in range(1, 101, 1):
        # Loop through all the rooms from 0 to 100 with steps of "person"
        for room in range(0, 101, person):
            # If the switch in the current room is off (False), turn it on (True)
            if not switches[room]:
                switches[room] = True
            # If the switch in the current room is on (True), turn it off (False)
            else:
                switches[room] = False
    # Return the updated state of the switches
    return switches


if __name__ == '__main__':
    # Call the update function to update the state of the switches
    update()
    # Loop through all the rooms from 1 to 100
    for i in range(1, 101, 1):
        # prints list of all room numbers and final state
        print(i, ": ", switches[i])
