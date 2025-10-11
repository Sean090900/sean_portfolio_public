# Huffman Encoder
Created By: Sean Dickson

IDE Used: Visual Studio Code

Python Version: 3.13.0

## Overview
explain what this is, and that it runs as a python module

add cloning info from github?

## Running
Steps for running this package:
1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
4. Run the program as a module: `python -m huffmanEncoder <"encode"/"decode"> <in_file> <out_file> <frequency_table_file>`

Output will be written to the specified output file after processing the input file.

## Usage

For encoding clear text:
```bash
python -m lab3 encode in_file out_file frequency_table_file
```

For decoding encoded text: 
```bash
python -m lab3 decode in_file out_file frequency_table_file
```

**Positional arguments:**

|Argument                      |Description                                        |
|------------------------------|---------------------------------------------------|
|"encode" / "decode"           |Tells the package what task is being done          |
|in_file                       |Input File Path Name                               |
|out_file                      |Output File Path Name                              |
|frequency_table_file          |Frequency Table Pathname                           |

