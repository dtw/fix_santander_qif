# regex functions
import re

# this function just counts how many lines in the file
def bufcount(filename):
    f = open(filename)                  
    lines = 0
    buf_size = 1024 * 1024
    read_f = f.read # loop optimization

    buf = read_f(buf_size)
    while buf:
        lines += buf.count('\n')
        buf = read_f(buf_size)

    return lines

# this pattern matches lines starting with P
p_Pline = re.compile('^P')
# this pattern matches everything after the first comma
p_trim = re.compile(',[^\n]*')

# this is a dictionary of patterns to match and substitutions 
qif_subs = {"DIRECT DEBIT PAYMENT": "DD",
    "CARD PAYMENT TO ": "",
    "STANDING ORDER VIA FASTER PAYMENT": "SO",
    "&amp;" : "&",
    "FASTER PAYMENTS RECEIPT" : "FP REC.",
    "BILL PAYMENT VIA FASTER PAYMENT": "FP"}

# get the output fiel ready
o_file = open('Y:\out.qif', 'w')
# open the input file
with open("Y:\in.qif", 'r') as i_file:
    # read it line by line
    for line in i_file:
        # does the line start with P?
        if p_Pline.match (line):
            # match p_trim for each line and replace with '' - i.e. nothing
            temp = (p_trim.sub ('',line))
            # for each pair in our dictionary
            for target, sub in qif_subs.items():
                # create a new pattern from the dictionary key
                temp_p = re.compile(target)
                # match that pattern and replace with the corresponding value from the dictionary
                temp = temp_p.sub(sub,temp)
            # write the line to the output file
            o_file.write(temp)
        # no, so just write it the output file
        else:
            o_file.write(line)

o_file.close()
print(bufcount("Y:\in.qif"))
print(bufcount("Y:\out.qif"))
