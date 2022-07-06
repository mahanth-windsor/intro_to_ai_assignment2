from collections import deque
from turtle import right


class BFS:

    def __init__(self):
        pass

    def solve(self, missionaries, cannibals):
        
        class States:
            def __init__(self, left_miss, left_cann, right_miss, right_cann, boat_position):

                self.left_miss = left_miss
                self.left_cann = left_cann
                self.right_miss = right_miss
                self.right_cann = right_cann
                self.boat_position = boat_position
                self.parent = None

            def __eq__(self, other):
                return (self.left_miss == other.left_miss and self.left_cann == other.left_cann and
                        self.right_miss == other.right_miss and self.right_cann == other.right_cann and
                        self.boat_position == other.boat_position)

            def goal(self):
                if self.left_miss == 0 and self.left_cann == 0 and self.right_miss == missionaries \
                        and self.right_cann == cannibals and self.boat_position == "right":
                    return True
                else:
                    return False

            def check_valid(self):
                if (self.left_miss != 0 and self.left_cann > self.left_miss) \
                        or (self.right_miss != 0 and self.right_cann > self.right_miss) \
                        or self.left_miss < 0 or self.left_cann < 0 or self.right_miss < 0 \
                        or self.right_cann < 0:
                    return False
                else:
                    return True

        def next(curr):

            next_move = []

            all_moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]

            if curr.boat_position == "left": 

                for move in all_moves:

                    result_state = States(curr.left_miss - move[0], curr.left_cann - move[1],
                                       curr.right_miss + move[0], curr.right_cann + move[1], "right")

                    if result_state.check_valid():

                        next_move.append(result_state)
                        result_state.parent = curr

            else:  

                for move in all_moves:

                    result_state = States(curr.left_miss + move[0], curr.left_cann + move[1],
                                       curr.right_miss - move[0], curr.right_cann - move[1], "left")

                    if result_state.check_valid():

                        next_move.append(result_state)
                        result_state.parent = curr

            return next_move

        def bfs(): 

            initial = States(missionaries, cannibals, 0, 0, "left")  

            if initial.goal():
                return initial

            q = deque([])
            is_explored = []
            q.append(initial)

            while q:

                s_state = q.popleft()

                if s_state.goal_state():
                    return s_state

                is_explored.append(s_state)
                children = next(s_state)

                for child in children:

                    if (child not in is_explored) and (child not in q):
                        q.append(child)
            return None

        def find_moves(result):

            path = []
            final_path = []
            result_parent = result.parent
            count = 0

            while result_parent:

                move = (abs(result.left_miss - result_parent.left_miss),
                        abs(result.left_cann - result_parent.left_cann))

                if(result.boat_position == 'right'):
                    sign = '+'
                    boat_on_left = 0
                    boat_on_right = 1

                else:
                    sign = '-'
                    boat_on_right = 0
                    boat_on_left = 1

                right_side = (result.left_miss, result.left_cann, boat_on_left)
                left_side = (result.right_miss, result.right_cann, boat_on_right)
                action = (abs(result.left_miss - result_parent.left_miss),
                        abs(result.left_cann - result_parent.left_cann))

                print('--- ---')
                print('action {}{}'.format(sign, action))
                print('depth: {}'.format(count))
                print('left side {}'.format(left_side))
                print('right side {}'.format(right_side))
                print()
                print()
                        
                path.append(move)
                result = result_parent
                result_parent = result.parent
                count = count + 1

            for i in range(len(path)):

                final_result = path[len(path) - 1 - i]
                final_path.append(final_result)
            return final_path

        solution = bfs()

        if solution:
            
            return find_moves(solution)
        else:
            return []

def test():
    
    test_agent = BFS()

    test_agent.solve(3, 3)

if __name__ == "__main__":
    test()