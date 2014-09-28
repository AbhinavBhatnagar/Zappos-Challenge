import sys
import json

def subset_sum(wanted_amount, check_list, total_price, partial=[]):
   # print check_list[0].split("$")[1]
    target = total_price
    range1=target-10
    range2=target+10
    partial_price = [int(float(partial[i].split("$")[1])) for i in range(len(partial))] 
    s = sum(partial_price)
   # print partial_price
   # print s
    if (s > range1) and (s < range2): 
	if len(partial)==wanted_amount:
	        print "possible combinations(%s)" % (partial)
    if s >= range2:
        return 
    for i in range(len(check_list)):
	n=int(float(check_list[i].split("$")[1]))
       # n = numbers[i]
        remaining = check_list[i+1:]
        subset_sum(wanted_amount, remaining, target, partial + [check_list[i]]) 

if __name__ == '__main__':
	subset_sum(wanted_amount, numbers, target, partial=[])
