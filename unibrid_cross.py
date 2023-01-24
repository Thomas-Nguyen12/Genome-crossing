import re
import numpy as np

genotype1 = input("please enter your first genotype: ")
genotype2 = input("Please enter your second genotype: ")
generation = input("which generation are you predicting? ")

print ("Genotype1: " + genotype1)
print ("Genotype2: " + genotype2)

gamete1 = []
gamete2 = []

for i in genotype1:
    gamete1.append(i)
for a in genotype2:
    gamete2.append(a)

print (gamete1)
print (gamete2)

pred = []

for i in gamete1:
    for a in gamete2:
        pred.append(i + a)
print (generation + " Prediction: ")
pred = np.array(pred)

pred = pred.reshape(2, 2)
print (pred)

# Here, i will calculate the probability that the offspring will display
# The dominant phenotype
# Given that every couple has exactly two offspring

# Dominant = Aa, AA
# Recessive = aa
dom = 0
rec = 0
for i in pred:
    if i[0].isupper() and i[1].isupper():
        dom += 1
    if i[0].islower() and i[1].islower():
        rec += 1
    else:
        dom += 1
total = dom + rec

print ("Probability of dominant expression: " + str((dom/total) * 100) + " %")
print ("Probability of recessive expression: " + str((rec / total) * 100 ) + " %")



