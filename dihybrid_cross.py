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
genome11_define = input("What does the allele set: " + str(genome1[0] + genome1[1]) + " express? ")
genome12_define = input("What does the allele set: " + str(genome1[2] + genome1[3]) + " express? ")

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
        pred_genome.append(i[0] + a[0] + i[1] + a[1])
    
print ("\n")
print ("Predicted genotypes: ")

arr = np.array(pred_genome)
arr = arr.reshape(4, 4)
print (arr)

            
# Here, I will calculate the Phenotype ratios
# Phenotype ratios are measure what is expressed as a result of the phenotype
# I can check for the presence of dominant alleles



AABB = 0
AaBb = 0
AABb = 0
AaBB = 0

AAbb = 0
Aabb = 0

aaBB = 0
aaBb = 0

aabb = 0





for i in pred_genome:
    
    if i[0].isupper() or i[1].isupper():
        
        if i[2].isupper() or i[3].isupper():
            
            
            AABB += 1
            
        if i[2].islower() and i[3].islower():
            
            AAbb += 1
        if i[2] != i[3]:
            AABb += 1
            
    if i[1].islower() and i[2].islower():
        if i[2].isupper() and i[3].isupper():
            aaBB += 1
            
        if i[2].islower() and i[3].islower():
            aabb += 1
        if i[2] != i[3]:
            aaBb += 1
    if i[1] != i[0]:
        if i[2].isupper() and i[3].isupper():
            AaBB += 1
        if i[2].islower() and i[3].islower():
            Aabb += 1
        if i[2] != i[3]:
            AaBb += 1
first_exp_second_exp = AABB + AABb + AaBB + AaBb
first_exp_second_rec = AAbb + Aabb

first_rec_second_exp = aaBb + aaBB
first_rec_second_rec = aabb

print ("Phenotype ratios: ")
print ("{0} : {1} : {2} : {3}".format(first_exp_second_exp, first_exp_second_rec, first_rec_second_exp, first_rec_second_rec))



