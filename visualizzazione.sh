#!/bin/bash
A=${1:-0} #se il valore non è assegnato, dà default
B=${2:-85}
C=${3:-170}
D=${4:-255}
echo "lista colori: A: $A B: $B C: $C D: $D"
echo "Converto..."
echo -e "P2\n146 2077\n255" > alieno.pgm #TODO: SPIEGA
sed "s/A/$A /g; s/B/$B /g; s/C/$C /g; s/D/$D /g" message.txt >> ./data/alieno.pgm #TODO: SPIEGA
read -p "Vuoi visualizzare il file? [s/altro]" ans
if [[ "$ans" == "s" ]]; then
    xdg-open alieno.pgm
fi
