import random
import math

class st:
    global h_state
    
    def __init__(self, cap, info=None):
        self.cap = cap
        self.info = info
        self.hur_value = -1                                            

    def gen_int_conf(self):
        board_s=[]
        for i in range(int(self.cap)):
            column_val=[None]*int(self.cap)
            random_value = random.randint(0,int(self.cap)-1)
            for j in range(int(self.cap)):
                if j == random_value:
                    column_val[j]='Q'
                else:
                    column_val[j]='_'
            board_s.append(column_val)
        self.info = board_s
        
        return self.info

    def generate_next(self, prev_pos, curr_pos):
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
    
    def replicate(self,old):
        new_board=[]
        
        for i in old:
            sqs=[]
            for j in i:
                sqs.append(j)
            new_board.append(sqs)
        return new_board
        
#   function to calculate the h value of a board.    
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
        self.steps = 0
        self.total_pass_steps = 0
        self.total_fail_steps = 0
        self.initial_c = 0

    def get_r_position(self,info,row_value):    
        for j in range(len(info)):
            if info[row_value][j] == 'Q':
                location = [None]*2
                location[0]= row_value
                location[1]= j     
                break
        return location
    
#   main 
    def main(self):
        global number_of_queens

        number_of_queens = 8
    
        number_of_runs = 100
        
        print("Staring with "+ str(number_of_queens) + " Queens and "+ str(number_of_runs) +" runs")

        print()

        print("Hill-Climbing search with sideways move")
        self.passing = 0
        self.fail = 0
        self.steps = 0
        self.total_pass_steps = 0
        self.total_fail_steps = 0
 
        for x in range(int(number_of_runs)):
            self.steps = 0        
            self.sideways_board_initial(x)
        
        print("----")
        print("----")
        print("----")
        print()

        print("Success ---> ", (self.passing / number_of_runs) * 100,"%")
        print("Failure ---> ", (self.fail / number_of_runs) * 100, "%")
        if(self.passing == 0):
            print("No success!!")
        else:
            print("Average number of steps for successes: ", self.total_pass_steps/self.passing)

        if(self.fail == 0):
            print("No success!!")
        else:
            print("Average number of steps for failures: ", self.total_fail_steps/self.fail)
        print()
        
        self.steps = 0
        self.initial_c = 0
        for x in range(int(number_of_runs)):
            self.get_RandomRestart(1)

        print("Average random restarts with sideways ", self.initial_c/number_of_runs)
        print("Average steps required with sideways ", self.steps/number_of_runs)

    def sideways_board_initial(self, iteration):
        tries = 0
        heuristic_d=-1
        
        initial_board = st(number_of_queens)
        initial_board.info = initial_board.gen_int_conf()
        initial_board.hur_value = initial_board.get_h_value()
        if iteration < 4:
            print("Search Sequence " + str(iteration+1) + ":")
            print("Initial state:")
            for x in initial_board.info:
                for y in x:
                    print(y, end=" ")
                print()
            print("h value:", initial_board.hur_value)
            print()

        board = initial_board.info
        while heuristic_d !=0:
            min_h_positions = []
            self.steps +=1
            high_count_hur = 0 
            old_board = st(number_of_queens, board)
            old_board.hur_value = old_board.get_h_value()
            heuristic_d = old_board.hur_value
            for i in range(int(number_of_queens)):
                location = self.get_r_position(old_board.info,i)
                for j in range(int(number_of_queens)):
                    new_location = [None]*2
                    new_location[0]=i
                    new_location[1]=j
                    if new_location == location:
                        continue    

                    next_board = st(number_of_queens)
                    next_board.info = old_board.generate_next(location, new_location)
                    next_board.hur_value = next_board.get_h_value()

                    if next_board.hur_value <= heuristic_d:
                        heuristic_d = next_board.hur_value
                        store_location = new_location
                        high_count_hur = 1
                        if next_board.hur_value < heuristic_d:
                            tries = 0
                        store_location.append(next_board.hur_value)
                        min_h_positions.append(store_location)
                        
            if min_h_positions:            
                l = len(min_h_positions)-1
                while l>=0:
                    y = min_h_positions[l]
                    if y[2] != heuristic_d:
                        del min_h_positions[l]
                    l-=1

                random_value = random.randint(0,len(min_h_positions)-1)
                location_dash = min_h_positions[random_value]
                del location_dash[2]
                location_of_parent = self.get_r_position(old_board.info,location_dash[0])
                board = old_board.generate_next(location_of_parent, location_dash)
            
            if heuristic_d == old_board.hur_value:                
                if heuristic_d == 0:
                    if iteration < 4:
                        print("Position")
                        print()
                    self.total_pass_steps += self.steps
                    self.passing +=1                
                else:
                    if high_count_hur != 0:
                        tries +=1
                        if iteration < 4:
                            print("Next")
                            for x in board:
                                for y in x:
                                    print(y, end=" ")

                                print()
                            print("h value:", heuristic_d)
                            print()                        
                    else:
                        self.total_fail_steps += self.steps
                        self.fail +=1
                        if iteration < 4:
                            print("Solution not found.")
                            print()
                        break
                    if tries >=100:
                        self.total_fail_steps +=self.steps
                        self.fail +=1
                
                        if iteration < 4:
                            for x in board:
                                for y in x:
                                    print(y, end=" ")
                                print()
                            print("h value:", heuristic_d)
                            print()
                            
                            print("No Solution 100 sideways move.")
                            print()
                        break
            else:
                if iteration < 4:
                    print("Next ")
                    for x in board:
                        for y in x:
                            print(y, end=" ")

                        print()
                    print("h value:", heuristic_d)
                    print()

                if heuristic_d==0:
                    self.total_pass_steps += self.steps
                    if iteration < 4:
                        print("Solution found.")
                        print()
                    self.passing += 1

#   Random-restart.
    def get_RandomRestart(self, sideway):
        tries=0
        hur_d=-1
        
        while hur_d != 0:
            self.initial_c +=1
            original_board = st(number_of_queens)
            original_board.info = original_board.gen_int_conf()
            original_board.hur_value = original_board.get_h_value()
            
            if original_board.hur_value == 0:
                self.passing +=1
                break

            min_board = original_board.info
            while hur_d !=0:
                min_hur_val = []
                check_hur = 0
                old_board = st(number_of_queens, min_board)
                old_board.hur_value = old_board.get_h_value()
                hur_d = old_board.hur_value
                for i in range(int(number_of_queens)):
                    pos = self.get_r_position(old_board.info,i)
                    for j in range(int(number_of_queens)):
                        new_location = [None]*2
                        new_location[0]=i
                        new_location[1]=j
                        if new_location == pos:
                            continue    

                        next_board = st(number_of_queens)
                        next_board.info = old_board.generate_next(pos, new_location)
                        next_board.hur_value = next_board.get_h_value()

                        if next_board.hur_value <= hur_d:
                            if next_board.hur_value < hur_d:
                                tries = 0
                            hur_d = next_board.hur_value
                            store_pos =new_location                            
                            store_pos.append(next_board.hur_value)
                            min_hur_val.append(store_pos)
                            check_hur = 1     
                
                if hur_d == 0 or check_hur == 0: 
                    if hur_d == 0:
                        self.steps+=1
                        self.total_pass_steps += self.steps
                        self.passing +=1

                    if check_hur == 0:
                        self.total_fail_steps +=self.steps
                        self.fail +=1
                    break

                if min_hur_val:            
                    l = len(min_hur_val)-1
                    while l>=0:
                        y = min_hur_val[l]
                        if y[2] != hur_d:
                            del min_hur_val[l]
                        l-=1
                    rand = random.randint(0,len(min_hur_val)-1)
                    pos_dash = min_hur_val[rand]
                    del pos_dash[2]
                    pos_parent = self.get_r_position(old_board.info,pos_dash[0])
                    min_board = old_board.generate_next(pos_parent, pos_dash)

                if hur_d == old_board.hur_value:
                    if sideway == 0:
                        break

                    if sideway == 1:
                        self.steps+=1
                        if check_hur != 0:
                            tries +=1
                        if tries >=100:
                            break
                else:
                    self.steps+=1                        


start = board()
start.main()