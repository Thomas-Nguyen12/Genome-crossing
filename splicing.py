## Removing the exons and introns of a RNA string

import re
import numpy as np
from Bio import Data
from Bio.Seq import Seq
pre_mrna = {
    "pre_mRNA": "ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG",
    "introns": "ATCGGTCGAA",
    "exons": "ATCGGTCGAGCGTGT",
    }

amino_acid = {
    
    }

start_codon = ["AUG"]
stop_codons = ["UAA", "UAG", "UGA"]

print ("pre-mRNA molecule: ")
print (pre_mrna["pre_mRNA"])
print ("\n")
## Must return a protein string reuslting from transcription and translation

# Step 1: Splicing method

mRNA = re.split(pre_mrna["introns"], pre_mrna["pre_mRNA"])
mRNA1 = ''.join(mRNA)

mRNA1 = re.sub("T", "U", mRNA1)
# Replace the T in mRNA with U
print ("mRNA: ")
print (mRNA1)


# Step 2: Translation

translation = {
    "A": "T",
    "U": "A",
    "G": "C",
    "C": "G",
    }


protein = []

for i in mRNA1:
    protein.append(translation[i])
    
protein1 = ''.join(protein)
print ("\n")
print ("protein: ")
print (protein1)

print (len(protein1)) # 90

a = 0


# Sample: AAATTTCCCGGG --> AAA TTT CCC GGG
sequence = []
a = 0

    
while (a <= len(protein) - 3):
    triplet = []
    triplet.append(protein[a])
    triplet.append(protein[a+1])
    triplet.append(protein[a+2])
    

  
   
    sequence.append(triplet)

    a += 1
print ("\n")
print ("triplet sequences")


print (sequence)

print ("\n")
print ("Readable triplet sequences")


triplet_seq = []
for i in sequence:
    triplet_seq.append(''.join(i))

print (len(sequence) / 3)
print (triplet_seq)


mRNA2 = Seq(mRNA1)
print ("\n")
print ("Translated protein")

print (mRNA2.translate())
print (len(mRNA2.translate()))



# Remember to account for start / stop codons
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = [1, 2, 3, 4, 5]
y = [2, 4, 9, 16, 25]

plt.scatter(x, y)
