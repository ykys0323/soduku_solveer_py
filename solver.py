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
        # print(np.array(t_three_x_three))
        return np.array(t_three_x_three)

    # Return remaining missing number
    def check_row(self,row,get_all=None):
        arr = np.arange(1,10)
        result = np.in1d(arr,row)
        index = np.where(~result)[0]+1
        index_zero = np.where(row == 0)[0]
        if get_all:
            if len(index) > 0:
                return True,index,None
            else:
                return False,None,None
        if len(index_zero) == 1:
            return True,index[0],index_zero[0]
        return False,None,None
    

    def update_sudoku(self,pattern,num,row_id,col_id):
        self.update_count +=1 
        # print(f"Pattern What {pattern} with count {self.update_count}")
        if pattern == 1:
            self.copy_sudoku[row_id][col_id] = num
            self.transpose_sudoku[col_id][row_id] = num
            self.three_x_three_sudoku[col_id//3 + row_id//3 *3][row_id%3 * 3 + col_id % 3] = num
            # print(f"Written index {row_id},{col_id}")
        elif pattern == 2:
            self.transpose_sudoku[row_id][col_id] = num
            self.copy_sudoku[col_id][row_id] = num
            self.three_x_three_sudoku[row_id//3 + col_id//3 *3][col_id%3 * 3 + row_id % 3] = num
            # print(f"Written index {col_id},{row_id}")
        elif pattern == 3:
            self.three_x_three_sudoku[row_id][col_id] = num
            self.copy_sudoku[row_id//3 * 3 + col_id // 3][row_id%3 *3 + col_id %3] = num
            self.transpose_sudoku[row_id%3 *3 + col_id %3][row_id//3 * 3 + col_id // 3] = num
        # print("#######")
        # print(self.copy_sudoku,"\n\n",self.transpose_sudoku,"\n\n",self.three_x_three_sudoku)
        # print("#######")
        # print()
        # user_input = input("wait for you")

    def check_missing_one(self):
        for row_index,row in enumerate(self.copy_sudoku):
            check_true,remaing_num,index = self.check_row(row)
            if check_true:
                self.update_sudoku(1,remaing_num,row_index,index)
        for row_index,row in enumerate(self.transpose_sudoku):
            check_true,remaing_num,index = self.check_row(row)
            if check_true:
                self.update_sudoku(2,remaing_num,row_index,index)
        for row_index,row in enumerate(self.three_x_three_sudoku):
            check_true,remaing_num,index = self.check_row(row)
            if check_true:
                self.update_sudoku(3,remaing_num,row_index,index)

    def check_repeating(self):
        pass

    def find_possible_for_index(self,row_id,col_id):
        check_normal,normal_available,_ = self.check_row(self.copy_sudoku[row_id],True)
        check_transpose,transpose_available,_ = self.check_row(self.transpose_sudoku[col_id],True)
        check_three_x_three,three_x_three_available,_ = self.check_row(self.three_x_three_sudoku[col_id//3 + row_id//3 *3],True)
        
        if check_normal and check_transpose and check_three_x_three:
            common_index = np.intersect1d(normal_available,np.intersect1d(transpose_available,three_x_three_available))
            # print("*****************")
            # print(row_id,col_id)
            # print(normal_available)
            # print(transpose_available)
            # print(three_x_three_available)
            # print("*****************")
            
            return True,common_index
        else:
            return False,None

    def find_possible(self):
        for row_id in range(9):
            for col_id in range(9):
                if self.copy_sudoku[row_id][col_id] != 0:
                    continue
                check_true,normal_possible = self.find_possible_for_index(row_id,col_id)
                if check_true:
                    if len(normal_possible) == 1:
                        # print(normal_possible)
                        self.update_sudoku(1,normal_possible[0],row_id,col_id)
                        
                else:
                    continue
    def solve(self) -> np.ndarray:
        start_time = time.time()
        count_try = 0
        while not self.done_solve:
            self.check_missing_one()
            self.find_possible()
            if not np.any(self.copy_sudoku == 0):
                self.done_solve = True
                self.result = self.copy_sudoku
                print(f"Fill total {self.update_count}")
            count_try += 1
            if count_try == 10:
                print("Break due to out of search")
                break
            
            # user_input = input("wait for you")

        end_time = time.time()
        print(f"Time taken to solve {end_time - start_time}")
        return self.result

sudoku = np.array([[0,0,8,7,0,2,0,0,5],
                   [0,9,0,4,0,6,1,0,0],
                   [5,1,4,3,9,8,0,2,0],
                   [0,0,1,6,3,0,8,7,0],
                   [6,0,5,9,0,0,2,3,1],
                   [8,0,9,1,0,7,5,4,0],
                   [2,0,6,0,0,3,9,0,4],
                   [0,5,3,2,4,0,7,6,0],
                   [1,0,7,8,0,0,3,0,2]])

if __name__ == '__main__':
    sudoku_solver = SudokuSolver(sudoku)
    print(sudoku_solver.solve())



    


"""
1 5
1 3 4 6 9
1 2 5 6 7 8 

2 3 6
2 3 4 7
2 3 4 6 7

"""
