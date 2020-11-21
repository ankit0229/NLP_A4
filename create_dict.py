import re
import nltk
import pickle
from collections import Counter

fp = open(r"C:\Users\ANKIT\Desktop\CNF\lang.txt","r",encoding="utf8")
text = fp.read()
productions = text.split("\n")
all_prod = []
#Making a nested list of all productions which contains lists with first element as tuple and the second element
#as a tuple containing the right hand side of the production
c = 1
for prod in productions:
    element = []
    rule = prod.split(" -> ")
    element.append(rule[0])
    rhs = rule[1]
    rhs = rhs.split(" ")
    if len(rhs) == 1:
        x = rhs[0]
        terminal = (x,)
        element.append(terminal)
    elif len(rhs) == 2:
        pair = (rhs[0],rhs[1])
        element.append(pair)
    all_prod.append(element)

all_terminals = []
for x in all_prod:
    y = x[1]
    if len(y) == 1:
        all_terminals.append(y[0])

dict_terminals = Counter(all_terminals)

unique_terminals = []
for k in dict_terminals:
    unique_terminals.append(k)

print(len(unique_terminals))

#Now making list of all binaries of all productions with binaries on RHS
all_binaries = []
for x in all_prod:
    y = x[1]
    if len(y) == 2:
        all_binaries.append(y)
dict_binaries = Counter(all_binaries)
unique_binaries = dict_binaries.keys()
print(len(unique_binaries))

all_possib = {}
for t in all_terminals:
    lhs = (t)
    rhs = []
    for p in all_prod:
        m = p[1]
        if len(m) == 1 and m[0] == t:
            rhs.append(p[0])
    dict_temp = Counter(rhs)
    rhs = []
    for k in dict_temp:
        rhs.append(k)
    all_possib[lhs] = rhs

print(len(all_possib))
for b in all_binaries:
    lhs = b
    rhs = []
    for p in all_prod:
        m = p[1]
        if len(m) == 2 and m[0] == b[0] and m[1] == b[1]:
            rhs.append(p[0])
    dict_temp = Counter(rhs)
    rhs = []
    for k in dict_temp:
        rhs.append(k)
    all_possib[lhs] = rhs

for k in all_possib:
    print(k)
    print(all_possib[k])
print(len(all_possib))

Picklefile1 = open('DictProd', 'wb')
pickle.dump(all_possib, Picklefile1)
Picklefile1.close()
print("done")