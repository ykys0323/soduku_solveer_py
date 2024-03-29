import os
import numpy as np
import time


class SudokuSolver():
    def __init__(self, sudoku: np.ndarray) -> None:
        self.ori_sudoku = sudoku
        self.copy_sudoku = sudoku
        self.transpose_sudoku = sudoku.T
        self.three_x_three_sudoku = self.convert_to_three_x_three(sudoku)
        self.result = np.ndarray
        self.done_solve = False
        self.update_count = 0
        self.all_index_possible = []
        self.visited = []
        self.recorded_sudoku = []
        self.layer = 0
        self.out_of_guess = False
        self.possibles = []
        

    #convert three time three array to 1 row
    def convert_to_three_x_three(self,c_sudoku):
        t_three_x_three = []
        for x in range(3):
            for y in range(3):
                t_row = []
                for z in range(3):
                    for w in range(3):
                        t_row.append(c_sudoku[x*3 + z][y*3 + w])
                t_three_x_three.append(t_row)
        return np.array(t_three_x_three)

    # Return remaining missing number
    def check_row(self,row,get_all=None):
        arr = np.arange(1,10)
        result = np.in1d(arr,row)
        index = np.where(~result)[0]+1
        index_zero = np.where(row == 0)[0]
        if len(index) > 0:
            return True,index,None
        return False,None,None

    
    def update_sudoku(self,num,row_id,col_id):
        if self.copy_sudoku[row_id][col_id] != 0:
            print("Wasting power")
        self.update_count +=1 
        self.copy_sudoku[row_id][col_id] = num
        self.transpose_sudoku[col_id][row_id] = num
        self.three_x_three_sudoku[col_id//3 + row_id//3 *3][row_id%3 * 3 + col_id % 3] = num


    def check_impossible_for_row(self,pattern,row_id):
        for i in range(9):
            count = 0
            found_index = -1
            for j in range(9):
                if pattern == 1:
                    if i+1 in self.all_index_possible[row_id][j]:
                        if count == 0:
                            count+=1
                            found_index = j
                        else:
                            count+=1
                elif pattern ==2:
                    if i+1 in self.all_index_possible[j][row_id]:
                        if count == 0:
                            count+=1
                            found_index = j
                        else:
                            count+=1
                else:
                    if i+1 in self.all_index_possible[j//3 + row_id//3 *3][row_id%3 * 3 + j % 3]:
                        if count == 0:
                            count+=1
                            found_index = j
                        else:
                            count+=1
            len_of_index = 0
            if pattern == 1:
                if self.copy_sudoku[row_id][found_index] != 0:
                    continue
                len_of_index = len(self.all_index_possible[row_id][found_index])
            elif pattern == 2:
                if self.copy_sudoku[found_index][row_id] != 0:
                    continue
                len_of_index = len(self.all_index_possible[found_index][row_id])
            else:
                if self.copy_sudoku[found_index//3 + row_id//3 *3][row_id%3 * 3 + found_index % 3] != 0:
                    continue
                len_of_index = len(self.all_index_possible[found_index//3 + row_id//3 *3][row_id%3 * 3 + found_index % 3])
            
            if count == 1 and len_of_index > 1:

                return True,found_index,i+1
        return False,None,None
            
    def find_possible_for_index(self,row_id,col_id):
        check_normal,normal_available,_ = self.check_row(self.copy_sudoku[row_id])
        check_transpose,transpose_available,_ = self.check_row(self.transpose_sudoku[col_id])
        check_three_x_three,three_x_three_available,_ = self.check_row(self.three_x_three_sudoku[col_id//3 + row_id//3 *3])
        if check_normal and check_transpose and check_three_x_three:
            common_index = np.intersect1d(normal_available,np.intersect1d(transpose_available,three_x_three_available))
            if len(common_index) == 0:
                print("Equal 0")
            return True,common_index
        else:
            return False,None

    def find_possible(self):
        cant_find_any = True
        self.all_index_possible = []
        for row_id in range(9):
            temp_possible = []
            for col_id in range(9):
                if self.copy_sudoku[row_id][col_id] != 0:
                    temp_possible.append([np.array(self.copy_sudoku[row_id][col_id])])
                    continue
                check_true,normal_possible = self.find_possible_for_index(row_id,col_id)
                if check_true:
                    if len(normal_possible) == 1:
                        cant_find_any = False
                        self.update_sudoku(normal_possible[0],row_id,col_id)
                temp_possible.append(normal_possible)

            self.all_index_possible.append(temp_possible)
        return cant_find_any
    
    def find_another_possible(self):
        cant_find_any = True
        for row_id in range(9):
            check_possible,col_id,num_value = self.check_impossible_for_row(1,row_id)
            if check_possible:
                cant_find_any = False
                self.update_sudoku(num_value,row_id,col_id)
            check_possible,col_id,num_value = self.check_impossible_for_row(2,row_id)
            if check_possible:
                cant_find_any = False
                self.update_sudoku(num_value,col_id,row_id)
            check_possible,col_id,num_value = self.check_impossible_for_row(3,row_id)
            if check_possible:
                cant_find_any = False
                self.update_sudoku(num_value, row_id//3 *3 + col_id//3,col_id%3 + row_id%3 *3)
        return cant_find_any
    
    def check_possible(self):
        # print("################")
        self.new_able_index = []
        for row_id in range(9):
            for col_id in range(9):
                if self.copy_sudoku[row_id][col_id] != 0:
                    continue
                check_normal,normal_available,_ = self.check_row(self.copy_sudoku[row_id])
                check_transpose,transpose_available,_ = self.check_row(self.transpose_sudoku[col_id])
                check_three_x_three,three_x_three_available,_ = self.check_row(self.three_x_three_sudoku[col_id//3 + row_id//3 *3])
                # print(f"{row_id},{col_id} {check_normal} {check_transpose} {check_three_x_three}")
                if check_normal and check_transpose and check_three_x_three:
                    common_index = np.intersect1d(normal_available,np.intersect1d(transpose_available,three_x_three_available))
                    if len(common_index) == 0:
                        return False
                    self.new_able_index.append((common_index,(row_id,col_id)))
                    
                    # return True,common_index
                    # print(f"{row_id},{col_id} {common_index} {normal_available} {transpose_available} {three_x_three_available}")
        return True
        # print("################")
    def get_next_possible(self):
        if self.layer == 0:
            return False,None
        for possible in self.possibles[self.layer-1]:
            if possible in self.visited[self.layer-1]:
                continue
            else:
                return True,possible
        return False,None
    
    def revert_previous_sudoko(self):
        self.replace_sudoku(self.recorded_sudoku[self.layer-1])
    
    def update_next_visiting(self,next_visiting):
        self.update_sudoku(next_visiting%10,next_visiting//100,next_visiting//10%10)
        self.visited[self.layer-1].append(next_visiting)
    def convert_possible_format(self):
        sorted_array = sorted(self.new_able_index,key=lambda x:len(x[0]))
        new_possbiles = []
        for arr in sorted_array:
            for possible_number in arr[0]:
                new_possbiles.append(arr[1][0]*100+arr[1][1]*10+possible_number)
        self.possibles.append(new_possbiles)
        # for possible in self.new_able_index:
    def remove_last_index(self):
        self.possibles = self.possibles[:-1]
        self.recorded_sudoku = self.recorded_sudoku[:-1]
        self.visited = self.visited[:-1]

    def start_guessing(self):
        still_possible = self.check_possible()
        if self.out_of_guess:
            return
        if still_possible:
            self.layer +=1
            self.visited.append([])
            self.backup_sudoku()
            self.convert_possible_format()
            _ , next_visiting = self.get_next_possible()
            self.update_next_visiting(next_visiting)
        else:
            check_possible_guess, next_visiting = self.get_next_possible()
            if check_possible_guess:
                self.revert_previous_sudoko()
                self.update_next_visiting(next_visiting)
            else:
                if self.layer > 0:
                    self.remove_last_index()
                    # self.revert_previous_sudoko()
                self.layer-=1

        if self.layer >= 0:
            self.out_of_guess = True



    def replace_sudoku(self,previous_sudoku):
        self.copy_sudoku = previous_sudoku
        self.transpose_sudoku = previous_sudoku.T
        self.three_x_three_sudoku = self.convert_to_three_x_three(previous_sudoku)

    def backup_sudoku(self):
        self.recorded_sudoku.append(self.copy_sudoku)

    def solve(self) -> np.ndarray:
        start_time = time.time()
        count_try = 0
        while not self.done_solve:
            second_not_possible = False
            not_possible = self.find_possible()
            if not np.any(self.copy_sudoku == 0):
                self.done_solve = True
                self.result = self.copy_sudoku
                print(f"Fill total {self.update_count}")
            if not_possible:
                second_not_possible = self.find_another_possible()
                # print("######")

            if not_possible and second_not_possible:
                # print(f"Not any possible starting {count_try}")
                self.start_guessing()
            count_try += 1
            if count_try == 81:
                print("Break due to out of search")
                print(self.copy_sudoku)
                # print(self.all_index_possible)
                break

        end_time = time.time()
        print(f"Time taken to solve {end_time - start_time}")
        return self.result

sudoku = np.array( [[0,0,0,8,0,3,0,0,0],
                    [0,0,9,0,4,0,2,0,0],
                    [0,5,0,0,0,0,0,4,0],
                    [0,9,0,0,0,0,4,0,0],
                    [0,4,0,0,2,1,0,0,8],
                    [1,0,6,0,0,8,0,0,0],
                    [6,0,0,1,0,0,0,8,5],
                    [0,0,0,0,0,0,0,0,0],
                    [0,2,0,0,3,6,0,0,0]])

if __name__ == '__main__':
    sudoku_solver = SudokuSolver(sudoku)
    print(sudoku_solver.solve())

