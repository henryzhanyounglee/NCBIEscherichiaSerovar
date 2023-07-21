# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 09:43:32 2023 A.D. R.O.C. year 112

@author: henryzhanyounglee
"""

from ftplib import FTP
import pandas as pd
import numpy as np
import time
import os

f = pd.read_csv('assembly_summary_genbank.txt' , sep = 'delimiter' , header = 1)
f.rename(columns = {'#assembly_accession	bioproject	biosample	wgs_master	refseq_category	taxid	species_taxid	organism_name	infraspecific_name	isolate	version_status	assembly_level	release_type	genome_rep	seq_rel_date	asm_name	asm_submitter	gbrs_paired_asm	paired_asm_comp	ftp_path	excluded_from_refseq	relation_to_type_material	asm_not_live_date	assembly_type	group	genome_size	genome_size_ungapped	gc_percent	replicon_count	scaffold_count	contig_count	annotation_provider	annotation_name	annotation_date	total_gene_count	protein_coding_gene_count	non_coding_gene_count	pubmed_id': 'col1'}, inplace = True)
###The Name of the columns may subject to changes due to NCBI's choice. Just copy and paste the headers.
ff = f 
rows = ff.query('col1.str.contains("Escherichia")', engine='python')###Could be anyother thing inside the "" Keyword
rows.to_csv('Escherichia.csv')  
f = pd.read_csv('Escherichia.csv' , sep = '\t' , header = 0)


path = r'E:/XDXDXD/' ###Path to your dir
GZFTP = []
ffff = []
for root, dirs, ff in os.walk( path):
    for fff in ff:
        if fff[:30] not in ffff:
            ffff.append(fff[:30])
        for files in f['ftp_path']:
            if files[57:] not in ffff[:30]:
                GZFTP.append( files)

for files in f['ftp_path']: 
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect('ftp.ncbi.nlm.nih.gov')
    ftp.login("anonymous",'MyEmail@Myemail.something')###NCBI allows anonymous login according to my understanding, remember to change the email address.
    ftp.cwd(files[28:])
    filenames = ftp.nlst()
    for filename in filenames:
        fh =  open(filename, 'wb+').write
        ftp.retrbinary(f'RETR {filename}',fh)
    ftp.set_debuglevel(0)
    time.sleep(5)###Time 5 seconds sounds more safe!?
ftp.quit()    
    
