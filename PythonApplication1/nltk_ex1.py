'''from nltk.book import *'''
import nltk
import math
import numpy

def main():
    print("hi")

'''
Open a text file, tokenize and return an nltk.Text object
'''
def open_textfile(fname):
    f = open(fname, 'r')
    raw_text = f.read()
    tokens = nltk.word_tokenize(raw_text)
    text = nltk.Text(tokens)
    
    return text

'''
Get the n most common words from a given text
text -> nltk.Text object
'''
def get_n_most_common_words(text, n):
    fdist = nltk.FreqDist(text) # creates a frequency distribution from a list
    most_commons = fdist.most_common(n)
    return most_commons

'''
Remove the n most common words from a given text
text -> nltk.Text object
'''
def remove_most_common(text, n):
    # get the frequency distribution for the input text
    fdist = nltk.FreqDist(text)
    most_common_words = fdist.most_common(n)
    most_common = [w[0] for w in most_common_words]
    ret_text = [word for word in text if word not in most_common]
    return nltk.Text(ret_text)

'''
Remove the n less common words from a given text
text -> nltk.Text object
'''
def remove_less_common_words(text, n):
    # get the frequency distribution for the input text
    fdist = nltk.FreqDist(text)
    most_common_words = fdist.most_common(len(text))
    most_common_words.sort(key=lambda x: x[1])
    most_common_words = most_common_words[0:n-1]
    most_common = [w[0] for w in most_common_words]
    ret_text = [word for word in text if word not in most_common]
    return nltk.Text(ret_text)

'''
Calculate the shannon information entropy for the specified text, and
returns a list of word ordered by information entropy
text -> nltk.Text object
'''
def calculate_text_entropy(text):
    # get the frequency distribution for the input text
    fdist = nltk.FreqDist(text)
    # get the text lenght
    words_count = len(set(text))
    # initialize the output list, that is, the most relevant words
    output_list = []

    # iterate each word
    for parola in set(text):
        # get the word frequency within the text (== Pwi)
        freq_word = fdist.freq(parola)
        # calculate the information quantity
        information = -(freq_word * math.log(freq_word))
        # append the couple word-information to the output list
        output_list.append([parola,information])
    
    # sort the output list by the information quantity in reverse order
    output_list.sort(key=lambda x: x[1], reverse=True)
    return output_list


def esercizio(text):
    # get the frequency distribution for the input text
    fdist = nltk.FreqDist(set(text))

    dict = []
    for parola in set(text):
        # get the word frequency within the text
        dict.append([w,fdist.freq(parola)])



def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * (count / total)

def jakkard(d1,d2):
    return len(set(d1).intersection(d2)) / len(set(d1).union(d2))

'''
Calculate the Jakkard distance between all the documents in the input list
testi -> list of nltk.Text objects
'''
def jakkard_distance(testi):
    coppie = [[i,j] for i in testi for j in testi]
    coefficienti = []
    for coppia in coppie:
        j = jakkard(coppia[0],coppia[1])
        if(j < 1):
            coefficienti.append([coppia[0],coppia[1],j])
    coefficienti.sort(key=lambda x: x[2])
    return coefficienti


if __name__ == "__main__":
    '''main()'''
    txt = open_textfile('C:\promessi_sposi.txt')

    cleaned_text = remove_most_common(text, 100)
    re_cleaned_text = remove_less_common_words(cleaned_text, 100)



    print(re_cleaned_text)
    #cleaned = calculate_text_entropy(txt)
    #print(cleaned)
    
    
    '''lexical_diversity(text3)
    lexical_diversity(text5)
    percentage(4,5)
    percentage(text4.count('a'),len(text4))'''
