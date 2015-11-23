import sys;
import re;

equa = sys.argv[1];
print(equa);
matching = re.findall(r'\d* \* X\^\d', equa, re.I);
op = re.findall(r'\d* \* X\^\d ([\-\+\*\/])', equa, re.I);
polynom = re.findall(r'\d* \* X\^(\d)', equa, re.I);

print (matching);
print (op);
print (polynom);
