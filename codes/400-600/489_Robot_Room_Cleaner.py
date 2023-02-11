class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0, 1, set())
    
    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        # if finish/ reach an end / find solution
        robot.clean()
        visited.add((x, y))
        # iterate over all candidate
        for k in range(4):
            xx = x + direction_x
            yy = y + direction_y
            # if the next move is a valid move
            if (xx, yy) not in visited and robot.move():
                # continue exploring
                self.dfs(robot, xx, yy, direction_x, direction_y, visited)
                # backtrack
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            # anti-clockwise for the next candidate
            robot.turnLeft()
            direction_x, direction_y = -direction_y, direction_x 