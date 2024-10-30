import requests
from kavenegar import *


#sending the user prompt
def post_data(api_url, data, headers):
    try:
        response = requests.post(api_url, json=data, headers=headers)  # Posting data as JSON
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def clean_posts(posts):
    for r in posts:
        r.pop('business_type', None)
        r.pop('city', None)
        r.pop('last_modified', None)
        r.pop('platform_data', None)
        r.pop('published_at', None)
        r["post_data"].pop('coordination_type', None)
        r["post_data"].pop('district', None)
        r["post_data"].pop('effective_location', None)
        r["post_data"].pop('exchange', None)
        r["post_data"].pop('fuel_type', None)
        r["post_data"].pop('gearbox', None)
        r["post_data"].pop('description', None)
        r["post_data"].pop('category', None)
        r["post_data"].pop('images', None)
    return posts
def get_posts(q):
    try:
        r = requests.post("https://api.divar.ir/v1/open-platform/finder/post", json={
            "city": "tehran",
            "category": "light",
            "query": dict(q["query"])
            },headers={"Content-Type": "application/json", "x-api-key":"eyJhbGciOiJSUzI1NiIsImtpZCI6InByaXZhdGVfa2V5XzIiLCJ0eXAiOiJKV1QifQ.eyJhcHBfc2x1ZyI6ImdyZWF0LXdhbG51dC1nb29zZSIsImF1ZCI6InNlcnZpY2Vwcm92aWRlcnMiLCJleHAiOjE3MzUzMjMxMjAsImp0aSI6IjIwNmU5ZmIyLTk1NTgtMTFlZi05YmY5LTVlZGI4OGNiMjZmMiIsImlhdCI6MTczMDEzOTEyMCwiaXNzIjoiZGl2YXIiLCJzdWIiOiJhcGlrZXkifQ.P_eN4cfWlONgOD6ZLkXTsruN1bUHtHiNf8UmdynJvlha3vIwc0ybua6aHNCQnScjsGYjIOKdr0LbCwA_501MI8tbi0kBaRT-xkaREFuCvbWgt3WyYKocncaIslfVHljF8xefFFb33Hgqt1zW5B4FVpnb3PJ_cE_13-3QFZJfN5iqCDKtqB-f_HEmbzvj8c0ckXYcMD3u9fuS0uMBT-92QGij2DBajgdiN4ovf4XCS-qK5-PaLqOwBFkCQKe-oEZwbYloJrFYtTf_hLA4UG_0YwCOUR1Nem6z4kNGm9rIfP6jtaUVOiFwRB79-SsEyqqUdLso85C78ucMjsVujpLciA"})
        r = r.json()["posts"][:5]
        r = clean_posts(r)
        return r
    except Exception as e:
        print(e)
        return
    
