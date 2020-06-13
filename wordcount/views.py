from django.shortcuts import render
from collections import Counter
# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    text=request.GET["fulltext"]
    sentences=text.split('.')
    words=text.split()
    word_dictionary={}
    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    a = Counter(words)
    return render(request, 'result.html', {'full':text, 'total_words':len(words), 'total_sentences':len(sentences), 'dictionary': word_dictionary.items(), 'b':a.most_common(5)})
    