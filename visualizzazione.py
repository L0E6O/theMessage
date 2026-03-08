import sys
import numpy as np
from PIL import Image

colori = [0, 85, 170, 255]

if len(sys.argv) == 5:
    try:
        # Prende gli argomenti dal terminale e li converte in numeri interi
        colori = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])]
    except ValueError:
        print("Errore: Devi inserire dei numeri validi. Uso i default.")
elif len(sys.argv) > 1:
    print("Attenzione: Devi passare esattamente 4 colori, oppure nessuno. Uso i default.")

# Mappatura delle lettere con i colori scelti
mapping = {'A': colori[0], 'B': colori[1], 'C': colori[2], 'D': colori[3]}

WIDTH = 146
HEIGHT = 2077

try:
    with open('message.txt', 'r') as f: # apro il msg in mod lettura (with chiude il file appena la lettura è finita), metto in f
        data = f.read().strip().replace('\n', '').replace('\r', '') #rimpiazzo gli 'a capo' con vuoto e tolgo spazi da inizio e fine, poi salvo in data
    
    pixels = [mapping.get(char, 127) for char in data] #scrive in pixels in numeri in base alla mappa fornita, mette 127 se c'è un carattere inspettato
    img_array = np.array(pixels, dtype=np.uint8).reshape((HEIGHT, WIDTH)) #converte i numeri in uint8 e li mette in un array, che poi dispone come l'immagine che si vuole
    
    img = Image.fromarray(img_array) # crea immagine
    nameInput = input("Come vuoi salvare il file? [default: alieno]\n")
    name = "alieno"
    if(nameInput):
        name = nameInput
    img.save("./data/" + name + '.png') # salva
    print(f"Immagine generata! Colori usati: A={colori[0]}, B={colori[1]}, C={colori[2]}, D={colori[3]}")

    apertura = input("Vuoi aprire il file? [s/altro] \n")

    if (apertura == "s"):
        img.show() 

except Exception as e:
    print(f"Qualcosa è andato storto: {e}")
