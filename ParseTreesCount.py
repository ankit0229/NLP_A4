import re
import nltk
import sys
import pickle
from collections import Counter
from nltk.tree import Tree
Picklefile1 = open('DictProd', 'rb')
all_possib = pickle.load(Picklefile1)

fp = open(r"C:\Users\ANKIT\PycharmProjects\Assign_CKY\TestSent.txt","r",encoding="utf8")
text = fp.read()
sentences = text.split("\n")
#print(sentences)
for s1 in sentences:
    sent = s1.split(" ")
    len_sent = len(sent)
    table = [[[[],{}] for i in range(len_sent+1)] for j in range(len_sent+1)]
    all_lhs = []
    dict_ptr = {}
    for j in range(1, len_sent+1):
        word = sent[j-1]
        m = '\''
        word = m + word + m
        lhs1 = all_possib.get(word)
        if lhs1 is not None:
            table[j - 1][j][0].extend(lhs1)
            for pre_ter in lhs1:
                prs = []
                t = Tree(pre_ter,[word])
                prs.append(t)
                table[j - 1][j][1][pre_ter] = prs
        for i in range(j-2,-1,-1):
            all_lhs = []
            for k in range(i+1,j):
                B = table[i][k][0]
                C = table[k][j][0]
                len_b = len(B)
                len_c = len(C)
                for x in range(len_b):
                    b = B[x]
                    for y in range(len_c):
                        c = C[y]
                        pair = (b,c)
                        lhs2 = all_possib.get(pair)
                        if lhs2 is not None:
                            all_lhs.extend(lhs2)
                            for non_term in lhs2:
                                nt1 = table[i][k][0][x]
                                nt2 = table[k][j][0][y]
                                temp_dict1 = table[i][k][1]
                                tree_ls1 = temp_dict1[nt1]
                                temp_dict2 = table[k][j][1]
                                tree_ls2 = temp_dict2[nt2]
                                temp_dict3 = table[i][j][1]
                                if temp_dict3.get(non_term) is not None:
                                    prs = []
                                    t1 = tree_ls1
                                    t2 = tree_ls2
                                    for tr1 in t1:
                                        for tr2 in t2:
                                            t = Tree(non_term, [tr1, tr2])
                                            prs.append(t)
                                    temp_dict3[non_term].extend(prs)
                                else:
                                    prs = []
                                    t1 = tree_ls1
                                    t2 = tree_ls2
                                    for tr1 in t1:
                                        for tr2 in t2:
                                            t = Tree(non_term, [tr1, tr2])
                                            prs.append(t)
                                    temp_dict3[non_term] = prs

            if len(all_lhs) != 0:
                dict_all_lhs = Counter(all_lhs)
                all_lhs = []
                for q in dict_all_lhs:
                    all_lhs.append(q)
                table[i][j][0].extend(all_lhs)

    final = table[0][len_sent][1]
    no_parse = final.get('SIGMA')
    prs_count = 0
    if no_parse is not None:
        prs_count = len(no_parse)
    fp = open(r"C:\Users\ANKIT\PycharmProjects\Assign_CKY\CalculatedParseTrees.txt", "a")
    prs_count = str(prs_count)
    for w in sent:
        fp.write(w + " ")
    fp.write("\t")
    fp.write(prs_count)
    fp.write("\n")
fp.close()
print("File successfully written")