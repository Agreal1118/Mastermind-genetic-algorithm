import judge
import random

def krzyzowanie(rodzic1, rodzic2):                                      # x/(y) krzyzowanie jednego elementu pomiendzy 2 rodzicami z prawdopodobienstwem 50 procent na podwojny
    dziecko = rodzic1
    x = random.random()
    punkt1 = random.randint(0,n-2)
    punkt2 = random.randint(punkt1+1,n-1) 
    if x<=1:
        dziecko=[]
        for y in range(punkt1):
            dziecko.append(rodzic1[y])
        for y in range(punkt1,n):
            dziecko.append(rodzic2[y])
        if x<=0.5:
            for y in range(punkt2,n):
                dziecko[y]=rodzic1[y]
    return dziecko

def mutacja(rodzic):                                                    # y zmienia jeden kolor na kolejny z prawdopodobienstwem 20 procent
    x = random.random()
    if x<=0.2:
        lista = rodzic[:]
        dziecko =[]
        lista = list(set(rodzic))
        z = random.sample(lista,1)
        if z[0] == n:
            for y in rodzic:
                if y == z[0]:
                    dziecko.append(1)
                else:
                    dziecko.append(y)
        else:
            for y in rodzic:
                if y == z[0]:
                    dziecko.append(y+1)
                else:
                    dziecko.append(y)
    return dziecko
        
def mutajed(rodzic):                                                    # x zmienia losowy kolor na losowym miejscu na losowy inny 3 procent
    x = random.random()
    if x <=0.03:
        y = random.randint(0,n-1)
        z = rodzic[y]
        while z == rodzic[y]:
            z = random.randint(1,k)
        rodzic[y] = z
    return rodzic
        
def permutacje(rodzic):                                                 # x zmienia miejscami 2 losowe kolory
    x = random.random()
    if x <=0.03:
        y=random.randint(0,n-1)
        z=random.randint(0,n-1)
        while y==z:
            z=random.randint(0,n-1)
        rodzic[y], rodzic[z] = rodzic[z], rodzic[y]
    return rodzic

def odwrocenie(rodzic):                                                 # x odwraca fragment rodzica
    x = random.random()
    if x<=0.02:
        y=random.randint(0,n-2)
        z=random.randint(y+2,n)
        dziecko = rodzic[y:z]
        dziecko.reverse()
        rodzic[y:z]=dziecko
    return rodzic

def transpozycja():                                                     # y permutacja kolorow z prawdopodobienstwem 40 procent
    x = random.random()
    if x<=1:
        pass
        
def stworz_dziecko(rodzic1, rodzic2):                                   # funkcja tworzaca dzieci
    dziecko = krzyzowanie(rodzic1, rodzic2)
    dziecko = mutajed(dziecko)
    dziecko = permutacje(dziecko)
    dziecko = odwrocenie(dziecko)
    return dziecko
    
def losowykod():                                                        # funkcja losujaca kompletnie losowa kombinacje
    dziec=[]
    while len(dziec)<n:
        dziec.append(random.randint(1,k))
    return dziec

def ocena(kodoceny, zapytania):
    zlicz=0
    for x in zapytania:
        zlicz = zlicz + judge.oceniacz(kodoceny, x)
    return zlicz

def main():
    zapytania=[]
    print "Hello you will start Mastermind game, give me length of code"
    global n 
    #n = input()                                                         # n to dlugosc kodu
    n=judge.czy_poprawne()
    print "Give amount of colors"
    global k 
    #k = input()                                                         # k to ilosc kolorow
    k=judge.czy_poprawne()
    print "Now whole code"
    kod = map(int,raw_input().split())                                  # kod to kod podany przez gracza
    testkod=[]
    judge.dane(k,n,kod)
    for i in range(n):                                                  # pierwsze testowe losowanie w stylu [1,2,3,4....]
        testkod.append(i+1)
    xo, yo = judge.pytam(testkod,kod)                                      # xo - ilosc na dobrych miejscach, yo - na zlych miejscach, testkod - ostatni porownywany do wzorca kod 
    zapytania.append([testkod,xo,yo])
    rodzice=[]
    runda=1
    while len(rodzice) < 300:                                           #losowanie 300 pierwszych osobnikow
        losowy=losowykod()
        if losowy not in rodzice:
            rodzice.append([100,losowy])
    while n != xo:
        pokolenie = 0
        dzieci=[]
        rodziceo=[]
        if len(rodzice) < 1:                                            #jesli rodzicow jest za malo to tu dorzuca sie kolejnych losowych
            while len(rodzice) < 200:                                          
                losowy=losowykod()
                if losowy not in rodzice:
                    rodzice.append([100,losowy])
        while pokolenie<15:
            for x in rodzice:
                rodziceo.append([ocena(x[1],zapytania),x[1]])           # kazdy rodzic zostaje oceniony w formacie [ocena (im mniejsza tym lepsza),rodzic]
            rodziceo.sort()                                             # rodzice zostaja posortoswani od najlepszych do najgorszych
            zalicz=0
            for p in rodziceo:
                if p[0]!=0:
                    break
                zalicz+=1
            dzieci=rodziceo[:zalicz]                                    # usuwam rodzicow o wyniku gorszym niz 0
            for y in rodziceo:                                          # kazdy rodzic dostaje swoje dziecko, ktore rowniez zostaje ocenione
                stworz = [ocena(y[1],zapytania),stworz_dziecko(y[1],random.choice(rodziceo)[1])]
                if stworz not in dzieci and stworz[0]==0:
                    dzieci.append(stworz)
            pokolenie+=1
            rodzice = dzieci[:]
            rodziceo=[]
            dzieci=[]
        rodzice.sort()
        najlepsze=[]
        for z in rodzice:                                               # przepisanie rodzicow na liste najlepsze
            najlepsze.append(z[1])
        pra=0
        while pra==0:                                                   # petla wybierajaca losowy najlepszy kod ale taki ktory nie byl wczesniej zapytany
            pra=1
            if len(najlepsze)>0:
                wybor = random.choice(najlepsze)
                najlepsze.remove(wybor)
                for o in zapytania:
                    if wybor == o[0]:
                        pra=0                    
                        break
                if pra == 1:
                    xo,yo=judge.pytam(wybor,kod)
                    zapytania.append([wybor,xo,yo])
                    runda=runda+1
    print "Ha ha, this code ", wybor, " was so simple that i resolved it in ", runda, " rounds. easy-peasy"

if __name__ == "__main__":
    main()

