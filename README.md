# E3_ligase_screen

E3_screen_gen_fasta.py =  is a script which allows you to generate a fasta file for a protein against a pannel of E3 ligases. 
E3_list.csv = is a csv file with the names and corresponding sequences of a pannel of E3 ligases. 

Input to E3_screen_gen_fasta.py:
- protein_name = name of the protein you are screening
- protein_sequence = sequence of the name of the protein that you are screening
- fasta_file_name = the desired name for the fasta file that will be generated with this script.

Output of  E3_screen_gen_fasta.py
- fasta_file_name.fasta which is formated in the following way:
   - >E3_name_protein_name
   - E3_sequence:protein_sequence

Workflow:
- use E3_ligase_screen to generate fasta file
- after fasta_file is generated: use pipeline_colabfold_batch to generate MSA files and AF models
- after AF models are generated: use PPIScreenML to determine interaction
