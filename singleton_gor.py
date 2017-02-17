class OneOnly:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(OneOnly, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.suit_of_card = 'chirva'


obj1 = OneOnly()
print(obj1.suit_of_card)

obj2 = OneOnly()
obj2.suit_of_card = 'Buba'
print(obj1.suit_of_card)