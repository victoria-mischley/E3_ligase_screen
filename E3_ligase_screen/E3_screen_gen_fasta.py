import pandas as pd
import argparse

def args():
    parser = argparse.ArgumentParser(description='Rename MSAs and Split Jobs')
    parser.add_argument('protein_name', type=str, help='name of protein')
    parser.add_argument('protein_sequence', type=str, help = 'sequence of protein')
    parser.add_argument('name_of_fasta_file', type=str, help = 'desired name for the fasta file')
    args = parser.parse_args()
    return args

##########################################################################################################
E3_ligase_csv = "E3_ligase_screen/E3_list.csv"
E3_df = pd.read_csv(E3_ligase_csv)

def main(protein_name, protein_sequence, name_of_fasta_file):
    for ind in E3_df.index:
        E3_name = E3_df['Name'][ind]
        E3_sequence = E3_df['Sequence'][ind]
        combined_name = f">{E3_name}_{protein_name}"
        combined_sequence = f"{E3_sequence}:{protein_sequence}"
        if name_of_fasta_file[-6:] == ".fasta":
            final_fasta_file_name = name_of_fasta_file
        else:
            final_fasta_file_name = f"{name_of_fasta_file}.fasta"
        
        newfile = open(final_fasta_file_name, "a")
        newfile.write(combined_name + '\n')
        newfile.write(combined_sequence + '\n')
        


if __name__ == '__main__':
    args = args()
    protein_name = args.protein_name
    protein_sequence = args.protein_sequence
    name_of_fasta_file = args.name_of_fasta_file
    main(protein_name, protein_sequence, name_of_fasta_file)