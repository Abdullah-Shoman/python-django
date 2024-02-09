#task 1: print all integers from 0-150
for count in range(151):
    break
    print(count);
# task 2
for count in range(5,1000):
    if count % 5 == 0 :
        print(count)
#task 3 Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
count = 1;
while count < 101:
    if count % 5 ==0 :
        print("Coding")
    if count % 10 == 0 :
        print("Coding Dojo");
    count+=1;
# task 4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0;
for count in range (500000):
    if count % 2 != 0:
        sum+=count;
print(sum);
#taks 5 Print positive numbers starting at 2018, counting down by fours
count = 2018;
while count >0:
    print(count);
    count-=4;
# Flexible Counter lowNum, highNum, mult. S
low_num = 2;
high_num = 10;
mult = 3;
for count in range(low_num,high_num):
    if count % mult == 0:
        print(count);