result = 1
seq = 0
prev = 0
cur_seq = 0
number = int(input())
while number > 0:
    if prev == number:
        cur_seq += 1
    else:
        cur_seq = 1
    if cur_seq != 1 and cur_seq > result:
        result = cur_seq
    prev = number
    number = int(input())

print(result)