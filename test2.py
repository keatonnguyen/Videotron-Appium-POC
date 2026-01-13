class autobot:
    def __init__(self, name):
        self.name = name
        self.lives = 5

    def greet(self):
        return f"Hello, I am {self.name}, your autobot!"
    
    def lose_life(self):
        self.lives -= 1
        return f"{self.name} has {self.lives} lives remaining."
    
class optimus(autobot):
    def transform(self):
        return f"{self.name} is transforming!"
    
class bumblebee(autobot):
    def drive(self):
        return f"{self.name} is driving!"
    
def main():
    optimus_prime = optimus("Optimus Prime")
    bumblebee_bot = bumblebee("Bumblebee")
    
    print(optimus_prime.greet())
    print(optimus_prime.transform())
    
    print(bumblebee_bot.greet())
    print(bumblebee_bot.drive())
    
    print(optimus_prime.lose_life())
    print(bumblebee_bot.lose_life())

main()