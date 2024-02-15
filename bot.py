# импорты не трогаем
import discord
import asyncio
import random
import os
import time
import aiohttp
import json
import requests
from discord.ext import commands

# конфиг
token = "OTg1NzcwODc4OTEyNTYxMTkz.G5irK1.reu1NhLPOuwxVNrvi0LlaAYFa0l7brzObPTkWk" # токен бота на всякие случаи ставим в token.txt
bot = commands.Bot(command_prefix='') # для чат ботов ненужен префикс если он будет без команд если хотите с командами ищите как сделать команды в боте я делал чат бота команды ненужны мне для него
bot.remove_command('help') # убрать перво-начальный хелп

# переменные для бота чтобы от отвечал можно использовать интернет не покажу других персонажей чтобы не затянуть видео
shelly = ["Пошли за ним", "Давайте сделаем это!", "Ха-ха!", "Золотце!", "Невероятно!", "Фантастика!", "Да!", "Ю-пи!", "Ву-ху"]
colt = ["Берегись, я иду!", "Я слишком хорош!", "Номер один!", "Прости, нуб.", "Какой хедшот!", "Да!"]
nita = ["Нита..!", "Да-а-а..!", "Мишка-а..!"]
bull = ["Эй, я здесь козырь!", "Не связывайся с Буллом!", "Тебе лучше в этом у-Булл-иться!", "И не вставай!", "Ты попал в меня...", "Буллдозее-ер!"]
dinamike = ["Я взрывоопасен!", "Птички поют.", "Кому еще тротила?", "Я сержусь.", "Прямо в карьер!"]
jessie = ["Джесс починит!", "Я номер один!", "Нет!", "Ха-ха-ха!", "Строю!"]
vosembit = ["Игрок ПЕРВЫЙ, будь ГОТОВ!", "Новый РЕКОРД!", "Игра НЕ окончена", "Иди к на-ам! Ням-ням!"]
emz = ["Посмотри на меня!.. Да не так!", "И я упс…", "OMG, ты так плох!", "Ты не получишь свой браслет дружбы!", "Попробуй новые духи!"]
sty = ["Кто хо-хо-хо~очет авто-о-о-граф?", "Ха-ХА-ха, я по-ПО-поймал тебя!", "Аварии, огонь! Починят — вернусь.", "Уи-и-и-и!..", "Я по-по-покажу тебе безумие."]
leon = ["Вперед!", "Леон главней!", "Да ну!", "Да-да-да!", "Нечестно!"]

# евент на активность бота

@bot.event
async def on_ready():
    activity = discord.Streaming(
        name=
        f"{len(bot.guilds)} server(s)! | бравл старс",
        url = "https://www.youtube.com/watch?v=z2JmKR_STSw",type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print("Бот активен!")


# евент чтобы от отвечал на переменные от слова "шейли" отвечал на одну из её фраз
@bot.event
async def on_message(message):
    if message.content == "шейли": # это вы можете скопировать и просто менять как на видео
        await message.channel.send(f"{random.choice(shelly)}")
    if message.content == "кольт":
        await message.channel.send(f"{random.choice(colt)}")
    if message.content == "нита":
        await message.channel.send(f"{random.choice(nita)}")
    if message.content == "булл":
        await message.channel.send(f"{random.choice(bull)}")
    if message.content == "диномайк":
        await message.channel.send(f"{random.choice(dinamike)}")
    if message.content == "джесси":
        await message.channel.send(f"{random.choice(jessie)}")
    if message.content == "8-бит":
        await message.channel.send(f"{random.choice(vosembit)}")
    if message.content == "эмз":
        await message.channel.send(f"{random.choice(emz)}")
    if message.content == "сту":
        await message.channel.send(f"{random.choice(sty)}")
    if message.content == "леон":
        await message.channel.send(f"{random.choice(leon)}")

    await bot.process_commands(message)


bot.run(token) # чтобы бот работал