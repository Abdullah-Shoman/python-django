
# Task 1
def biggie_size(my_list):
    for counter in range (len(my_list)):
        if my_list[counter] > 0:
            my_list[counter] = "big"
    return my_list;
print(biggie_size([-1,2,4,-2]));

# Task 5
def length(my_list):
    if not my_list:
        return 0;
    counter = 0;
    for value in my_list:
        counter+=1;
    return counter;

print(length([1,2,3,4]))
# Task 2

def count_positives(my_list):
    count_positiv_num =0;
    for value in my_list:
        if value > 0:
            count_positiv_num+=1;
    my_list[length(my_list)-1] = count_positiv_num;
    return my_list;
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]));

# Task 3

def sum_total(my_list):
    sum =0;
    for value in my_list:
        sum+= value;
    return sum;
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

# Task 4

def average(my_list):
    return (sum_total(my_list)/length(my_list));

print(average([1,2,3,4]));

# Task 6

def min_num(my_list):
    min = my_list[0];
    for counter in range (length(my_list)):
        if my_list[counter] < min:
            min = my_list[counter];
    return min;
print(min_num([1,2,3,4,5]));
# Task 7
def max_num(my_list):
    max = my_list[0];
    for counter in range (length(my_list)):
        if my_list[counter] > max:
            max = my_list[counter];
    return max;

print(max_num([1,2,3,4,5]));

# Task 8
def ultimate_analysis(my_list):
    dict = {'sumTotal':sum_total(my_list),
            'average':average(my_list),
            'minimum':min(my_list),
            'maximum':max(my_list),
            'length':length(my_list)};
    return dict;

print(ultimate_analysis([1,2,3,4]))
# Task 9
def reverse(my_list):
    size = length(my_list) - 1;
    counter = 0;
    while  size > 0 and counter < size:
        my_list[counter] , my_list[size] = my_list[size],my_list[counter];
        size-=1;
        counter+=1;
    
    return my_list;

print(reverse([1,2,3,4,5,6,7,8,9,10]))
