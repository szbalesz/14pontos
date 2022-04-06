def Felszin(a,b):

    return(a*b+a*c+b*c)*2

def Terfogat(a,b,c):

    return(a*b*c)

a = input("Kérem az első él hosszát centiméterben: ")
if a != "":
    b = int(input("Kérem a második él hosszát centiméterben: "))
    c = int(input("Kérem a harmadik él hosszát centiméterben: "))
    a = int(a)
    print(f"A téglatest felszíne {Felszin(a,b)} cm2" )
    print(f"A téglatest térfogata {Terfogat(a,b,c)} cm3")