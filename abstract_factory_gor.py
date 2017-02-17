q=''
while q!='e':
    try:
        class Myclass(object):
            def __init__(self, item_factory = None):
                self.item_factory=item_factory

            def get(self):
                item=self.item_factory.get_()
                print("Name: ", item.name())
                print( "Year: ", self.item_factory.year())
                print ("Company: ", self.item_factory.company())
                print ("Genre: ", self.item_factory.genre())

        class STALKER(object):
            def name(self):
                return "S.T.A.L.K.E.R. Shadow of Chernobyl"
            def __str__(self):
                return "S.T.A.L.K.E.R. Shadow of Chernobyl"

        class Outlast(object):
            def name(self):
                return "Outlast"
            def __str__(self):
                return "Outlast"

        class Dead_Space(object):
            def name(self):
                return "Dead Space"
            def __str__(self):
                return "Dead Space"

        class Darksiders(object):
            def name(self):
                return "Darksiders"
            def __str__(self):
                return "Darksiders"

        class FEAR(object):
            def name(self):
                return "F.E.A.R."
            def __str__(self):
                return "F.E.A.R."

        class Metro2033(object):
            def name(self):
                return "Metro2033"
            def __str__(self):
                return "Metro2033"

        class Left4Dead2(object):
            def name(self):
                return "Left4Dead2"
            def __str__(self):
                return "Left4Dead2"

        class Witcher3(object):
            def name(self):
                return "Witcher3"
            def __str__(self):
                return "Witcher3"

        class DarkSouls3(object):
            def name(self):
                return "DarkSouls3"
            def __str__(self):
                return "DarkSouls3"

        class Bioshock(object):
            def name(self):
                return "Bioshock"
            def __str__(self):
                return "Bioshock"

        class First_game(object):
            def get_(self):
                return STALKER()
            def year(self):
                return "2007"
            def company(self):
                return "GSC Game World"
            def genre(self):
                return "survival horror"

        class Second_game(object):
            def get_(self):
                return Outlast()
            def year(self):
                return "2013"
            def company(self):
                return "Red Barrels"
            def genre(self):
                return "survival horror"

        class Third_game(object):
            def get_(self):
                return Dead_Space()
            def year(self):
                return "2008"
            def company(self):
                return "Visceral Games"
            def genre(self):
                return "survival horror"

        class Fourth_game(object):
            def get_(self):
                return Darksiders()
            def year(self):
                return "2010"
            def company(self):
                return "Vigil Games"
            def genre(self):
                return "slasher"

        class Fifth_game(object):
            def get_(self):
                return FEAR()
            def year(self):
                return "2005"
            def company(self):
                return "Monolith Productions"
            def genre(self):
                return "survival horror"

        class Sixth_game(object):
            def get_(self):
                return Metro2033()
            def year(self):
                return "2010"
            def company(self):
                return "4A Games"
            def genre(self):
                return "survival horror"

        class Seventh_game(object):
            def get_(self):
                return Left4Dead2()
            def year(self):
                return "2009"
            def company(self):
                return "Valve Corporation"
            def genre(self):
                return "survival horror"

        class Eighth_game(object):
            def get_(self):
                return Witcher3()
            def year(self):
                return "2015"
            def company(self):
                return "CD Projekt RED"
            def genre(self):
                return "Action/RPG"

        class Ninth_game(object):
            def get_(self):
                return DarkSouls3()
            def year(self):
                return "2016"
            def company(self):
                return "FromSoftware"
            def genre(self):
                return "Action/RPG"

        class Tenth_game(object):
            def get_(self):
                return Bioshock()
            def year(self):
                return "2007"
            def company(self):
                return "Irrational Games"
            def genre(self):
                return "shooter"


        print('Favourite games: ')
        print('About which game you want to know some information?')
        print('1-S.T.A.L.K.E.R.')
        print('2-Outlast')
        print('3-Dead Space')
        print('4-Darksiders')
        print('5-F.E.A.R.')
        print('6-Metro 2033')
        print('7-Left4Dead2')
        print('8-Witcher 3')
        print('9-Dark Souls 3')
        print('10-Bioshock')
        print()
        print()
        n=int(input('Enter the number of game do you want to choose: '))
        if n==1:
            print('First game: ')
            a=Myclass(First_game())
            a.get()
        elif n==2:
            print ('Second game: ')
            b=Myclass(Second_game())
            b.get()
        elif n==3:
            print ('Third game: ')
            b=Myclass(Third_game())
            b.get()
        elif n==4:
            print ('Fourth game: ')
            b=Myclass(Fourth_game())
            b.get()
        elif n==5:
            print ('Fifth game: ')
            b=Myclass(Fifth_game())
            b.get()
        elif n==6:
            print ('Sixth game: ')
            b=Myclass(Sixth_game())
            b.get()
        elif n==7:
            print ('Seventh game: ')
            b=Myclass(Seventh_game())
            b.get()
        elif n==8:
            print ('Eighth game: ')
            b=Myclass(Eighth_game())
            b.get()
        elif n==9:
            print ('Ninth game: ')
            b=Myclass(Ninth_game())
            b.get()
        elif n==10:
            print ('Tenth game: ')
            b=Myclass(Tenth_game())
            b.get()
        else:
            while (n>10)|(n<10):
                print('Wrong number! Try again!')
                n=int(input('Enter the number of game do you want to choose: '))
    except ValueError:
        print('Wrong data!')
    print()
    e=str(input('Enter-restart, q+enter-exit'))
if e==q:
    exit()