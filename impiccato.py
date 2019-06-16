#impiccato rev 1
##################################################################STRUTTURA DEL PROGRAMMA######################################################################################################
#tentativi di prova: testa (1) corpo (2) braccia sx (3) braccia dx (4) gamba sx (5) gamba dx (6) == Numero dei tentativi impiccato 
#funzione che preleva una parola a caso dal dizioario "dizionarioita.txt" e che la restituisce come stringa
#funzione che ne calcola la lunghezza
#funzione che legge un carattere, controlla che esso sia presente. Se presente, lo sottrae alla lunghezza della stringa e mostra all'utente quanti sono i caratteri rimanenti da indovinare
#Se i tentativi = 0 e rimasti caratteri da indovinare == PERSO ; ALTRIMENTI SE TENTATIVI > 0 E CARATTERI DA INDOVINARE = 0 UTENTE HA VINTO
#Non funziona con le parole accentate..
##################################################################################################################################################################################

import random #modulo per creare parola random 
#funzione che preleva una parola a caso dal dizionario "dizionarioita.txt" e che la restituisce come stringa
def leggiparola():
    valore = random.randint(0,400)
    f = open("dizionarioita.txt","r") #assegna alla variabile f la lettura del file, con gli annessi metodi write (non possibile perche' r e read/readline)
    for i in range(valore):   #metodo scemo, legge tra numero compreso tra 0 e 400 una riga 
        parola = f.readline()
    f.close()
    return parola

def calcolalunghezza(stringa):   #funzione che ne calcola la lunghezza della stringa estratta
    cnt = 0
    for c in stringa: #estrae un carattere dalla stringa
          cnt = cnt + 1
    return cnt

def getch(): #funzione che legge un carattere, funzionamento stupidissimissimo ottieni una stringa tramite input Se lungh. stringa > 1 ripeti input else accetta
    val = 1
    while val==1:
        stringa = input("Inserisci una lettera: ")
        if calcolalunghezza(stringa) > 1:
            print("DEVI INSERIRE UN SOLO CARATTERE!!")
            stringa=""
        else:
            val=0 #hai immesso un solo carattere - OK!!
    return stringa

def contains(c,stringa): #vede se un carattere è presente nella stringa: Se si, ne restituisce le occorrenze altrimenti restituisce 0
    conta =0
    for car in stringa:
        if car==c:
            conta = conta + 1
    return conta

def convertitrattini(stringa): #converte la stringa della parola in trattini 
    nuovastringa = stringa
    lista = []
    for c in stringa:
        if c!='\n': #veniva aggiunto anche il carattere di "a capo" alias \n
            lista.append('_')
    return lista
def aggiorna(c,lista,stringa):
    i = 0 #inizializza contatore
    for carattere in stringa: #per ogni carattere nella stringa
        if carattere == c: #se il carattere corrisponde
            lista[i]=c #aggiorna il carattere nella lista (stringhe non sono mutabili)
        i +=1 #aumenta il contatore [0,lunghezza stringa)
    return lista #restituisce la stringa aggiornata

def attesa():
    input("premi un tasto per uscire..., hope u enjoyed it! :)\n")
#esecuzione
tentativi=6
parola = leggiparola() #ottiene la parola dal dizionario
parola_backup = parola #se ne salva una copia
parolamisteriosa = convertitrattini(parola) #crea una lista con soli "trattini"
print("=> CARATTERI RIMASTI DA INDOVINARE: ",parolamisteriosa) #stampa tutti i caratteri iniziali da indovinare
caratteri = calcolalunghezza(parola)-1#viene calcolato un carattere in piu' per via dello \n
while tentativi >0 and caratteri>0: #finchè i tentativi sono > 0 e i caratteri da indovinare sono > 0
    print("tentativi: ",tentativi)   #stampa i tentativi
    print("caratteri rimasti da indovinare: ",caratteri)  #stampa solo i caratteri rimanenti da indovinare
    c = getch() #ottiene il carattere da tastiera
    if contains(c,parola) == 0: #se le occorrenze del carattere sono == 0
        tentativi = tentativi - 1 #diminuisce i tentativi
        print("Argh, non e' quello! Ti rimangono",tentativi," tentativi, attento!\n")
    else:                                               
        caratteri = caratteri - contains(c,parola) #altrimenti aggiorna il contatore dei caratteri da indovinare
        parola = parola.replace(c,"") #rimuove i caratteri dalla stringa in modo da non ricontare lo stesso carattere più volte
        print("BRAVO!! => CARATTERI RIMASTI DA INDOVINARE: ",aggiorna(c,parolamisteriosa,parola_backup))

if tentativi == 0:
    print("hai perso, mi spiace, riprova sarai più fortunato!.La parola esatta era ",parola_backup)
if caratteri == 0:
    print("Bravo!! Hai indovinato la parola segreta. La parola era ",parola_backup)
attesa()
