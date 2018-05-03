import collections
import pandas as pd
import matplotlib.pyplot as plt

file = open('PrideandPrejudice.txt',encoding='utf-8')
a=file.read()
# stopwords
stopwords=set(line.strip() for line in open('stopwords.txt'))
stopwords=stopwords.union(set(['mr','mrs','one','tow','said']))
wordcount={}
for word in a.lower().split():
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace(":", "")
    word = word.replace("\"", "")
    word = word.replace("!", "")
    word = word.replace("â€œ", "")
    word = word.replace("â€˜", "")
    word = word.replace("*", "")
    word = word.replace("\?", "")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word]=1
        else:
            wordcount[word]+=1
#print the most common words
n_print = int(input("How many most common words to print: "))
print("OJBK. The %d most common words are as follows\n" % n_print)
word_counter=collections.Counter(wordcount)
for word,count in word_counter.most_common(n_print):
    print(word,":",count)
#close the file
file.close()
#plot
lst=word_counter.most_common(n_print)
df= pd.DataFrame(lst, columns=['Word','Count'])
df.plot.bar(x='Word',y='Count')
plt.show()