import re

# reading given tsv file
with open("TCGA_PAAD_182_norm_beta.txt", 'r') as myfile:
    with open("TCGA_PAAD_182_norm_beta.csv", 'w') as csv_file:
        for line in myfile:
            # Replace every tab with comma
            fileContent = re.sub("\t", ",", line)

            # Writing into csv file
            csv_file.write(fileContent)

# output
print("Successfully made csv file")