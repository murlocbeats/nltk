import requests
import json

# URL API که درخواست به آن ارسال می‌شود
url = 'https://nltk-beta.vercel.app/analyze'

# داده‌هایی که باید به API ارسال شود
data = {
    'text': 'I love programming!'
}

# ارسال درخواست POST به API
response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))

# دریافت و چاپ پاسخ
if response.status_code == 200:
    print('Response:', response.json())
else:
    print('Failed to get a response. Status code:', response.status_code)
    print('Response:', response.text)
