list1 = [1, 2, 3, 4]
# swap the values first to last and last to first
length = len(list1)
tem = list1[-1]
list1[-1] = list1[0]
list1[0] = tem
print(list1)
