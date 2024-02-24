
class Animal:
    def __init__(self,name,age,health_rate,happiness_level):
        self.name = name
        self.age = age
        self.heath_rate = health_rate
        self.happiness_leve = happiness_level

    # display animal info 
    def display_info(self):
        return "Name:",self.name,"Health_rate:"+str(self.heath_rate)+"%, Happinnes_level:"+str(self.happiness_leve)+"%"
        
    def feed(self):
        self.heath_rate+=10
        self.happiness_leve+=10
    
    def get_animal_name(self):
        return self.name

class Lion(Animal):
    # claws_status = have to two optiones cuted or uncut 
    def __init__(self, name, age, health_rate, happiness_level,claws_status):
        super().__init__(name, age, health_rate, happiness_level)
        self.clasw_status = claws_status

    def display_info(self):
        info = super().display_info()
        print(info,"claws_status:",self.clasw_status)
    
    def get_animal_name(self):
        return self.name



class Tigers(Animal):
    def __init__(self, name, age, health_rate, happiness_level,color):
        super().__init__(name, age, health_rate, happiness_level)
        self.color = color
    
    def display_info(self):
        info = super().display_info()
        print(info,"Color:",self.color)
    
    def get_animal_name(self):
        return self.name


class Bear(Animal):
    def __init__(self, name, age, health_rate, happiness_level,hight,weight):
        super().__init__(name, age, health_rate, happiness_level)
        self.hight = hight
        self.weight = weight
    
    def display_info(self):
        info = super().display_info()
        print(info,"Hight:",self.hight,"Wight:",self.weight)
    
    def get_animal_name(self):
        return self.name

class Zoo:
    
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    
    def append_animals(self,animal):
        self.animals.append(animal);

    def display_zoo_animals(self):
        names = ""
        for animal in self.animals:
            names = names+ str(animal.name)+ ","

        return names
    

tiger = Tigers("Shere Khan",10,75,90,'black')
tiger.feed()
# tiger.display_info()

lion = Lion("Simba",5,90,88,'cutted')

# lion.display_info()

bear = Bear("Lili",8,98,99,180,95)

# bear.display_info()

my_zoo = Zoo("Don Litto's jungle")

my_zoo.append_animals(tiger)
my_zoo.append_animals(lion)
my_zoo.append_animals(bear)

print(my_zoo.display_zoo_animals())





