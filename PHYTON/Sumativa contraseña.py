print(" ")
print("Un numero major o igual que 1 i menor o igual que 5")
print("Una lletra minuscula")
print("Una lletra mayuscula")
print("Un dels seguents simbols: *,_,@")
print("Una lletra minuscula")
print("Un numero major o igual 6 i menor o igual que 9")
print("Un dels seguents sÃ­mbols: &,/,#")
print("Un numero menor o igual que 5")
print(" ")

password=input("INTRODUEIX UNA CONTRASENYA: ")
long=len(password)
#Asignamos a cada variable su mensaje de error
longitud=f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits"
a="“Error en el caràcter 1”"
b="“Error en el caràcter 2”"
c="“Error en el caràcter 3”"
d="“Error en el caràcter 4”"
e="“Error en el caràcter 5”"
f="“Error en el caràcter 6”"
g="“Error en el caràcter 7”"
h="“Error en el caràcter 8”"

#Comprobamos si en cada 
if len(password)>=6 and len(password)<=8:
    longitud=""

    if password[0].isnumeric():
        if int(password[0])>=1 and int(password[0])<=5:
            a="" 
    if password[1].isalpha():
        if password[1].islower():
            b="" 
    if password[2].isalpha():
        if password[2].isupper():
            c="" 
    if password[3]=="*" or password[3]=="_" or password[3]=="@" :
        d="" 
    if password[4].isalpha():
        if password[4].islower():
            e=""
    if password[5].isnumeric():
        if int(password[5])>=6 and int(password[5])<=9:
            f="" 
    if len(password)>=7:  
        if password[6]=="&" or password[6]=="/" or password[6]=="#" :
            g="" 
    else:
        g=""
        
    if len(password)>=8:  
        if password[7].isnumeric():
            if  int(password[7])<=5:
                h="" 
    else: 
        h=""

errores= a + b + c + d + e + f + g + h

if errores=="" and longitud=="":
    print ("“El format del PASSWORD és correcte”")
elif longitud=="":    
    print (errores)
else:
    print (longitud)