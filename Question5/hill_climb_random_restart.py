import random
import math

class board_st:
#   global for value of h
    global h_state

#   constructor
    def __init__(self, cap, info=None):
        self.cap = cap
        self.info = info
        self.h_val = -1   
    
#   initial config of the board
    def gen_int_conf(self):
        b_state=[]
        for i in range(int(self.cap)):
            column_val=[None]*int(self.cap)
            random_value = random.randint(0,int(self.cap)-1)
            for j in range(int(self.cap)):
                if j == random_value:
                    column_val[j]='Q'
                else:
                    column_val[j]='_'
            b_state.append(column_val)
        self.info = b_state
        
        return self.info
    
#   function to move the queen to a new location.
    def gen_next_b(self, prev_pos, curr_pos):
        x_pos = curr_pos[0]
        y_pos = curr_pos[1]
        
        pre_x = prev_pos[0]
        pre_y = prev_pos[1]
        
        nxt_pos = self.replicate(self.info)
        
        for i in range(0, len(nxt_pos)):
            for j in range(0, len(nxt_pos)):
                if i==x_pos and j==y_pos:
                    nxt_pos[i][j]='Q'

                if i==pre_x and j==pre_y:
                    nxt_pos[i][j]='_'
        return nxt_pos
    
#   helper to to create a successor board.
    def replicate(self,old):
        new_board=[]
        
        for i in old:
            sqs=[]
            for j in i:
                sqs.append(j)
            new_board.append(sqs)
        return new_board
        
#   heuristic val calculator  
    def get_h_value(self):
        c=0
                    
        for i in range(len(self.info)):
            for j in range(len(self.info)):
                if self.info[i][j]=='Q':
                    location = [None]*2
                    location[0] = i
                    location[1] = j
                    v,d = self.getAttPosition(location)

                    for k in range(len(self.info)):
                        for l in range(len(self.info)):
                                if self.info[k][l]=='Q':
                                    for e in v:
                                        if e[0] == k and e[1] == l:
                                            c+=1
                                    for e in d:
                                        if e[0] == k and e[1] == l:
                                            c+=1
        return math.ceil(c/2)
        
#   helper to calculate the attack positions     
    def getAttPosition(self,position): 
        vertical_position = []                           
        x_value=position[0]
        y_value=position[1]
        
        if x_value==0:
            while(x_value < len(self.info)-1):
                attack_vertical=[None]*2
                x_value+=1

                attack_vertical[0]=x_value
                attack_vertical[1]=y_value
                vertical_position.append(attack_vertical)
        
        elif x_value==len(self.info):
            while(x_value>=0):
                attack_vertical=[None]*2
                x_value-=1

                attack_vertical[0]=x_value
                attack_vertical[1]=y_value
                vertical_position.append(attack_vertical)
        
        else:
            while(x_value < len(self.info)-1):
                attack_vertical=[None]*2
                x_value+=1

                attack_vertical[0]=x_value
                attack_vertical[1]=y_value
                vertical_position.append(attack_vertical)
                
            x_value=position[0]
            y_value=position[1]
                
            while(x_value>=0):
                attack_vertical=[None]*2
                x_value-=1

                attack_vertical[0]=x_value
                attack_vertical[1]=y_value
                vertical_position.append(attack_vertical)
                
        diagonal_list = []                         
        x_value=position[0]
        y_value=position[1]  
        
        while x_value>0 and x_value<len(self.info) and y_value>0 and y_value<len(self.info):
            attack_diagonal=[None]*2
            x_value-=1
            y_value-=1

            attack_diagonal[0]=x_value
            attack_diagonal[1]=y_value
            diagonal_list.append(attack_diagonal)
            
        x_value=position[0]
        y_value=position[1]    
        
        while x_value>=0 and x_value<len(self.info)-1 and y_value>0 and y_value<len(self.info):
            attack_diagonal=[None]*2
            x_value+=1
            y_value-=1

            attack_diagonal[0]=x_value
            attack_diagonal[1]=y_value
            diagonal_list.append(attack_diagonal)
            
        x_value=position[0]
        y_value=position[1]
        
        while x_value>0 and x_value<len(self.info) and y_value>=0 and y_value<len(self.info)-1:
            attack_diagonal=[None]*2
            x_value-=1
            y_value+=1

            attack_diagonal[0]=x_value
            attack_diagonal[1]=y_value
            diagonal_list.append(attack_diagonal)
        
        x_value=position[0]
        y_value=position[1]
        
        while x_value>=0 and x_value<len(self.info)-1 and y_value>=0 and y_value<len(self.info)-1:
            attack_diagonal=[None]*2
            x_value+=1
            y_value+=1

            attack_diagonal[0]=x_value
            attack_diagonal[1]=y_value
            diagonal_list.append(attack_diagonal) 
        
        return vertical_position, diagonal_list
    
class board:

    global number_of_queens
    
    def __init__(self):
        self.passing = 0
        self.fail = 0
        self.total_steps = 0
        self.total_pass_steps = 0
        self.total_fail_steps = 0
        self.count_initial_val = 0

    def get_r_position(self,info,row_value):    
        for i in range(len(info)):
            if info[row_value][i] == 'Q':
                location = [None]*2
                location[0]= row_value
                location[1]= i     
                break
        return location
    
#   main 
    def main(self):
        global number_of_queens
        
        
        number_of_queens = 8
    
        number_of_runs = 100

        print("Staring with "+ str(number_of_queens) + " Queens and "+ str(number_of_runs) +" runs")
        
        print()

#       Hill-Climbing search.
        print("Hill-Climbing start ")
        for x in range(int(number_of_runs)):
            self.total_steps = 0
            self.get_curr_board(x)
        print()
        print("-------")
        print("-------")
        print()
        print("Success ---> ", (self.passing / number_of_runs) * 100,"%")
        print("Failure ---> ", (self.fail / number_of_runs) * 100, "%")
        if(self.passing == 0):
            print("No success!!")
        else:
            print("Average steps for passing: ", self.total_pass_steps/self.passing)

        if(self.fail == 0):
            print("No success!!")
        else:
            print("Average steps for failure: ", self.total_fail_steps/self.fail)
        
        print()
        
#       random-restart without sideways move.
        print("Random Restart Hill Climbing")
        self.total_steps = 0
        self.count_initial_val = 0
        for x in range(int(number_of_runs)):
            self.calc_RandomRestart(0)
        print()
        print("Random Restart Hill Climbing with no sideways for " + str(number_of_queens) + " Queens and " + str(number_of_runs) + " runs")
        print("Average random restarts without sideways move ", self.count_initial_val/int(number_of_runs))
        print("Average steps required without sideways move: ", self.total_steps/int(number_of_runs))
        print()

#   Hill-Climbing search.     
    def get_curr_board(self, iteration_number):
        h_state=-1
        
        initial_board = board_st(number_of_queens)
        initial_board.info = initial_board.gen_int_conf()
        initial_board.h_val = initial_board.get_h_value()
        if iteration_number < 4:
            print("Search Number " + str(iteration_number+1))
            print("Original state ")
            for x in initial_board.info:
                for y in x:
                    print(y, end=" ")
                print()
            print("h value:", initial_board.h_val)
            print()

        min_board = initial_board.info
        while h_state !=0:
            min_h_value = []
            previous_board = board_st(number_of_queens, min_board)
            previous_board.h_val = previous_board.get_h_value()
            h_state = previous_board.h_val
            for i in range(int(number_of_queens)):
                location = self.get_r_position(previous_board.info,i)
                for j in range(int(number_of_queens)):
                    next_loc = [None]*2
                    next_loc[0]=i
                    next_loc[1]=j
                    if next_loc == location:
                        continue    

                    next_b = board_st(number_of_queens)
                    next_b.info = previous_board.gen_next_b(location, next_loc)
                    next_b.h_val = next_b.get_h_value()

                    if next_b.h_val <= h_state:
                        h_state = next_b.h_val
                        location_value = next_loc
                        location_value.append(next_b.h_val)
                        min_h_value.append(location_value)
                        
            if min_h_value:            
                l = len(min_h_value)-1
                while l>=0:
                    y = min_h_value[l]
                    if y[2] != h_state:
                        del min_h_value[l]
                    l-=1

                random_value = random.randint(0,len(min_h_value)-1)
                position_d = min_h_value[random_value]
                del position_d[2]
                parent_location = self.get_r_position(previous_board.info,position_d[0])
                min_board = previous_board.gen_next_b(parent_location, position_d)

            if h_state == previous_board.h_val:
                if h_state == 0:
                    if iteration_number < 4:
                        print("Passed")
                    self.passing +=1
                else:
                    self.total_fail_steps +=self.total_steps
                    if iteration_number < 4:
                        for x in min_board:
                            for y in x:
                                print(y, end=" ")

                            print()
                        print("h value: " + str(h_state))
                        print()
                        print("Fail")
                        print()
                    self.fail +=1
                break

            else:
                self.total_steps +=1
                if iteration_number < 4:
                    print("Next state")
                    for x in min_board:
                        for y in x:
                            print(y, end=" ")

                        print()
                    print("h value", h_state)
                    print()

                if h_state==0:
                    self.total_pass_steps += self.total_steps
                    if iteration_number < 4:
                        print("Solution found")
                        print()
                    self.passing += 1

#   Random-restart.
    def calc_RandomRestart(self, side_value):
        number_of_tries = 0
        h_value = -1
        
        while h_value != 0:
            self.count_initial_val +=1
            original_b = board_st(number_of_queens)
            original_b.info = original_b.gen_int_conf()
            original_b.h_val = original_b.get_h_value()
            
            if original_b.h_val == 0:
                self.passing +=1
                break

            board = original_b.info
            while h_value !=0:
                min_h_value = []
                factor_h_value = 0
                old_b = board_st(number_of_queens, board)
                old_b.h_val = old_b.get_h_value()
                h_value = old_b.h_val
                for i in range(int(number_of_queens)):
                    location = self.get_r_position(old_b.info,i)
                    for j in range(int(number_of_queens)):
                        new_pos = [None]*2
                        new_pos[0]=i
                        new_pos[1]=j
                        if new_pos == location:
                            continue    

                        next_b = board_st(number_of_queens)
                        next_b.info = old_b.gen_next_b(location, new_pos)
                        next_b.h_val = next_b.get_h_value()

                        if next_b.h_val <= h_value:
                            if next_b.h_val < h_value:
                                number_of_tries = 0
                            h_value = next_b.h_val
                            store_pos =new_pos                            
                            store_pos.append(next_b.h_val)
                            min_h_value.append(store_pos)
                            factor_h_value = 1     
                
                if h_value == 0 or factor_h_value == 0: 
                    if h_value == 0:
                        self.total_steps+=1
                        self.total_pass_steps += self.total_steps
                        self.passing +=1

                    if factor_h_value == 0:
                        self.total_fail_steps +=self.total_steps
                        self.fail +=1
                    break

                if min_h_value:            
                    l = len(min_h_value)-1
                    while l>=0:
                        y = min_h_value[l]
                        if y[2] != h_value:
                            del min_h_value[l]
                        l-=1
                    rand_value = random.randint(0,len(min_h_value)-1)
                    location_d = min_h_value[rand_value]
                    del location_d[2]
                    parent_location = self.get_r_position(old_b.info,location_d[0])
                    board = old_b.gen_next_b(parent_location, location_d)

                if h_value == old_b.h_val:
                    if side_value == 0:
                        break

                    if side_value == 1:
                        self.total_steps+=1
                        if factor_h_value != 0:
                            number_of_tries +=1
                        if number_of_tries >=100:
                            break
                else:
                    self.total_steps+=1                        


start = board()
start.main()