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
        print(q["query"])
        r = requests.post("https://api.divar.ir/v1/open-platform/finder/post", json={
            "city": "tehran",
            "category": "light",
            "query": dict(q["query"])
            },headers={"Content-Type": "application/json", "x-api-key":"eyJhbGciOiJSUzI1NiIsImtpZCI6InByaXZhdGVfa2V5XzIiLCJ0eXAiOiJKV1QifQ.eyJhcHBfc2x1ZyI6Im1vb3ItaXJvbi1qYWd1YXIiLCJhdWQiOiJzZXJ2aWNlcHJvdmlkZXJzIiwiZXhwIjoxNzM0Nzc5OTM0LCJqdGkiOiI2YzRmM2FlYy05MDY3LTExZWYtYjM1ZS1mYWFiMDYxNzA5ZmMiLCJpYXQiOjE3Mjk1OTU5MzQsImlzcyI6ImRpdmFyIiwic3ViIjoiYXBpa2V5In0.AJSNFlbXsb8y_D1F4D4uTsTg2J_T3r_vOZznfoEwWTFyZJeszEKzZQLNbVDDC7svD_onK0spppBj8dB4JhPwiKiKrU_07Mz_EIyMr_7LhtvT6wTbf8zd8ztrbd3PSeFDwt9otVeP73awP0x18DJq3nSZeUarehS9g0PC-oLU4Fb4WRdvjOUFfDBu0QGV3OT8vbS4TZ17BBRVIKKwfY1zyISsqzAbIQ8vK5mGrncyS5WXDE9ndikLMPgcdmEj87POC-u_cM8iVpS_scLJc0g6ps35yeZafw14hyhiYhluuLTnocQ32PgfvIcYLV7Of7Juf-aiK8W_BQrTVoV5VaGHrQ"})
        r = r.json()["posts"][:5]
        r = clean_posts(r)
        print(f"***{r}***")
        return r
    except Exception as e:
        print(e)
        return
    
