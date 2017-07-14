from wordcloud import WordCloud

filename="tomhanks.txt"
with open(filename,encoding='UTF-8') as f:
    mytext = f.read()
wordcl=WordCloud().generate(mytext)