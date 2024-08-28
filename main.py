from methods import *

file = open("inputwitherror.txt", "r")
data = file.read().split()

error = False
next_token = ''
count = 0

while True:
    next_token = data[count]
    G(count, error, next_token)
    count += 1