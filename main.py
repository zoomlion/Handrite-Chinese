#! /usr/bin/env python3

# use fpdf to generate a pdf file from string
# auto shake the font to make it look like real handwriting

import fpdf
import random
import string
import sys
import argparse

non_break_char = [str(i) for i in range(10)] + [',', '.',\
                    '!', '?', ':', ';', '，', '。', '！', '？',\
                    '：', '；', '\"', '\'', '“', '”', '‘', '’', \
                    '（', '）', '(', ')', ' ', '　', '、', '…', '、', \
                    '《', '》', '-', '%']

ascii_letters = string.ascii_letters

def main():
    # get the input string from txt file
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input txt file")
    parser.add_argument("output", help="output pdf file")
    args = parser.parse_args()
    raw_strings = []
    with open(args.input, 'r') as f:
        raw_strings = f.readlines()
    input_strings = ['   ' + s.strip() for s in raw_strings]
    pdf = fpdf.FPDF('P', 'mm', 'A4')
    pdf.add_font('Handwriting', '', '陈静的字.ttf', uni=True)
    pdf.set_font('Handwriting', '', 20)
    pdf.add_page()
    # make font spacing randomly smaller to make it more like handwriting
    # and set auto line feed
    pdf.set_auto_page_break(True, 10)

    # place y axis to 30mm
    pdf.set_y(30)
    
    # reomve the first line of input string
    input_strings = input_strings[1:]

    for s in input_strings:
        for c in s:
            # auto split the string to fit the page, max string number in one line is 40
            # generate pdf file, and use specific font file (ttf format) to render pdf file
            if c in non_break_char:
                pdf.set_x(pdf.get_x() + 0.5*random.randint(-2, -1))
                pdf.set_font_size(12 + random.randint(-1, 1))
                pdf.cell(4 + 0.1*random.random()*random.randint(-1, 1), 10, c, 0, 0, 'C', 0, '')
                pdf.set_x(pdf.get_x() + 0.5*random.randint(-2, -1))
                continue
            if c in ascii_letters:
                pdf.set_x(pdf.get_x() - .2 + 0.3*random.randint(-2, -1))
                pdf.set_font_size(20 + random.randint(-1, 1))
                pdf.cell(4 + 0.1*random.random()*random.randint(-1, 1), 10, c, 0, 0, 'C', 0, '')
                pdf.set_x(pdf.get_x() + 0.5*random.randint(-2, -1))
                continue
            if pdf.get_x() > 190 + random.randint(-5, 2):
                pdf.ln()
                pdf.set_x(10)
                pdf.set_y(pdf.get_y() + random.random() * random.randint(-1, 1))
            pdf.set_font_size(20 + random.randint(-2, 2))
            pdf.cell(6 + 0.2*random.random()*random.randint(-1, 1), 10, c, 0, 0, 'C', 0, '')
            pdf.set_font('Handwriting', '', 20 + random.randint(-2, 2))
            pdf.set_x(pdf.get_x() + 0.2*random.random()*random.randint(-1, 1))
        pdf.ln()
        pdf.set_y(pdf.get_y() + random.random() * random.randint(-4, 4))
    pdf.output(args.output, 'F')


if __name__ == '__main__':
    main()
