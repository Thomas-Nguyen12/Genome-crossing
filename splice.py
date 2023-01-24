from Bio.Seq import Seq
import re


df = {
    "Rosalind_10": "ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG",
    "Rosalind_12": "ATCGGTCGAA",
    "Rosalind_15": "ATCGGTCGAGCGTGT",
    }

pre_mrna = Seq(df["Rosalind_10"])

exon = Seq(df["Rosalind_15"])


exon1 = exon.reverse_com
