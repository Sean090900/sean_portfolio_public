# Huffman Encoder
Created By: Sean Dickson
IDE Used: Visual Studio Code
Python Version: 3.13.0

## Overview
explain what this is, and that it runs as a python module
add cloning info fro github?

## Running Huffman Encoder Module
Steps for running this package:
1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
4. Run the program as a module: `python -m lab3 <"encode"/"decode"> <in_file> <out_file> <frequency_table_file>`

Output will be written to the specified output file after processing the input file.

### Huffman Encoder Usage:
```commandline
usage (for encoding clear text): python -m lab3 encode in_file out_file frequency_table_file
usage (for decoding encoded text): python -m lab3 decode in_file out_file frequency_table_file

positional arguments:
  "encode" / "decode"           Tells the package what task is being done
  in_file                       Input File Pathname
  out_file                      Output File Pathname
  frequency_table_file          Frequency Table Pathname
```
