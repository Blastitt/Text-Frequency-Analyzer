# Text-Frequency-Analyzer
A simple letter frequency analyzer written in python.

## What is it?
The script will read through all files in the specified directory. 
It analyzes the frequency of single letters, letter pairs, and letter triplets.
For multi-letter analysis, the script will backtrack to analyze all adjacent letter combinations.
>**For Example**:

>`abcdefghij` will be interpreted as

>Single: a, b, c, d, etc.

>Pairs: ab, bc, cd, etc.

>Triplets: abc, bcd, cde, etc.

It will output three CSV files containing information about single letter, pair, and triplet frequency.
The files will all have the same name (specified by you) prepended with `SINGLE-`, `PAIRS-`, or `TRIPLETS-`.
The output will contain the **total number of files scanned**, the **total number of patterns scanned**, and **newline delimited,
comma separated key/value pairs** of each pattern and its frequency.
>**For Example**:

>Total Files: 1

>Total Pairs: 107664

>JU,147

>GW,1

>GU,152

>GT,1

>GS,83

>GR,139

>GY,17

>..........

The analyzer recognizes the English alphabet, ü, ö, ä, and ñ.
It does not account for letter case (everything is considered uppercase), whitespace, punctuation, or any other characters.

## Setup
Put all text files you wish to analyze in a directory of your choosing.

## Usage
`$ python textParse.py <directory containing text files> <output file name>`

