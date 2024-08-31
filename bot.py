import random
import asyncio

from pyrogram import Client

from chat_list.chats import chats_1, chats_2, chats_3
from message_list.messages import message_1, message_2, message_3
from config import api_id, api_hash, session_name

app = Client(session_name, api_id=api_id, api_hash=api_hash)


async def send_messages_1():
    while True:
        for chat_id in chats_1:
            try:
                await asyncio.sleep(random.randint(9 ,12))
                await app.send_message(chat_id, message_1, reply_to_message_id=20)
                print(f"Сообщение об услугах рассылки {chat_id}")
            except Exception as e:
                print(f"Ошибка при отправке первого сообщения в чат {chat_id}: {e}")
            await asyncio.sleep(random.randint(9, 12))


async def send_messages_2():
    while True:
        for chat_id in chats_2:
            try:
                await asyncio.sleep(random.randint(9,12))
                await app.send_message(chat_id, message_2, reply_to_message_id=20)
                print(f"Сообщение об услугах залива трафика {chat_id}")
            except Exception as e:
                print(f"Ошибка при отправке второго сообщения в чат {chat_id}: {e}")
            await asyncio.sleep(random.randint(9, 12))


async def send_messages_3():
    while True:
        for chat_id in chats_3:
            try:
                await asyncio.sleep(random.randint(9, 12))
                await app.send_message(chat_id, message_3, reply_to_message_id=20)
                print(f"Сообщения о пиаре биржы рекламе {chat_id}")
            except Exception as e:
                print(f"Ошибка при отправке третьего сообщения в чат {chat_id}: {e}")
            await asyncio.sleep(random.randint(9, 12))


async def main():
    async with app:
        task_1 = asyncio.create_task(send_messages_1())
        task_2 = asyncio.create_task(send_messages_2())
        task_3 = asyncio.create_task(send_messages_3())
        await asyncio.gather(task_1, task_2, task_3)


asyncio.run(main())
