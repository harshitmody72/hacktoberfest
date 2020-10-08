class Data:
    def __init__(self,**x):
        self.x = x
    def new(self):
        print(self.x)


n = int(input("Enter your no. of detail's what to enter : "))
i = 0
while i < n:
    names = input("Enter your name: ").lower()
    id_num = input("Enter your key: ").lower()
    s = Data(name = names , id = id_num)

    i += 1

s.new()
 

