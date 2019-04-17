
# -*- coding: utf-8 -*-

"""
    A Simple Python Script to Manage EPD Databases,
    Removing identical replicate FEN Positions, despite
    differing op codes, such as id or comments c0..c9, etc...
    
    This script was written by Ferdinand Mosca (AKA Ferdy),
    and can be found in this talkchess thread:
    http://talkchess.com/forum3/viewtopic.php?f=2&t=66853&p=795814#p795813
    
    Please note, that this script prioritizes positions by order of occurance.
    For this reason, I sort the epd file, by line length apriori using
    a simple perl expression in terminal:
    perl -e 'print sort { length($b) <=> length($a) } <>' input.epd > output.epd
    
    Requirements:
    Python 3
    
"""

import argparse

VERSION = 'v0.1.0'


def main():
    parser = argparse.ArgumentParser(prog='Identical epd remover {}'.format(VERSION))
    parser.add_argument('-i', '--input', help='input epd filename',
                        required=True)
    parser.add_argument('-o', '--output', help='output filename, overwrite mode',
                                            required=True)
                        
    args = parser.parse_args()
    epdfn = args.input
    outfn = args.output
                        
    tmp_save = []
    uni_save = []
                        
    # Read input epd and remove identical, consider first entry as priority
    with open(epdfn, 'r', encoding='utf-8', errors='ignore') as f:
        for lines in f:
            line = lines.strip()
                            
            base_epd = ' '.join(line.split()[0:4]).strip()
            if base_epd not in tmp_save:
                tmp_save.append(base_epd)
                uni_save.append(line)

    # Write to output file
    with open(outfn, 'w', encoding='utf-8', errors='ignore') as f:
        for epd_line in uni_save:
            f.write('{}\n'.format(epd_line))


if __name__ == '__main__':
    main()
