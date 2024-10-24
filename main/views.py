from django.http import HttpResponse
from django.shortcuts import render
from .forms import PromptForm
from .api_client import post_data


def check_status(request):
    return HttpResponse(status=200)


def index(request):
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data.get('prompt')
            print(prompt)
            api_url = "https://api.metisai.ir/api/v1/chat/session/94df69b6-d097-42cc-9293-c87a254f11c7/message"  # Replace with actual POST endpoint
            headers = { "Authorization" : "tpsg-NQ0pyhU50rjz2968KkpMieosIvLjl1K" , 
                       "Content-Type" : "application/json"}
            data = {"message":{
                "content":f"{prompt}",
                "type":"USER"
                    }}  
            response_data = post_data(api_url, data , headers=headers)
            print(response_data["content"])
    else:
        form = PromptForm()
    return render(request, "index.html", {"form" : form})
    