import judge
import random
kody=[]                                                                 # kody to lista z wylosowanym kodem
def main():                                                             
    moj=[]
    ilorund = 0                                                            
    print "Hello you will start Mastermind game, give me length of code"
    #n = input()
    n=judge.czy_poprawne()                                             # n to dlugosc kodu
    print "Give amount of colors"
    #k = input()
    k=judge.czy_poprawne()                                             # k to ilosc kolorow
    for x in xrange(n):                                                 # Losowanie kodu
        kody.append(random.randrange(1,k+1,1))
    judge.dane(k,n,kody)
    print "Attention, game starts"
    do,zle=0,0
    while(do!=n):                                                       # wczytanie danych do sedziego
        print "Give me your sequence"
        moj=judge.czy_poprawne()                                       # wczytuje kolejna sekwencje gracza
        do,zle=judge.pytam(moj,kody)                                   # porownuje ja do szyfru
        ilorund = ilorund + 1                                           # licznik rund
    print "Congratulation you won in " + str(ilorund) + " rounds"

if __name__ == "__main__":
    main()
