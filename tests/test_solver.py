import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solver import SudokuSolver
import numpy as np
import pytest
def test_flash():
    sudoku = np.array([[0,0,8,7,0,2,0,0,5],
                       [0,9,0,4,0,6,1,0,0],
                       [5,1,4,3,9,8,0,2,0],
                       [0,0,1,6,3,0,8,7,0],
                       [6,0,5,9,0,0,2,3,1],
                       [8,0,9,1,0,7,5,4,0],
                       [2,0,6,0,0,3,9,0,4],
                       [0,5,3,2,4,0,7,6,0],
                       [1,0,7,8,0,0,3,0,2]])
    sudoku_solver = SudokuSolver(sudoku)
    result = np.array([[3,6,8,7,1,2,4,9,5],
                       [7,9,2,4,5,6,1,8,3],
                       [5,1,4,3,9,8,6,2,7],
                       [4,2,1,6,3,5,8,7,9],
                       [6,7,5,9,8,4,2,3,1],
                       [8,3,9,1,2,7,5,4,6],
                       [2,8,6,5,7,3,9,1,4],
                       [9,5,3,2,4,1,7,6,8],
                       [1,4,7,8,6,9,3,5,2]])
    assert np.array_equal(result,sudoku_solver.solve())


def test_easy():
    sudoku = np.array([[5,9,0,4,0,0,2,3,0],
                       [8,0,2,0,0,0,6,0,1],
                       [1,7,0,0,0,9,0,0,0],
                       [6,1,0,0,2,0,0,0,0],
                       [0,8,0,7,1,3,4,0,0],
                       [3,2,0,8,9,0,0,0,5],
                       [7,0,0,0,4,0,5,6,0],
                       [0,5,8,6,0,2,1,0,0],
                       [0,0,0,9,0,7,3,4,0]])
    sudoku_solver = SudokuSolver(sudoku)
    result = np.array([[5,9,6,4,8,1,2,3,7],
                       [8,4,2,3,7,5,6,9,1],
                       [1,7,3,2,6,9,8,5,4],
                       [6,1,7,5,2,4,9,8,3],
                       [9,8,5,7,1,3,4,2,6],
                       [3,2,4,8,9,6,7,1,5],
                       [7,3,9,1,4,8,5,6,2],
                       [4,5,8,6,3,2,1,7,9],
                       [2,6,1,9,5,7,3,4,8]])
    assert np.array_equal(result,sudoku_solver.solve())

def test_medium():
    sudoku = np.array([[0,0,0,0,0,0,0,0,0],
                       [9,0,1,2,6,0,3,0,0],
                       [0,0,0,0,3,0,0,0,0],
                       [0,5,0,0,0,0,0,0,0],
                       [0,0,0,0,0,4,0,0,8],
                       [0,0,9,5,7,8,2,1,0],
                       [0,2,8,1,0,0,0,4,0],
                       [5,7,0,8,0,2,1,3,6],
                       [0,0,0,7,4,6,0,8,0]])
    sudoku_solver = SudokuSolver(sudoku)
    result = np.array([[2,3,5,4,8,7,6,9,1],
                       [9,8,1,2,6,5,3,7,4],
                       [7,4,6,9,3,1,8,2,5],
                       [8,5,2,3,1,9,4,6,7],
                       [3,1,7,6,2,4,9,5,8],
                       [4,6,9,5,7,8,2,1,3],
                       [6,2,8,1,5,3,7,4,9],
                       [5,7,4,8,9,2,1,3,6],
                       [1,9,3,7,4,6,5,8,2]])
    assert np.array_equal(result,sudoku_solver.solve())

def test_hard():
    sudoku = np.array([[0,0,0,0,0,0,3,0,5],
                       [0,9,8,0,0,0,4,0,0],
                       [7,0,0,0,0,0,8,0,0],
                       [0,7,0,3,0,0,5,1,8],
                       [0,6,0,0,9,4,0,0,0],
                       [3,0,2,0,8,0,6,0,9],
                       [0,0,3,2,5,0,0,0,0],
                       [9,0,4,6,0,0,0,0,0],
                       [6,0,0,0,0,0,0,0,0]])
    sudoku_solver = SudokuSolver(sudoku)
    result = np.array([[2,4,6,9,1,8,3,7,5],
                       [5,9,8,7,3,6,4,2,1],
                       [7,3,1,4,2,5,8,9,6],
                       [4,7,9,3,6,2,5,1,8],
                       [8,6,5,1,9,4,2,3,7],
                       [3,1,2,5,8,7,6,4,9],
                       [1,8,3,2,5,9,7,6,4],
                       [9,5,4,6,7,3,1,8,2],
                       [6,2,7,8,4,1,9,5,3]])
    assert np.array_equal(result,sudoku_solver.solve())

def test_expert():
    sudoku = np.array([[0,6,3,5,0,9,2,0,0],
                       [7,0,0,0,0,0,9,0,0],
                       [0,0,0,0,0,7,0,6,0],
                       [1,3,0,0,0,0,6,2,0],
                       [5,7,0,0,0,0,1,0,9],
                       [0,0,2,0,0,0,0,0,0],
                       [0,0,1,0,0,0,0,0,0],
                       [0,4,0,0,0,5,0,0,3],
                       [0,0,0,2,0,0,0,7,0]])
    sudoku_solver = SudokuSolver(sudoku)
    result = np.array([[8,6,3,5,1,9,2,4,7],
                       [7,1,4,6,3,2,9,5,8],
                       [9,2,5,4,8,7,3,6,1],
                       [1,3,9,7,5,8,6,2,4],
                       [5,7,6,3,2,4,1,8,9],
                       [4,8,2,1,9,6,7,3,5],
                       [6,5,1,8,7,3,4,9,2],
                       [2,4,7,9,6,5,8,1,3],
                       [3,9,8,2,4,1,5,7,6]])
    assert np.array_equal(result,sudoku_solver.solve())

def test_not_able_solve():
    sudoku = np.array([[4,6,3,5,0,9,2,0,0],
                       [7,0,0,0,0,0,9,0,0],
                       [0,0,0,0,0,7,0,6,0],
                       [1,3,0,0,0,0,6,2,0],
                       [5,7,0,0,0,0,1,0,9],
                       [0,0,2,0,0,0,0,0,0],
                       [0,0,1,0,0,0,0,0,0],
                       [0,4,0,0,0,5,0,0,3],
                       [0,0,0,2,0,0,0,7,0]])
    sudoku_solver = SudokuSolver(sudoku)
    assert (sudoku_solver.solve() == None)

def test_repeated_but_solved():
    sudoku = np.array([[4,0,0,0,0,0,0,0,0],
                       [0,4,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0]])
    sudoku_solver = SudokuSolver(sudoku)
    assert (sudoku_solver.solve() == None)