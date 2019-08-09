class Piggy_Bank():
    money = 0
    def AddMoney(self):
        print(" ")
        inputAdd = float(input('Add amount : '))
        print(" ")
        self.money = self.money + inputAdd;
        print("After adding , your updated balance is " + str(self.money) + " rupees")
    
    def WithdrawMoney(self):
        amountDrawn = float(input('withdraw amount : '))
        print(" ")
        self.money = self.money - amountDrawn;
        print(" ")
        print("After withdrawing , balance amount is " + str(self.money) + " rupees")  
        
    def CheckCurrentAmount(self):   
        print(" ")
        print("Your current balance is " + str(self.money) + " rupees")