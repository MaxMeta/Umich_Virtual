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

