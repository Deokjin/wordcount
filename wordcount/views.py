from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, "about.html")

def result(request):
    text = request.GET['fulltext'] #fulltext로 이름 붙은 폼의 데이터를 text라는 변수에 넣은 것/원문 전체가 담긴다
    words = text.split() #text라는 변수를 공백 기준으로 잘라서 리스트로 만든다공백을 기준으로 나눈다
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] +=1 #word키의 value에 1을 더해라
        else :
            word_dictionary[word] = 1
    return render(request, "result.html", {'full' : text, 'total':len(words), "dictionary" : word_dictionary.items()})  #render는 세번 째 값을 받는데
                                                #key값 value값 나눠서 사전형 객체

