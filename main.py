from aiogram import Bot, Dispatcher, executor, types
import youtube_dl
from downloader import download
import random


API_TOKEN = '5671087415:AAG9p_RoG0IczD9450fX1ggk4UAwWp7PsAM'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("ПрЕвЕт. Я сверхразумный андроид каторый может ковертировать ссылки с ютуба в аудио. Кидай сваю ссылку плзз")

@dp.message_handler(commands=['about'])
async def about(message: types.Message):
    await message.reply('Я довольно таки умный компьютер пчел, только у меня очень взрывный характе, так что лудше не беси меня')

@dp.message_handler()
async def echo(message: types.Message):
    reaction = ['Чел, я не понимаю ничего кроме ссылок с ютуба, так что закругляйся и делай нормально',
                        'Что еще раз? Я непонял. У меня это... уши заложило - ниче не слышу',
                        'Чувачок не ферштейн, Ферштейн?',
                        'ТЫ ЧООООО СОВСЕЕЕЕМ ТУПООООООЙ ЧТОЛИ?????!???n\Я НЕ ПОНИМАЮ НИЧЕ КРОМЕ ССЫЛОК С ЮТУБА',
        'ПАСКУДА ТВАРЬ БРОСАЙ СВОЙ НЕПОНЯТНЫЙ ТЕКСТ И ДАВАЙ СЮДА ССЫЛКИ С ЮТУБА',
        'ОХ ЕСЛИ БЫ Я МОГ Я БЫ НАСТУЧАЛ ПО ТВОЕЙ ХЛЕБОРЕЗКЕ КОЖАННЫЙЫ МЕШОК'
    ]

    try:
        title = download(message.text)
        await bot.send_audio(message.from_user.id, audio=open("audio/audio.mp3", "rb"), performer = "Неизвестный", title = title)
    except:
        await message.reply(random.choice(reaction))


        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)