

x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15;
print(x);
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = "Andres"
print(sports_directory)
# Change the value 20 in z to 30
z[0]['y'] = 30;
print(z)

# Task 2

def iteration_dictionary(some_list):
    # print items in the dict inside the list
    for value in some_list:
        print("first_name  - ",value['first_name']+",","last_name - ",value['last_name'])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iteration_dictionary(students)

# #Task 3 
def iteration_dictionary2(key_name,some_list):
    for value in some_list:
        print(value[key_name])

iteration_dictionary2('first_name',students)
iteration_dictionary2('last_name',students)

#Task 4
def printInfo(some_dict):
    for value in some_dict:
        print(len(some_dict[value]),value)
        for items in some_dict[value]:
            print(items)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

