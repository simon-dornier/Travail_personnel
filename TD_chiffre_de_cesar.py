alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


##### Codage d'un message par la méthode de César

def codage(message,d):
    """
    données : message, de type str, est le message à encoder | d, de type int, décalage
    résultat : messagecode, de type str, est le message encodé
    """
    messagecode = ""
    for k in range(0,len(message)):
        if message[k] == " ":
            messagecode = messagecode + " "
        for i in range(0,25): #pour chaque lettre du message, on parcours la liste alphabet
            if message[k]==alphabet[i]:
                messagecode = messagecode + alphabet[(i+d)%26] #(i+d)%26 = indice de la lettre avec un décalage d
    return messagecode

#print(codage("bonjour tout le monde",3))

##### Calcul de la fréquence de chaque lettre dans un message codé

def freq_lettres(messagecode):
    liste_freq = [0 for i in range(26)]
    for k in range(len(messagecode)):
        for i in range(26):
            if messagecode[k] == alphabet[i]:
                liste_freq[i] = liste_freq[i] + 1
    return(liste_freq)
print(freq_lettres("bonjour tout le monde"))

##### Calcul du décalage probable

def calcul_auto_decal(messagecode):
    indicemax = 0
    liste_freq = freq_lettres(messagecode)
    for i in range(26):
        if liste_freq[i] > indicemax:
            indicemax = i
    if indicemax >= 4:
        decalage = indicemax - 4
    else:
        decalage = indicemax + 22
    return(decalage)

message = "pas si facile que cela le code cesar"   
text_cod = "tew wm jegmpi uyi gipe pi gsheki hi giwev"
decal = calcul_auto_decal(text_cod)
print(codage(text_cod,-decal))