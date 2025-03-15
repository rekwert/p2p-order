from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import json

TOKEN = "7679686266:AAFQUchkQF4hnC1VecX30uHAnOxPdxbRXJA"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Храним язык пользователей в памяти (можно заменить на Redis или БД)
user_languages = {}

# Клавиатура для выбора языка
language_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
language_keyboard.add(KeyboardButton("Русский 🇷🇺"))
language_keyboard.add(KeyboardButton("English 🇬🇧"))
language_keyboard.add(KeyboardButton("हिन्दी 🇮🇳"))

# Тексты на разных языках
messages = {
    "ru": {
        "welcome": "👋🏻 {name}, Добро пожаловать в 🔸Бота🔸!\n\n🚀 Этот бот создан для того, чтобы помочь вам использовать возможности популярных игр и получать максимальную выгоду.\n\n🎯 Основой бота является мощная нейросеть (Бота), которая анализирует данные и помогает вам принимать верные решения с высокой точностью.\n\n🔥 Начните игру и используйте наши прогнозы для повышения своих шансов на успех!",
        "buttons": ["📜 Инструкция", "📡 Получить сигнал", "🎥 Видеоинструкция", "✉️ Написать в Support"],
        "instruction": "Бот основан и обучен на кластере нейросети БОТ 🧠\n\nДля обучения бота было проанализировано более 10 000 игр 🎰\nПользователи уже достигают доходности 15-25% от капитала ежедневно! 💰\n\nТочность прогнозов бота составляет 87%, но он продолжает улучшаться! 📈\n\nСледуйте простой инструкции, чтобы начать зарабатывать:\n\n🟢 1. Выберите игру, на которой хотите зарабатывать.\n🟢 2. Запросите сигнал в боте и поставьте по этому сигналу в выбранной игре.\n🟢 3. В случае неудачного сигнала просто удвойте (X²) сумму ставки, чтобы компенсировать потерю при следующем сигнале.\n\n⚠️ Важно: удваивать ставку нужно осознанно. Не используйте эту стратегию постоянно, чтобы избежать излишних рисков.\n\nПопробуйте сегодня и убедитесь сами, как ваш капитал может расти с нашим ботом! 🚀",
        "instruction_buttons": ["Зарегистрироваться", "📡 Получить сигнал", "🔙 Вернуться на главную"],
        "registration": "💸 1. Для начала зарегистрируйтесь на сайте нажав кнопку 1WIN или перейдя по ссылке: (https://1wgxql.com/v3/aggressive-casino?p=uqbx)\n\n💸 2. Введите промокод (новый) при регистрации.\n\n💸 3. После успешной регистрации ваша учетная запись будет автоматически проверена системой, и вы получите сообщение в боте об успешной регистрации.\nЕсли вы зарегистрировались, но не получили сообщение, вы можете вручную проверить свой ID.\n\nЕсли возникнут проблемы, обратитесь в поддержку: SUPPORT (https://t.me/Forsakenbb).\n\n💸 4. ВАЖНАЯ ИНФОРМАЦИЯ!\nЕсли у вас уже есть аккаунт на этом сайте, просто зарегистрируйте новый аккаунт, используя новый адрес электронной почты. Помните, на этом сайте вы можете указать любой номер телефона, он ничего не даёт. Самое важное — ваша электронная почта!",
        "registration_buttons": ["1WIN", "🔙 Отмена", "✔️ Проверить ID"],
        "check_id": "Введите ваш 1WIN ID, который состоит из 9 цифр (Например: 46230574)",
        "check_id_buttons": ["🔙 Отмена", "✉️ Написать в Support"]
    }
}


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Выберите язык / Choose a language / एक भाषा चुनें:", reply_markup=language_keyboard)


@dp.message_handler(lambda message: message.text in ["Русский 🇷🇺", "English 🇬🇧", "हिन्दी 🇮🇳"])
async def set_language(message: types.Message):
    user_id = message.from_user.id
    lang = "ru" if "Русский" in message.text else "en" if "English" in message.text else "hi"
    user_languages[user_id] = lang

    welcome_text = messages[lang]["welcome"].format(name=message.from_user.first_name)
    buttons = messages[lang]["buttons"]

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for btn in buttons:
        keyboard.add(KeyboardButton(btn))

    await message.answer(welcome_text, reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "📜 Инструкция")
async def instruction_command(message: types.Message):
    lang = user_languages.get(message.from_user.id, "ru")
    text = messages[lang]["instruction"]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for btn in messages[lang]["instruction_buttons"]:
        keyboard.add(KeyboardButton(btn))
    await message.answer(text, reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "✔️ Проверить ID")
async def check_id_command(message: types.Message):
    lang = user_languages.get(message.from_user.id, "ru")
    text = messages[lang]["check_id"]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for btn in messages[lang]["check_id_buttons"]:
        keyboard.add(KeyboardButton(btn))
    await message.answer(text, reply_markup=keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)