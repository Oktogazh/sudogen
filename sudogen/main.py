from sudogen import load_dictionary


def main():
    # load a spylls (huspell) dictionary class
    # lemma still need to be extracted
    dictionary = load_dictionary()
    lemmas = [word.stem for word in dictionary.dic.words]
    print(lemmas)
