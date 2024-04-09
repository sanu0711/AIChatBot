from django.shortcuts import render
from django.http import HttpResponse
import google.generativeai as gai
from chatHistory.models import ChatInteraction
def modelBot(userinput):
    api_key='AIzaSyCnsw4EI7Hz0DrYMhqP0JklYqHm2-0O5p8'
    gai.configure(api_key=api_key)
    model=gai.GenerativeModel('gemini-pro')
    chat=model.start_chat(history=[])
    response=chat.send_message(userinput)
    return response.text

def home(request):
    if request.method == 'POST':
        qus=request.POST.get('user-input')
        res=modelBot(qus)
        dict1={'Question':qus,'Answer':res}
        ChatInteraction.objects.create(question=qus,response=res)
        return render(request, 'home.html',dict1)
    return render(request, 'home.html')
