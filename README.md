Here you will find the python script for batch trimming yor ab1 files...

Get the sequence data here:

http://dna2.macrogen.com/eng/data_access_inv.jsp?invkey=9445F9377F29CA4E831BBF34D5A18261&uI=owenje&oN=170207FN-031&fn=170207FN-031.zip

notes for me so I can remember what I did..

Get the blast binaries for linux, unzip them and then move the folder to your home directory.

gunzip -d ncbi-blast-2.6.0+-x64-linux.tar.gz 
tar xvpf ncbi-blast-2.6.0+-x64-linux.tar 
mv ncbi-blast-2.6.0+ ~

Open your .bashrc and then append the blast folder to your search path:

export PATH=$PATH:$HOME/ncbi-blast-2.6.0+/bin

ncbi-blast-2.2.30+-ia32-linux.tar.gz

Change directory to Downloads and download the 32bit linux binaries for BLAST:


wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.30/ncbi-blast-2.2.30+-ia32-linux.tar.gz

Download the install file for miniconda:

wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86.sh

Change the file permissions to make it executable:

chmod 777 Miniconda2-latest-Linux-x86.sh

run the install script"

./Miniconda2-latest-Linux-x86.sh

reload settings from your .bashrc:

source ~/.bashrc

type "conda" to confirm that minconda has installed correctly

Make a new python 2.7 environment called bio that has biopython and spyder installed:

conda create --prefix bio python=2.7 biopython spyder

Unzip the blast package and move the resulting directory to your home directory

gunzip -d ncbi-blast-2.2.30+-ia32-linux.tar.gz 
tar xvpf ncbi-blast-2.2.30+-ia32-linux.tar
mv ncbi-blast-2.2.30+ ~

remove the blast .gz file

rm ncbi-blast-2.2.30+-ia32-linux.tar.gz 

change directory to your home directory

make a directory to contain your custom blast database

mkdir BLASTDB

change to this directory

download the mibig protein file

wget mibig.secondarymetabolites.org/MIBiG_prot_seqs_1.3.fasta

change the name of the file to mibig.fasta

mv MIBiG_prot_seqs_1.3.fasta mibig.fasta

Make a blastdatabase from the file

makeblastdb -in ~/BLASTDB/mibig.fasta -parse_seqids -dbtype prot

open your .bashrc

nano ~/.bashrc

Your path should be set in a statement that looks like this:

export PATH="/home/student/miniconda2/bin:$PATH

Add this to the end:

:/home/student/ncbi-blast-2.2.30+/bin

So that the complete line looks like this:

export PATH="/home/student/miniconda2/bin:$PATH:/home/student/ncbi-blast-2.2.30+/bin

Close and save

Open your browser, paste the address below, and download the zipped sequences from our experiment:

http://dna2.macrogen.com/eng/data_access_inv.jsp?invkey=9445F9377F29CA4E831BBF34D5A18261&uI=owenje&oN=170207FN-031&fn=170207FN-031.zip

Change directory to downloads and unzip the sequnce file into a folder called seqdata

unzip 170207FN-031.zip -d seqdata

activate your virtual python environment

source activate bio

open the python ide you included in your environment

spyder

cut and paste the entire trimmer.py file from this repository into the temprary script file that has been created

Select the whole lot and run it in the currently open python console

Open a terminal and change directory to Downloads/seqdata, then verify that there is now a file called Multifasta.fasta in there

use nano to have a look at it

Blast all of the trimmed sequences in Multifasta.fasta against your mibig database:

blastx -query ~/Downloads/seqdata/Multifasta.fasta -db ~/BLASTDB/mibig.fasta -max_target_seqs 1 -outfmt 6 -out ~/blast_output.txt

