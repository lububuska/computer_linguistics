
from nltk.corpus import stopwords 
from nltk.tokenize import *

file = open('dataset.txt', 'r', encoding = "utf-8")
text = file.read()
tokens = word_tokenize(text)

stop_words = set(stopwords.words('russian'))

filtered_tokens = [word for word in tokens if word not in stop_words]

with open('lab1_result.txt', 'w', encoding = 'utf-8') as file_result:
    print(filtered_tokens, file = file_result)

file.close()
file_result.close()