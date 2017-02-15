# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:49:17 2015
@author: SpiffKringle
"""
import os
from Bio import SeqIO, Alphabet

targetDir = '/home/student/Downloads/seqdata'
extensions = set(['.ab1'])

generator =  os.walk(targetDir)
items = generator.next()
fileList = items[2]
dirName = items[0]
records = []
for fname in fileList:
    print fname
    if fname[-4:] in extensions:
        to_open = os.path.join(dirName,fname)
        OutName = to_open[:-4] +'.fastq'
        #print to_open
        Handle = open(to_open,'rb')
        record = SeqIO.read(Handle,'abi')
        record.seq.alphabet = Alphabet.IUPAC.ambiguous_dna
        trimmed = SeqIO.AbiIO._abi_trim(record[20:])
        print len(record), len(trimmed)
        records.append(trimmed)

for record in records:
    print record.id, len(record)
      
with open(targetDir + '/Multifasta.fasta','w') as f:
    for record in records:
        f.write('> ' + str(record.id) +'\n')
        f.write(str(record.seq) + '\n')
