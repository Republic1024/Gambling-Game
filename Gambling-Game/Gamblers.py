from random import choice

class Gamblers:
    def __init__(self,number = 100,money = 100):
        self.number = number
        self.money = money
        self.money_infros = []
        for m in range(0,self.number):
            self.money_infros.append(self.money)

    def start_Gambling(self):

        self.direction = choice([1,-1])
        #self.change *= self.direction
        self.change = choice([x for x in range(int(self.money*0.1),int(self.money*0.5))])
        x = 0
        y = 0
        while x==y:  

            x = choice([s for s in range(0,self.number)])
            y = choice([s for s in range(0,self.number)])
        
        #while self.money_infros[x] < self.change or self.money_infros[y] < self.change:
        #   self.change = choice([x for x in range(int(self.money*0.1),int(self.money*0.5))])

        self.money_infros[x] += self.change*1
        self.money_infros[y] -= self.change*1
        
        return self.money_infros
        







