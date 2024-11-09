from tabulate import tabulate
import itertools
from itertools import islice
import argparse

# arguments
parser = argparse.ArgumentParser(description='Available inputs')

# -i is argument name, dest is where it will be saved inside the parsed arguments Namespace
parser.add_argument('-1', dest='file_path1', help = 'Path to the first input file')
parser.add_argument('-2', dest='file_path2', help = 'Path to the second input file')
parser.add_argument('-3', dest='file_path3', help = 'Path to the third input file')
parser.add_argument('-4', dest='file_path4', help = 'Path to the fourth input file')

args = parser.parse_args()

print('File path 1: ', args.file_path1)
print('File path 2: ', args.file_path2)
print('File path 3: ', args.file_path3)
print('File path 4: ', args.file_path4)

if not args.file_path1:
    print("Usage: readmct.py -1 mctfile1.mct -2 mctfile2.mct -3 mctfile3.mct -4 mctfile4.mct")
    print("You need at least one file path.")
    quit()

# datasets
dataset1 = []
dataset2 = []
dataset3 = []
dataset4 = []

# get the 1st data set
if args.file_path1:
    try:
        with open(args.file_path1, "r") as filea:
            for line in itertools.islice(filea, 80):
                if "+" not in line:
                    dataset1.append(line)
    except IOError:
        print("Path or filename (1) incorrect, quitting...")
        quit()

# get the 2nd data set
if args.file_path2:
    try:
        with open(args.file_path2, "r") as fileb:
            for line in itertools.islice(fileb, 80):
                if "+" not in line:
                    dataset2.append(line)
    except IOError:
        print("Path or filename incorrect, quitting...")
        #quit()

# get the 3rd data set
if args.file_path3:
    try:
        with open(args.file_path3, "r") as filec:
            for line in itertools.islice(filec, 80):
                if "+" not in line:
                    dataset3.append(line)
    except IOError:
        print("Path or filename incorrect, quitting...")
        #quit()

# get the 4th data set
if args.file_path4:
    try:
        with open(args.file_path4, "r") as filed:
            for line in itertools.islice(filed, 80):
                if "+" not in line:
                    dataset4.append(line)
    except IOError:
        print("Path or filename incorrect, quitting...")
        #quit()

# combine every 4 items
dataset1_combined = [''.join([dataset1[i], dataset1[i+1], dataset1[i+2], dataset1[i+3]]).strip() for i in range(0, len(dataset1), 4)]
dataset2_combined = [''.join([dataset2[i], dataset2[i+1], dataset2[i+2], dataset2[i+3]]).strip() for i in range(0, len(dataset2), 4)]
dataset3_combined = [''.join([dataset3[i], dataset3[i+1], dataset3[i+2], dataset3[i+3]]).strip() for i in range(0, len(dataset3), 4)]
dataset4_combined = [''.join([dataset4[i], dataset4[i+1], dataset4[i+2], dataset2[i+3]]).strip() for i in range(0, len(dataset4), 4)]

# elements to array for the table
dataset1_combined = [[item] for item in dataset1_combined]
dataset2_combined = [[item] for item in dataset2_combined]
dataset3_combined = [[item] for item in dataset3_combined]
dataset4_combined = [[item] for item in dataset4_combined]

# check if the datasets are empty
if not dataset1_combined: dataset1_combined = [[''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], ['']]
if not dataset2_combined: dataset2_combined = [[''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], ['']]
if not dataset3_combined: dataset3_combined = [[''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], ['']]
if not dataset4_combined: dataset4_combined = [[''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], ['']]

# adding sector, sector block and block number
for x in range(len(dataset1_combined)):
    dataset1_combined[x] = [x] + [str(x+x+x+x)+"\n"+str(x+x+x+x+1)+"\n"+str(+x+x+x+x+2)+"\n"+str(x+x+x+x+3)] + ["0\n1\n2\n3"] + dataset1_combined[x] + dataset2_combined[x] + dataset3_combined[x] + dataset4_combined[x]

# adding titles in bold
dataset1_combined.insert(0, ["\033[1mSector", "SB", "Block", "Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4\033[0m"])

# creating the table
table = tabulate(dataset1_combined, headers="firstrow", tablefmt="rounded_grid")

# we are done
print(table)
