class Animal:
    legs=4
    @classmethod
    def talk(cls,name):
        print("{} walks with {} legs..".format(name,cls.legs))

Animal.talk('Dog')
Animal.talk('Cat')
        