#!/bin/python3

import math
import os
import random
import re
import sys

def findDestn(matrix, n, m):
	for ind1 in range(n):
		for ind2 in range(m):
			if(matrix[ind1][ind2] == "*"):
				return [ind1, ind2]

def findStart(matrix, n, m):
	for ind1 in range(n):
		for ind2 in range(m):
			if(matrix[ind1][ind2] == "M"):
				return [ind1, ind2]


def generatePath(matrix, point, final, k, prev, n, m):
	nextPs = []
	# print(point)
	res = 0
	if(point[0] == final[0] and point[1] == final[1]):
		return k
	if(point[0] + 1 != n and matrix[point[0] + 1][point[1]] != "X" and not(point[0] + 1 == prev[0] and point[1] == prev[1])):
		nextPs.append([point[0] + 1, point[1]])
	if(point[0] - 1 != -1 and matrix[point[0] - 1][point[1]] != "X" and not(point[0] - 1 == prev[0] and point[1] == prev[1])):
		nextPs.append([point[0] - 1, point[1]])
	if(point[1] + 1 != m and matrix[point[0]][point[1] + 1] != "X" and not(point[0] == prev[0] and point[1] + 1 == prev[1])):
		nextPs.append([point[0], point[1] + 1])
	if(point[1] - 1 != -1 and matrix[point[0]][point[1] - 1] != "X" and not(point[0] == prev[0] and point[1] - 1 == prev[1])):
		nextPs.append([point[0], point[1] - 1])
	# print(nextPs)
	if(len(nextPs) > 1):
		k += 1
	for ps in nextPs:
		res = generatePath(matrix, ps, final, k, point, n, m)
		if(res != -1):
			return res
	return -1


def countLuck(matrix, k, n, m):
	
	start = findStart(matrix, n, m)
	destn = findDestn(matrix, n, m)
	res = generatePath(matrix, start, destn, 0, [-1, -1], n, m)

	if(res == k):
		return "Impressed"
	else:
		return "Oops!"



if __name__ == '__main__':
	t = int(input())

	for t_itr in range(t):
		nm = input().split()

		n = int(nm[0])

		m = int(nm[1])

		matrix = []

		for _ in range(n):
			matrix_item = input()
			matrix.append(matrix_item)

		k = int(input())

		result = countLuck(matrix, k, n, m)

		print(result)
