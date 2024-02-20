

class math_dojo:
    
    def __init__(self):
        self.result = 0
    def add(self,num=0,*nums):
        self.result += num
        if nums != []:
            for value in nums:
                self.result +=value
        return self
    
    def subtract(self,num=0,*nums):
        self.result -= num
        if nums != []:
            for value in nums:
                self.result -=value
        return self
    
    def get_result(self):
        return self.result 

md = math_dojo();

test1 = md.add(1,2,3,4,5).subtract(15).get_result()
print(test1)

test2 = md.add(100,300,500,200).subtract(500).get_result()
print(test2)