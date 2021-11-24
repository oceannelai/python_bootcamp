from exercisexp import Dog

class PetDog(Dog):
    def __init__(self, trained=False):
        self.trained = trained
    def train(self):
        print(Dog.bark())
        self.trained = True
    def play(self, *args):
        print(f'{args} dance together')
    play("Yasaar","Varsh","Saad","Kyle")

    def do_a_trick(self):
        if self.trained  == True:
            print(Dog.dog_name.play() + "does a barrel roll")

