# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:10:03 2023

@author: remi.gschwind
"""
### Accession numbers list retrieval 
## First, the total meaning all the unique inserts included in ResFinderFG v2.0 construction.
an_tot = []
tot = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_ARG_candidates/data/DNA_insert_seq_cdhit.fasta"
with open(tot , 'r') as f :
    for line in f :
        if ">" in line :
            an = str(line.strip().split(' ')[0]).strip().split('>')[-1]
            an_tot.append(an.strip())
## Second, the accession numbers found in the ResFinderFG v2.0 database.
an_rfg = []
rfg = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_ARG_candidates/data/ResFinder_FG.fasta"
with open(rfg , 'r') as f :
    for line in f :
        if ">" in line :
            an = line.strip().split("|")[1]
            an_rfg.append(an)
## Third, the accession numbers found in the annotation process output using prokka discarding accession numbers already included in ResFinderFG v2.0. 
an_prokka = []
line_prokka = []
prokka_output = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_ARG_candidates/data/prokka.gff"
with open(prokka_output , 'r') as f :
     for line in f :
         if "Prodigal" in line :
             an = line.strip().split()[0]
             annotation = line.strip().split('=')[-1]
             if an not in an_rfg :
                 an_prokka.append(an)
                 line_prokka.append(an + '|' + annotation)
## Then, with the last list, we can select specifically insert sequences containing a unique ORF
an_unique_orf = []
for acc_num in an_prokka :
    if an_prokka.count(acc_num) == 1 :
        an_unique_orf.append(acc_num)
annotation_unique_orf = []
for line in line_prokka :
    an = line.strip().split('|')[0]
    if an in an_unique_orf :
        annotation_unique_orf.append(line)
        
## A step has to be added to discard the accession numbers that were lost during the last cdhit step
## These inserts hold ARGs that are actually already included in the ResFinderFG v2.0 database. 
an_to_discard = []
db_before_cdhit = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_ARG_candidates/data/db.fasta"
with open(db_before_cdhit , 'r') as f :
    for line in f :
        if '>' in line :
            an = line.strip().split('|')[1]
            if an not in an_rfg :
                an_to_discard.append(an)
for an in an_to_discard :
    for line in annotation_unique_orf :
        if an in line :
            annotation_unique_orf.remove(line)
            

## We have to retrieve information that were described in the gb_output file from ResFinderFG v2.0 construction process.
gb_info = []
gb_output = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_ARG_candidates/data/gb_output.csv" 
with open(gb_output , 'r') as f :
    for line in f :
        an = line.strip().split(';')[0]
        if an in an_unique_orf :
            ### the atb used for selection was not available in some genbank file and were noted as ?
            ### so we get rid of them
            if "?" not in line :
                gb_info.append(line.strip().split(';')[0] + '|' + line.strip().split(';')[1] + '|' + line.strip().split(';')[2])

## These information have to be merged with the annotation that were found in the prokka output file. 
merge = []
for line1 in gb_info :
    an1 = line1.strip().split('|')[0]
    # print(an1)
    for line2 in annotation_unique_orf :
        if an1 in line2 :
            annotation = line2.strip().split('|')[-1]
            merge.append(line1 + '|' + annotation)

## we retrieve the accession numbers to get the genbank file containing all the corresponding insert sequences.
o_an_unique = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_ARG_candidates/output/an_unique.txt"
with open(o_an_unique , 'w') as f :
    for element in merge :
        f.write(element.strip().split('|')[0] + '\n')

## We retrieve the sequences of the inserts in the genbank file
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature
from Bio.SeqRecord import SeqRecord

gb = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_ARG_candidates/output/gb_unique_orf.gb"
seq_record = SeqIO.parse(gb , "genbank")
final_list = []

for record in seq_record :
    for line in merge :
        an = line.strip().split('|')[0]
        if record.id == an :
            final_list.append(str(">") + line.strip() + '\n' + str(record.seq))
## Writting the database
arg_candidates = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_ARG_candidates/output/ARGs_candidates.fasta"
with open(arg_candidates , 'w') as f :
    for element in final_list :
        f.write(element + '\n')
print(len(final_list))
        



