import pickle
import numpy as np

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter


SLACK_TOKEN = "xoxb-522539944562-736199143463-qmmUPNK1nQVNFCj5P2SLtTsK"
SLACK_SIGNING_SECRET = "57ff273e36cc95d388b9a7746414b4bc"

app = Flask(__name__)

slack_events_adaptor = SlackEventAdapter(SLACK_SIGNING_SECRET, "/listening", app)
slack_web_client = WebClient(token=SLACK_TOKEN)

# Req. 2-1-1. pickle로 저장된 model.clf 파일 불러오기
lrmodel=pickle.load(open('model.clf','rb'))
beta_0 = lrmodel.coef_[0]
beta_1 = lrmodel.coef_[1]
beta_2 = lrmodel.coef_[2]
beta_3 = lrmodel.intercept_

# Req. 2-1-2. 입력 받은 광고비 데이터에 따른 예상 판매량을 출력하는 lin_pred() 함수 구현
def lin_pred(test_str):
    test_str=test_str.split(' ')
    return float(test_str[1])*beta_0+float(test_str[2])*beta_1+float(test_str[3])*beta_2+beta_3

# 챗봇이 멘션을 받았을 경우
@slack_events_adaptor.on("app_mention")
def app_mentioned(event_data):
    channel = event_data["event"]["channel"]
    text = event_data["event"]["text"]

    keywords = lin_pred(text)
    slack_web_client.chat_postMessage(
        channel=channel,
        text=keywords
    )

@app.route("/", methods=["GET"])
def index():
    return "<h1>keroBot 출동 준비완료!!</h1>"

if __name__ == '__main__':
    app.run()
