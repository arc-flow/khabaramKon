from celery import shared_task
import requests
from django.conf import settings
from .api_client import *
from .send_sms import sendMessange
import json


@shared_task(bind=True)
def send_http_request(self, query, prompt, phone):
    try:
        headers = { "Authorization" : "tpsg-NQ0pyhU50rjz2968KkpMieosIvLjl1K" , 
            "Content-Type" : "application/json"}
        api_url2 = "https://api.metisai.ir/api/v1/chat/session/8135fbaa-0ae8-48c4-a9ca-b32db9d0e885/message"
        data2 = {"message":{
            "content":f'{get_posts(query)}\nآیا در آگهی های بالا آگهی متناسب با ویژگی های "{prompt}" وجود داره؟',
            "type":"USER"
                }}
        print(data2)
        response_data_final_result = post_data(api_url2, data2 , headers=headers)
        response_final = json.loads(response_data_final_result["content"])
        print(response_data_final_result["content"])
        if response_final["status"] == 200:
            print(f"https://divar.ir/v/{response_final["token"]}")
            sendMessange(f"خبرم کن\nآگهی مناسب شما پیدا شد\nتوکن آگهی : {response_final["token"]}\nمتاسفانه در حال حاضر به دلایل امنیتی در پنل پیامکی امکان ارسال لینک آگهی رو نداریم و فقط میتونیم توکنش رو براتون ارسال کنیم", phone)
            self.retry(countdown=1800, max_retries=4)
        elif response_final["status"] == 400:
            # print("وضعیت 400 است، تسک دوباره اجرا خواهد شد.")
            # برنامه‌ریزی مجدد برای ۱۰ دقیقه بعد
            self.retry(countdown=600, max_retries=12)  # تنظیم تعداد تلاش‌ها به دلخواه
        else:
            print("وضعیت غیر منتظره‌ای دریافت شد.")
    except requests.exceptions.RequestException as e:
        print(f"خطا در درخواست: {e}")
        # برنامه‌ریزی مجدد برای ۱۰ دقیقه بعد
        self.retry(countdown=600, max_retries=6)
