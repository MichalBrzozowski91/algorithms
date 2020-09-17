class Solution:
    def isRobotBounded(self, instructions) -> bool:
        # We calculate composition of all instructions
        direction = 0 # 0: North, 1: West, 2: South, 3: East
        movement = {0: [0,1],1: [-1,0],2: [0,-1],3: [1,0]}
        position = [0,0]
        for letter in instructions:
            if letter == 'L':
                direction = (direction - 1) % 4
            elif letter == 'R':
                direction = (direction + 1) % 4
            elif letter == 'G':
                position[0] += movement[direction][0]
                position[1] += movement[direction][1]
        if direction == 0 and position != [0,0]: # Robot moved but did not rotate
            return False
        else:
            return True
