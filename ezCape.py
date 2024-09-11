from requests import get, post
from base64 import b64decode
from PIL import Image
from io import BytesIO

 
def base64_to_image(base64_string):
    image_data = b64decode(base64_string)
    image = Image.open(BytesIO(image_data))
    return image

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

captcha = get("https://supportreportpost.minecraft.net/api/ReportPost/challenge?challengeType=visual", headers=headers)
captcha = captcha.json()
id = captcha["challengeId"]
image = captcha["content"] # 验证码图片，base64

image = base64_to_image(image)
image.show()  # 显示图片

answer = input("Enter captcha: ")
email = input("Enter your email: ")
name = input("Enter your name: ")
cape = input("Enter cape name(find name on https://namemc.com/capes): ")

#answer = "xxxx" # 用户的验证码输入
#email = "test@test.com" # 用户输入的邮箱
#name = "test" # 用户输入的名字
#cape = "MCC 15th Year" # 披风名，实际使用按需修改
body = f"""Dear Minecraft Support,

I am writing to formally appeal regarding my Java Edition Minecraft account. I have not received the {cape} Cape as promised, despite being eligible for this reward.

I kindly request that you investigate this matter and ensure that the {cape} Cape is correctly issued to my account. If any additional information or verification is required from my end, please let me know, and I will be happy to provide it.

Thank you for your attention to this issue. I look forward to a prompt resolution.

Sincerely,
{name}""" # 文案，请按需修改

headers['Content-Type'] = 'application/json'
params = {
    "request": {
        "subject": " Content Questions",
        "brand_id": 360002579011,
        "comment": {
            "body": body
        },
        "requester": {
            "email": email,
            "name": name
        },
        "custom_fields": [
            {
                "id": 114102530251,
                "value": None
            },
            {
                "id": 114102530311,
                "value": None
            },
            {
                "id": 114102530331,
                "value": None
            },
            {
                "id": 9461201633165,
                "value": None
            },
            {
                "id": 360042941731,
                "value": None
            },
            {
                "id": 1900001985267,
                "value": None
            },
            {
                "id": 8470766104333,
                "value": None
            },
            {
                "id": 360048203131,
                "value": None
            },
            {
                "id": 360021175712,
                "value": "language_english"
            },
            {
                "id": 360038528912,
                "value": "title_minecraft_java_edition"
            },
            {
                "id": 360038528932,
                "value": "platform_pc"
            },
            {
                "id": 360038528952,
                "value": "category_marketplace_support"
            },
            {
                "id": 360038443091,
                "value": "subject_content_questions"
            },
            {
                "id": 360038443531,
                "value": name
            },
            {
                "id": 360038443551,
                "value": email
            },
            {
                "id": 360038443571,
                "value": email
            },
            {
                "id": 360038443111,
                "value": None
            },
            {
                "id": 360038443131,
                "value": None
            },
            {
                "id": 360038529032,
                "value": name
            },
            {
                "id": 360038529092,
                "value": None
            },
            {
                "id": 360038529172,
                "value": None
            },
            {
                "id": 360038529192,
                "value": None
            },
            {
                "id": 360038443691,
                "value": body
            },
            {
                "id": 114102530211,
                "value": " Content Questions"
            },
            {
                "id": 114102530231,
                "value": body
            },
            {
                "id": 360029526951,
                "value": None
            },
            {
                "id": 360029526931,
                "value": None
            },
            {
                "id": 360043133692,
                "value": None
            },
            {
                "id": 360038509031,
                "value": None
            },
            {
                "id": 1900002448427,
                "value": None
            },
            {
                "id": 6619843432205,
                "value": None
            },
            {
                "id": 6619954559117,
                "value": None
            },
            {
                "id": 11395135170189,
                "value": None
            },
            {
                "id": 14712310436621,
                "value": None
            },
            {
                "id": 29476285692685,
                "value": None
            }
        ],
        "ticket_form_id": 360001225811
    },
    "ChallengeId": id,
    "InputSolution": answer,
    "AzureRegion": "EastUS",
    "ChallengeType": "visual"
} # 请按需修改

response = post("https://supportreportpost.minecraft.net/api/reportpost/help/create-ticket", json=params, headers=headers)
if response.status_code == 200:
    print("申诉成功")
else:
    print("申诉失败")
