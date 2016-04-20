from nltk.book import *

def main():
    print('hi')

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * (count/total)

def jakkard(d1,d2):
    return len(set(d1).intersection(d2)) / len(set(d1).union(d2))

def esercizio_jakkard(testi):
    coppie = [[i,j] for i in testi for j in testi];
    coefficienti = []
    for coppia in coppie:
        j = jakkard(coppia[0],coppia[1])
        if(j < 1):
            coefficienti.append([coppia[0],coppia[1],j])
    coefficienti.sort(key=lambda x: x[2])
    return coefficienti


if __name__ == "__main__":
    '''main()'''
    lexical_diversity(text3)
    lexical_diversity(text5)
    percentage(4,5)
    percentage(text4.count('a'),len(text4))
