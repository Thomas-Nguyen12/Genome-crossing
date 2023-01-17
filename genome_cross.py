import numpy as np
import re

print ("This program will predict the mendelian ratio of a dihybrid cross")
print ("\n \n")
print ("Each genome contains four letters which represent the two alleles of each gene")
print ("Please group alleles according gene")
print ("Example genome: AaBb ")
print ("both A and a are alleles for the same gene")
print ("B and b are alleles for the same gene")


print ("\n")


genome1 = input("please input your first four letter genome: ")
genome11_define = input("What does the dominant gene: " + str(genome1[0]) + " express?")
genome12_define = input("What does the dominant gene: " + str(genome1[2]) + " express?")

genome2 = input("Please input your second four letter genome: ")
first_genome = []
second_genome = []

for i in genome1:
    first_genome.append(i)
for i in genome2:
    second_genome.append(i)

print ("First genome = {}".format(first_genome))
print ("Second genome = {}".format(second_genome))

# Here i will split the first_genome into gametes
gamete1 = []

gamete1.append(first_genome[0] + first_genome[2])
gamete1.append(first_genome[0] + first_genome[3])
gamete1.append(first_genome[1] + first_genome[2])
gamete1.append(first_genome[1] + first_genome[3])

print ("gamete1: " + str(gamete1))


# Here, i will split the second_genome into gametes

gamete2 = []

gamete2.append(second_genome[0] + second_genome[2])
gamete2.append(second_genome[0] + second_genome[3])
gamete2.append(second_genome[1] + second_genome[2])
gamete2.append(second_genome[1] + second_genome[3])

print ("Gamete 2: " + str(gamete2))


# I need to make sure that each gamete is the haploid of the genotype
pred_genome = []
for i in gamete1:
    for a in gamete2:
        pred_genome.append(i + a)
    
print ("\n")
print ("Predicted genotypes: ")
print (pred_genome)

for i in pred_genome:
    print ("\n")
    print (i)
    if i[0].isupper():
        if i[2].isupper():
            print ("The first allele set is homozygous dominant")
        else:
            print ("The first allele set is heterozygous")
    if i[0].islower():
        if i[2].islower():
            print ("The first allele set is homozygous recessive")
        else:
            print ("the first set is heterozygous")
    if i[1].isupper():
        if i[3].isupper():
            print ("The second allele set is homozygous dominant")
        else:
            print ("The second allele set is heterozygous")
    if i[1].islower():
        if i[3].islower():
            print ("The second allele set is homozygous recessive")
        else:
            print ("the second set is heterozygous")
        
