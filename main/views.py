from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import CustomUser
from .api_client import *
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import random
import datetime
from django.contrib.auth import login
from ast import literal_eval
from .send_sms import *


def check_status(request):
    return HttpResponse(status=200)

@login_required
def index(request):
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data.get('prompt')
            print(prompt)
            # تحلیل کننده پرامپت
            api_url = "https://api.metisai.ir/api/v1/chat/session/6e2377f5-1985-4c81-95e7-b9836b02cf45/message"
            headers = { "Authorization" : "tpsg-NQ0pyhU50rjz2968KkpMieosIvLjl1K" , 
                       "Content-Type" : "application/json"}
            data = {"message":{
                "content":f"{prompt}",
                "type":"USER"
                    }}  
            response_data = post_data(api_url, data , headers=headers)
            print(response_data["content"])
            #next request to metis
            api_url2 = "https://api.metisai.ir/api/v1/chat/session/8135fbaa-0ae8-48c4-a9ca-b32db9d0e885/message"
            data2 = {"message":{
               "content":f'{get_posts(literal_eval(response_data["content"]))}\nآیا در آگهی های بالا آگهی متناسب با ویژگی های "{prompt}" وجود داره؟',
               "type":"USER"
                   }}
            print(data2)
            response_data_final_result = post_data(api_url2, data2 , headers=headers)
            response_final = literal_eval(response_data_final_result["content"])
            print(response_data_final_result["content"])
            if response_final["status"] == 200:
                print(f"https://divar.ir/v/{response_final["token"]}")
                print(request.user.phone)
                sendMessange(f"https://divar.ir/v/{response_final["token"]}", str(request.user.phone))

    else:
        form = PromptForm()
    return render(request, "index.html", {"form" : form})
    
def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            try:
                user = CustomUser.objects.get(phone=phone)
                if int(user.max_otp_try) == 0 and user.otp_max_out and timezone.now() < user.otp_max_out:
                    return HttpResponse("Max OTP try reached, try after an hour", status=400)
                otp = random.randint(1000, 9999)
                otp_expiry = timezone.now() + datetime.timedelta(minutes=10)
                max_otp_try = int(user.max_otp_try) - 1
                user.otp = otp
                user.otp_expiry = otp_expiry
                user.max_otp_try = max_otp_try
                if max_otp_try == 0:
                    otp_max_out = timezone.now() + datetime.timedelta(hours=1)
                elif max_otp_try == -1:
                    user.max_otp_try = 3
                else:
                    user.otp_max_out = None
                    user.max_otp_try = max_otp_try
                    user.save()
                    print(user.otp, 'OTP', user.phone)
                    send_otp(user.phone, otp)
                    return redirect("otp")
            except ObjectDoesNotExist:
                user_ = CustomUser.objects.create(phone=phone)
                otp = random.randint(1000, 9999)
                otp_expiry = timezone.now() + datetime.timedelta(minutes=10)
                max_otp_try = int(user_.max_otp_try) - 1
                user_.otp = otp
                user_.otp_expiry = otp_expiry
                user_.max_otp_try = max_otp_try
                if max_otp_try == 0:
                    otp_max_out = timezone.now() + datetime.timedelta(hours=1)
                elif max_otp_try == -1:
                    user_.max_otp_try = 3
                else:
                    user_.otp_max_out = None
                    user_.max_otp_try = max_otp_try
                    user_.is_passenger = True
                    user_.save()
                    send_otp(user_.phone, otp)
                    return redirect("otp")
        else:
            return HttpResponse("Phone number is incorrect", status=401)
    else:
        form = LoginForm
    return render(request, "login.html", {"form":form})

def verifyOTPView(request):
    if request.method == 'POST':
        form = VerifyOTPForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data.get('otp')
            user = CustomUser.objects.get(otp=otp)
            if user:
                login(request, user)
                user.otp = None
                user.otp_expiry = None
                user.max_otp_try = 3
                user.otp_max_out = None
                user.save()
                return redirect("index")
            else:
                return HttpResponse("Please enter the correct OTP", status=400)
    else:
        form = VerifyOTPForm()
    return render(request, "otp.html", {"form":form})
