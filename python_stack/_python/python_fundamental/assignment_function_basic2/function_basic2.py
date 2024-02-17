# Task 1
def count_down(num):
    list = [];
    for count in range(num,-1,-1):
        list.append(count);
    return list;
print(count_down(5));
# Task 2
def print_and_return(list):
    print(list[0])
    return list[1];
print(print_and_return([1,2]));
# Task 3
def first_plus_length(list):
    return list[0]+len(list);
print(first_plus_length([1,2,3,4,5]));
# Task 4 ask here which list shoud i check the length the orginal or the new lest
def values_greater_than_second(list):
    count_num = 0;
    new_list = [];
    for val in list:
        if len(list) < 2:
            return False;
        if  val > list[1]:
            count_num=+1;
            new_list.append(val);
    return print_result(count_num,new_list);
def print_result(count_num,list):
    if len(list) < 2 :
        return False;
    else:
        print(len(list));
        return list;
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([5]))
# Task 5 
def length_and_value(size,value):
    list = [];
    for counter in range(size):
        list.append(value);
    return list;

print(length_and_value(4,7))
print(length_and_value(6,2))
