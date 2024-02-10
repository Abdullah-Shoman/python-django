import random
def rand_int(min = 0,max =100):
    if not max == 100 and  min == 0:
        print("Max num is provided");
        num = random.random()* max;
    elif not min == 0 and max == 100:
        print("Min num is provided")
        num = random.random()* (100-min) + min;
    else:
        print("no number is provided or both are provided");
        num = random.random()* max + min;
    return round(num);
# Ask about the Bouns 
print(rand_int());
print(rand_int(min=50));
print(rand_int(max=500));
print(rand_int(min = 1000 , max = 5000));