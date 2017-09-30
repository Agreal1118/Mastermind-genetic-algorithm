import sys
def dane(kol,dlu,szyfr):                                                    # funkcja ktora trzyma w sobie szyfr kolory i dlugosc szyfru
    global pra
    pra = szyfr[:]
    global k 
    k = kol
    global n
    n = dlu

def czy_poprawne():                                                         # funkcja ktora odpowiada za obsluge wyjatkow
    try:
        if n and k:
            pra=0
            while pra == 0:
                pra=1
                x=raw_input()
                y=[int(w) for w in x.split()]
                if len(y)!=n:
                    print "Wrong length of code"
                    pra=0
                    continue
                for z in y:
                    if z>k:
                        print "Color is too high"
                        pra=0
                        continue
                    if z<0:
                        print "There is something like negative colour, write again"
                        pra=0
                        continue
                    if type(z)!=int:
                        print "You could write only natural numbers (for this game 0 is not natural)"
                        pra=0
                        continue
            return y
    except EOFError:
        print "HA HA You are terrible weak!"
        sys.exit(0)
    except NameError:
        try:
            pra = 0
            while pra==0:
                x=raw_input()
                pra=1
                if x.isdigit()>0:
                    x=int(x)
                    if x<1:
                        pra=0
                        print "That must be nuber higher than 0"
                        continue
                else:
                    pra=0
                    print"That must be natural number"
                    continue
            return x
        except EOFError:
            print "Ha ha you are terrible weak!"
            sys.exit(0)
        
def pytam(sekwencja,kod):
    wla=0
    niewla=0
    y=0
    zkopkod=kod[:]
    sequ=sekwencja[:]
    for x in sekwencja:
        if x==kod[y]:
            wla=wla+1
            zkopkod.remove(x)
            sequ.remove(x)
        y=y+1
    for z in sequ:
        if z in zkopkod:
            zkopkod.remove(z)
            niewla=niewla+1
    if kod == pra:
        print "For code ", sekwencja," Amount on good places : " + str(wla) + " Amount of good colours on wrong places: " + str(niewla)
    return wla,niewla

def oceniacz(kodoceny,wzor):                                            #modul oceniajacy rodzicow w stosunku do zapytan ktore sie juz odbyly
    
    dobre, zle = pytam(kodoceny,wzor[0])
    punkty = 0
    if dobre>wzor[1]:
        if zle>wzor[2]:
            punkty = dobre+zle-wzor[1]-wzor[2]
        else:
            while dobre!=wzor[1] or zle!=wzor[2]:
                while dobre!=wzor[1] and zle!=wzor[2]:
                    dobre -=1
                    zle +=1
                    punkty +=1
                if dobre!=wzor[1]:
                    dobre -=1
                    punkty +=1
                if zle!=wzor[2]:
                    zle +=1
                    punkty +=1
    else:
        if zle>wzor[2]:
            while dobre!=wzor[1] or zle!=wzor[2]:
                while dobre!=wzor[1] and zle!=wzor[2]:
                    dobre +=1
                    zle -=1
                    punkty +=1
                if dobre!=wzor[1]:
                    dobre +=1
                    punkty +=1
                if zle!=wzor[2]:
                    zle -=1
                    punkty +=1
        else:
            punkty = wzor[1]+wzor[2]-dobre-zle
    return punkty 
