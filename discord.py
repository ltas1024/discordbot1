import discord
import json
import random

# Discord 봇 클라이언트 생성
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

# 대화 데이터를 저장하고 로드하는 함수
def save_conversations(conversations):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(conversations, f, ensure_ascii=False, indent=4)
pip install --upgrade discord.py
def load_conversations():
    try:
        with open('conversations.json', 'r', encoding='utf-8') as f:
            conversations = json.load(f)
    except FileNotFoundError:
        conversations = []
    return conversations

# 봇이 온라인 상태일 때 실행되는 이벤트 핸들러
@client.event
async def on_ready():
    print(f'로그인 완료: {client.user.name}')

# 사용자 메시지에 대한 응답 처리
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # 대화 데이터 로드
    conversations = load_conversations()

    # 사용자 메시지를 대화 데이터에 추가
    user_message = {
        "user": message.author.name,
        "message": message.content
    }
    conversations.append(user_message)

    # 대화 데이터를 JSON 파일에 저장
    save_conversations(conversations)

    # 봇의 응답 생성
    if message.content.startswith('!학습'):
        if len(conversations) > 1:
            # 대화 데이터에서 사용자 메시지와 봇 응답을 추출
            user_messages = [entry["message"] for entry in conversations if entry["user"] == message.author.name]
            bot_responses = [entry["message"] for entry in conversations if entry["user"] == client.user.name]

            # 여기에서 본인의 대화 생성 로직을 구현해야 합니다.
            bot_response = generate_response(user_messages, bot_responses, message.content)

            await message.channel.send(bot_response)
        else:
            await message.channel.send("학습 데이터가 부족합니다.")

# 여기에서 본인의 대화 생성 로직을 구현해야 합니다.
def generate_response(user_messages, bot_responses, input_message):
    # 간단한 예제: 가장 최근 사용자 메시지를 반복
    if user_messages:
        bot_response = user_messages[-1]
    else:
        bot_response = "아직 학습 데이터가 부족합니다."

    return bot_response

# 봇 토큰으로 봇 로그인
client.run('MTE2MTI3NDU4NDgzNDc3NzE1OQ.G_C7mi.nUkOOELUE49Vl2jgGTUwhklSGlkFh6o5j4RNQ8')