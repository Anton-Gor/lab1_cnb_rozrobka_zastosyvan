e=''
while e!='q':
    try:
        n=int(input('Enter the size of pack of cards: '))
        while n<1:
            print('Error!')
            n=int(input('Enter another number of cards: '))

        def decorator(func):
            def wrapper(*args, **kwargs):
                print("You just entered the parametres of card ")
                return func(*args, **kwargs)
            return wrapper

        @decorator
        def vvod(name, suit):
            print('Name of card: ' + name + '; suit of card: ' + suit)
        for i in range(0, n):
            if i!=n:
                print('Input parametres of next card:')
            name=str(input('Name of card: '))
            suit=str(input('Suit of card: '))
            vvod(name, suit)
    except ValueError:
        print('Wrong data!')
    print()
    e=str(input('enter-restart, q+enter-exit'))
if e=='q':
    exit()
