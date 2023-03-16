import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="xoxb-4693014614277-4927023407137-FTwmE9FmPcts1MftyuJEodXV")

def send_message():
    try:
        message = "<!channel> 데일리 스크럼 작성해주세요! :rocket:"

        response = client.chat_postMessage(channel="#업무", text=message)
        print(f"메시지 전송 성공: {response['ts']}")
    except SlackApiError as e:
        print(f"메시지 전송 실패: {e.response['error']}")

if __name__ == '__main__':
    send_message()