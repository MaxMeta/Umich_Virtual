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

Change directory to Downloads and download the 32bit linux binaries for BLAST

$wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.30/ncbi-blast-2.2.30+-ia32-linux.tar.gz

Download the install file for miniconda

wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86.sh

Change the file permissions to make it executable

chmod 777 Miniconda2-latest-Linux-x86.sh

run the install script
./Miniconda2-latest-Linux-x86.sh

reload settings from your .bashrc

source ~/.bashrc
type "conda" to confirm that minconda has installed corrctly

Make a new python 2.7 environment called bio that has biopython and spyder installed

conda create --prefix bio python=2.7 biopython spyder


.


