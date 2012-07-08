#!/usr/bin/env python
#
# Sudoku checker
# Take 9 lists of 9 numbers and check whether or not it is a valid sudoku
# check_sudoku() requires get_sudoku() and can't be guarenteed to work without it, though if you enter a valid sudoku - 9 rows of 9 digits
# between 1 & 9 seperated by spaces, then check_sudoku should work on it's own. Otherwise, both the functions check the sudoku in
# conjunction

def get_sudoku():
	sudoku = []
	print 'Input the sudoku'
	for i in range(9):
		sudoku.append(raw_input().split(' '))
		if len(sudoku[i]) != 9:
			print 'Really? Since when was a sudoku row not 9 numbers?'
			return False
		for n in sudoku[i]:
			if (len(n) !=1) or (not n.isdigit()) or n=='0': # negative entries & entries greater than 9(2 or more digits), not digits or less than 1 are weeded out
				print 'Enter a valid sudoku!'
				return False
	return sudoku

def check_sudoku(sudoku):
	if not sudoku:
		return False
	row=[]
	column=[]
	box=[]
	for i in range(9):
		row.append([])
		column.append([])
		box.append([])
	for r in sudoku:
		i= sudoku.index(r)
		for c in r:
			j= r.index(c)
			if c in row[i] or c in column[j] or c in box[(i/3)*3+j/3]:
				return False
			else:
				row[i].append(c)
				column[j].append(c)
				box[(i/3)*3+j/3].append(c)
	return True

if __name__=='__main__':
	s = get_sudoku()
	print check_sudoku(s)	
