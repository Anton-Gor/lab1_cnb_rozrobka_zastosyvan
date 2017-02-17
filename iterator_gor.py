e=''
while e!='q':
    try:
        class example:
            def __init__(self, start, stop):
                self._current=start
                self._current=stop
            def __iter__(self):
                return self
            def __next__(self):
                if self._current<self._stop:
                    result=self._current
                    self._current+=1
                    return result
                else:
                    raise StopIteration
        n=int(input('Enter the head(first number): '))
        m=int(input('Enter the tail(last number): '))
        while ((m-n)>1000)|((m-n)<1):
            print('Very big range or heads value is higher(equal) than tails! Wright another values of head and tail!')
            n=int(input('Enter the head(first number): '))
            m=int(input('Enter the tail(last number): '))
        r=range(n,m)
        for e in r:
            print(e)
    except ValueError:
        print('Wrong data!')
    print()
    e=str(input('enter-exit, q+enter-restart'))
if e=='q':
    exit()
