from workingModule import Message

class Animal():
    def __init__(self, legs, ears, eyes, sound):
        self.legs = legs
        self.ears = ears
        self.eyes = eyes
        self.sound = sound

    def make_sound(self):
        return self.sound


class Dog(Animal):
    pass

dog = Dog(legs=4,ears=2, eyes=2, sound="Woof Woof")
print(dog.make_sound())

message = Message("SaM", "sam@test.com", "Thanks for reaching Us, We will get back to you soon.")

print(message.create_message())