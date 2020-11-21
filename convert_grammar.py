import nltk
grammar = nltk.data.load("grammars/large_grammars/atis.cfg")
grammar = nltk.CFG.binarize(grammar, padding = '$')
gr = nltk.CFG.remove_unitary_rules(grammar)
print(gr)