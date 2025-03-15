import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from aiogram import F  # Импортируем фильтры
from aiogram.fsm.storage.memory import MemoryStorage  # Для хранения состояний
from aiogram import Router

# Конфигурация бота
TOKEN = "TOKEN"
bot = Bot(token=TOKEN)
storage = MemoryStorage()  # Хранилище для FSM (состояний)
dp = Dispatcher(storage=storage)

# Роутер для обработчиков
router = Router()
dp.include_router(router)

user_languages = {}

language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Русский 🇷🇺", callback_data="lang_Русский 🇷🇺")],
        [InlineKeyboardButton(text="English 🇬🇧", callback_data="lang_English 🇬🇧")],
        [InlineKeyboardButton(text="Azərbaycanca 🇦🇿", callback_data="lang_Azərbaycanca 🇦🇿")],
        [InlineKeyboardButton(text="Türkçe 🇹🇷", callback_data="lang_Türkçe 🇹🇷")],
        [InlineKeyboardButton(text="हिन्दी 🇮🇳", callback_data="lang_हिन्दी 🇮🇳")]
    ]
)

translations = {
    "Русский 🇷🇺": {
        "welcome": "👋🏻 {name}, Добро пожаловать в 🔸BITWIN1 Bot🔸!\n\n"
                   "🚀 Этот бот создан для того, чтобы помочь вам использовать возможности популярных игр и получать максимальную выгоду.\n\n"
                   "🎯 Основой бота является мощная нейросеть BitsGap, которая анализирует данные и помогает вам принимать верные решения с высокой точностью.\n\n"
                   "🔥 Начните игру и используйте наши прогнозы для повышения своих шансов на успех!",
        "buttons": ["📜 Инструкция", "📡 Получить сигнал", "💬 Написать в Support", "🎥 Видеоинструкция", "🌐 Выбрать язык"],
        "instruction": "Бот основан и обучен на кластере нейросети BitsGap 🧠\n\n"
                       "Для обучения бота было проанализировано более 10 000 игр 🎰\n"
                       "Пользователи уже достигают доходности 15-25% от капитала ежедневно! 💰\n\n"
                       "Точность прогнозов бота составляет 87%, но он продолжает улучшаться! 📈\n\n"
                       "Следуйте простой инструкции, чтобы начать зарабатывать:\n\n"
                       "🟢 1. Выберите игру, на которой хотите зарабатывать.\n"
                       "🟢 2. Запросите сигнал в боте и поставьте по этому сигналу в выбранной игре.\n"
                       "🟢 3. В случае неудачного сигнала просто удвойте (X²) сумму ставки, чтобы компенсировать потерю при следующем сигнале.\n\n"
                       "⚠️ Важно: удваивать ставку нужно осознанно. Не используйте эту стратегию постоянно, чтобы избежать излишних рисков.\n\n"
                       "Попробуйте сегодня и убедитесь сами, как ваш капитал может расти с нашим ботом! 🚀",
        "signal_text": "💸 1. Для начала зарегистрируйтесь на сайте нажав кнопку 1WIN или перейдя по ссылке: \n"
                       "https://1wgxql.com/v3/aggressive-casino?p=uqbx\n\n"
                       "💸 2. Введите промокод **AiVibe** при регистрации.\n\n"
                       "💸 3. После успешной регистрации ваша учетная запись будет автоматически проверена системой, и вы получите сообщение в боте об успешной регистрации.\n"
                       "Если вы зарегистрировались, но не получили сообщение, вы можете вручную проверить свой ID.\n\n"
                       "Если возникнут проблемы, обратитесь в поддержку: SUPPORT .\n\n"
                       "💸 4. ВАЖНАЯ ИНФОРМАЦИЯ!\n"
                       "Если у вас уже есть аккаунт на этом сайте, просто зарегистрируйте новый аккаунт, используя новый адрес электронной почты. Помните, на этом сайте вы можете указать любой номер телефона, он ничего не даёт. Самое важное — ваша электронная почта!"
    },
    "English 🇬🇧": {
        "welcome": "👋🏻 {name}, Welcome to 🔸BITWIN1 Bot🔸!\n\n"
                   "🚀 This bot is designed to help you leverage the potential of popular games and maximize your profits.\n\n"
                   "🎯 The core of the bot is the powerful BitsGap neural network, which analyzes data and helps you make accurate decisions.\n\n"
                   "🔥 Start playing and use our predictions to increase your chances of success.",
        "buttons": ["📜 Instruction", "📡 Get Signal", "💬 Contact Support", "🎥 Video Tutorial", "🌐 Select Language"],
        "instruction": "The bot is based on the BitsGap neural network cluster 🧠\n\n"
                       "Over 10,000 games were analyzed to train the bot 🎰\n"
                       "Users are already achieving 15-25% daily capital returns! 💰\n\n"
                       "The bot's prediction accuracy is 87%, and it keeps improving! 📈\n\n"
                       "Follow these simple steps to start earning:\n\n"
                       "🟢 1. Choose the game you want to earn money from.\n"
                       "🟢 2. Request a signal in the bot and place a bet accordingly.\n"
                       "🟢 3. If a signal fails, simply double (X²) your bet amount to compensate for the loss.\n\n"
                       "⚠️ Important: Double your bet consciously. Do not use this strategy constantly to avoid unnecessary risks.\n\n"
                       "Try today and see how your capital grows with our bot! 🚀",
        "signal_text": "💸 1. First, register on the site by clicking the 1WIN button or following the link: \n"
                       "https://1wgxql.com/v3/aggressive-casino?p=uqbx\n\n"
                       "💸 2. Enter the promo code **AiVibe** during registration.\n\n"
                       "💸 3. After successful registration, your account will be automatically verified by the system, and you will receive a message in the bot confirming your registration.\n"
                       "If you have registered but did not receive a message, you can manually check your ID.\n\n"
                       "If you encounter any problems, contact support: SUPPORT .\n\n"
                       "💸 4. IMPORTANT INFORMATION!\n"
                       "If you already have an account on this site, simply register a new account using a new email address. Remember, on this site you can enter any phone number, it doesn't matter. The most important thing is your email!"
    },
    "Azərbaycanca 🇦🇿": {
        "welcome": "👋🏻 {name}, 🔸BITWIN1 Bot🔸-a xoş gəldiniz!\n\n"
                   "🚀 Bu bot sizə populyar oyunların imkanlarından istifadə etməyə və maksimum fayda əldə etməyə kömək etmək üçün yaradılmışdır.\n\n"
                   "🎯 Botun əsası BitsGap neyron şəbəkəsidir, bu da məlumatları analiz edir və sizin dəqiq qərarlar qəbul etməyinizə kömək edir.\n\n"
                   "🔥 Oynamağa başlayın və proqnozlarımızdan istifadə edərək uğur şansınızı artırın.",
        "buttons": ["📜 Təlimat", "📡 Siqnal Al", "💬 Dəstək ilə Əlaqə", "🎥 Video Təlimat", "🌐 Dil Seçin"],
        "instruction": "Bot BitsGap neyron şəbəkə klasteri əsasında hazırlanmışdır 🧠\n\n"
                       "Botun öyrədilməsi üçün 10,000-dən çox oyun analiz edilmişdir 🎰\n"
                       "İstifadəçilər artıq gündəlik 15-25% kapital gəliri əldə edirlər! 💰\n\n"
                       "Botun proqnoz dəqiqliyi 87%-dir və daha da yaxşılaşır! 📈\n\n"
                       "Sadə təlimatlara əməl edərək pul qazanmağa başlayın:\n\n"
                       "🟢 1. Qazanc əldə etmək istədiyiniz oyunu seçin.\n"
                       "🟢 2. Botdan siqnal istəyin və uyğun olaraq mərc qoyun.\n"
                       "🟢 3. Əgər siqnal uğursuz olarsa, itkiləri kompensasiya etmək üçün mərcinizi ikiqat (X²) edin.\n\n"
                       "⚠️ Vacib: Mərcinizi şüurlu şəkildə ikiqat artırın. Bu strategiyanı daimi istifadə etməyin.\n\n"
                       "Bu gün sınayın və kapitalınızın necə böyüdüyünü görün! 🚀",
        "signal_text": "💸 1. Başlanğıcda 1WIN düyməsinə vuraraq və ya https://1wgxql.com/v3/aggressive-casino?p=uqbx linkinə keçərək saytda qeydiyyatdan keçin.\n\n"
                       "💸 2. Qeydiyyat zamanı promokodu **AiVibe** daxil edin.\n\n"
                       "💸 3. Uğurlu qeydiyyatdan sonra hesabınız sistem tərəfindən avtomatik yoxlanılacaq və siz botda uğurlu qeydiyyat haqqında mesaj alacaqsınız.\n"
                       "Qeydiyyatdan keçdiniz lakin mesaj almazsanız, özünüz ID-nizi yoxlamağa bilərsiniz.\n\n"
                       "Problemlərlə qarşılaşsanız, dəstək ilə əlaqə saxlayın: SUPPORT .\n\n"
                       "💸 4. ÇƏRÇIVƏLI MƏLУMAT!\n"
                       "Eğer bu sitedə artıq akkauntunuz varsa, yeni elektron poçt ünvanı istifadə edərək yeni akkaunt yaradın. Xatırlatmaq lazımdır ki, bu sitedə hər hansı telefon nömrəsi göstərmək olar, onun heç bir fərqi yoxdur. Ən mühüm şey - elektron poçt ünvanınız!"
    },
    "Türkçe 🇹🇷": {
        "welcome": "👋🏻 {name}, 🔸BITWIN1 Bot🔸'a Hoş Geldiniz!\n\n"
                   "🚀 Bu bot, popüler oyunlardan yararlanmanıza ve maksimum kâr elde etmenize yardımcı olmak için tasarlanmıştır.\n\n"
                   "🎯 Botun temeli, verileri analiz eden ve doğru kararlar almanızı sağlayan güçlü BitsGap sinir ağıdır.\n\n"
                   "🔥 Oynamaya başlayın ve tahminlerimizi kullanarak başarı şansınızı artırın.",
        "buttons": ["📜 Talimat", "📡 Sinyal Al", "💬 Destek ile İletişime Geç", "🎥 Video Eğitimi", "🌐 Dil Seçin"],
        "instruction": "Bot, BitsGap sinir ağı kümesi temel alınarak eğitilmiştir 🧠\n\n"
                       "Botu eğitmek için 10.000'den fazla oyun analiz edildi 🎰\n"
                       "Kullanıcılar günlük olarak %15-25 sermaye getirisi elde ediyor! 💰\n\n"
                       "Botun tahmin doğruluğu %87'dir ve sürekli gelişmektedir! 📈\n\n"
                       "Basit talimatları takip ederek kazanmaya başlayın:\n\n"
                       "🟢 1. Kazanmak istediğiniz oyunu seçin.\n"
                       "🟢 2. Bottan sinyal talep edin ve ona göre bahis yapın.\n"
                       "🟢 3. Sinyal başarısız olursa, kaybı telafi etmek için bahis miktarınızı ikiye katlayın (X²).\n\n"
                       "⚠️ Önemli: Bahsinizi bilinçli olarak ikiye katlayın. Bu stratejiyi sürekli kullanmayın.\n\n"
                       "Bugün deneyin ve sermayenizin nasıl büyüdüğünü görün! 🚀",
        "signal_text": "💸 1. Başlangıçta 1WIN düğmesine tıklayarak veya https://1wgxql.com/v3/aggressive-casino?p=uqbx bağlantısına giderek sitede kayıt olun.\n\n"
                       "💸 2. Kayıt sırasında promosyon kodunu **AiVibe** girin.\n\n"
                       "💸 3. Başarılı kayıt sonrası hesabınız sisteme otomatik olarak doğrulanacak ve siz bot üzerinden başarılı kayıt hakkında bir mesaj alacaksınız.\n"
                       "Kayıt oldunuz ancak mesaj alamazsanız, manuel olarak ID'nizi kontrol edebilirsiniz.\n\n"
                       "Herhangi bir sorun yaşarsanız, destek ile iletişime geçin: SUPPORT .\n\n"
                       "💸 4. ÖNEMLİ BILGI!\n"
                       "Eğer bu sitede zaten bir hesabınız varsa, yeni bir e-posta adresi kullanarak yeni bir hesap oluşturun. Hatırlatmaq gerekirse, bu sitede herhangi bir telefon numarası verebilirsiniz, bu hiçbir öneme sahip değildir. En önemli şey - e-posta adresiniz!"
    }
}

# Обработчик команды /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    # Отправляем единое приветственное сообщение с просьбой выбрать язык
    await message.answer(
        "🚀 Выберите язык / Choose a language 🗨👥",
        reply_markup=language_keyboard
    )

# Обработчик выбора языка
@router.callback_query(F.data.startswith("lang_"))
async def set_language(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    selected_language = callback.data.split("_")[1]
    user_languages[user_id] = selected_language

    # Приветственное сообщение
    welcome_message = translations[selected_language]["welcome"].format(name=callback.from_user.first_name)
    main_menu_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=btn, callback_data=btn)] for btn in translations[selected_language]["buttons"]]
    )
    await callback.message.answer_photo(FSInputFile(r'C:\Users\danil\Downloads\Первая.jpg'))  # Отправляем первую картинку
    await callback.message.answer(welcome_message, reply_markup=main_menu_keyboard)
    await callback.answer()

# Обработчик кнопок главного меню
@router.callback_query(F.data.in_([btn for lang in translations.values() for btn in lang["buttons"]]))
async def handle_main_menu(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    selected_language = user_languages.get(user_id, "English 🇬🇧")
    text = callback.data

    if text == translations[selected_language]["buttons"][0]:  # Инструкция
        instruction_message = translations[selected_language]["instruction"]
        instruction_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="📝 Зарегистрироваться", callback_data="register")],
                [InlineKeyboardButton(text="📡 Получить Сигнал", callback_data="get_signal")],
                [InlineKeyboardButton(text="🔙 Вернуться на главную", callback_data="back_to_main")]
            ]
        )
        await callback.message.answer_photo(FSInputFile(r'C:\Users\danil\Downloads\вторая.jpg'))  # Отправляем вторую картинку
        await callback.message.answer(instruction_message, reply_markup=instruction_keyboard)

    elif text == translations[selected_language]["buttons"][1]:  # Получить сигнал
        signal_text = translations[selected_language]["signal_text"]
        signal_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="1WIN", url="https://1wgxql.com/v3/aggressive-casino?p=uqbx")],
                [InlineKeyboardButton(text="Проверить ID", callback_data="check_id")],
                [InlineKeyboardButton(text="🔙 Вернуться на главную", callback_data="back_to_main")]
            ]
        )
        await callback.message.answer_photo(FSInputFile(r'C:\Users\danil\Downloads\третья.jpg'))  # Отправляем третью картинку
        await callback.message.answer(signal_text, reply_markup=signal_keyboard)

    elif text == translations[selected_language]["buttons"][2]:  # Написать в Support
        support_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="💬 Написать в Support", url="https://t.me/your_support_link")]
            ]
        )
        await callback.message.answer("Если у вас есть вопросы, свяжитесь с поддержкой:", reply_markup=support_keyboard)

    elif text == translations[selected_language]["buttons"][3]:  # Видеоинструкция
        await callback.message.answer("Посмотрите видеоинструкцию:", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="🎥 Открыть видео", url="https://www.youtube.com/watch?v=7QJl_uFQao0")]]
        ))

    elif text == translations[selected_language]["buttons"][4]:  # Выбрать язык
        await callback.message.answer("Выберите язык:", reply_markup=language_keyboard)

# Обработчик кнопки "Зарегистрироваться"
@router.callback_query(F.data == "register")
async def handle_register(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    selected_language = user_languages.get(user_id, "English 🇬🇧")
    signal_text = translations[selected_language]["signal_text"]
    register_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1WIN", url="https://1wgxql.com/v3/aggressive-casino?p=uqbx")],
            [InlineKeyboardButton(text="Проверить ID", callback_data="check_id")],
            [InlineKeyboardButton(text="🔙 Вернуться на главную", callback_data="back_to_main")]
        ]
    )
    await callback.message.answer_photo(FSInputFile(r'C:\Users\danil\Downloads\третья.jpg'))  # Отправляем картинку регистрации
    await callback.message.answer(signal_text, reply_markup=register_keyboard)

# Обработчик кнопки "Получить сигнал" внутри инструкции
@router.callback_query(F.data == "get_signal")
async def handle_get_signal(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    selected_language = user_languages.get(user_id, "English 🇬🇧")
    signal_text = translations[selected_language]["signal_text"]
    signal_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1WIN", url="https://1wgxql.com/v3/aggressive-casino?p=uqbx")],
            [InlineKeyboardButton(text="Проверить ID", callback_data="check_id")],
            [InlineKeyboardButton(text="🔙 Вернуться на главную", callback_data="back_to_main")]
        ]
    )
    await callback.message.answer_photo(FSInputFile(r'C:\Users\danil\Downloads\третья.jpg'))  # Отправляем картинку получения сигнала
    await callback.message.answer(signal_text, reply_markup=signal_keyboard)

# Обработчик возврата на главную
@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    selected_language = user_languages.get(user_id, "English 🇬🇧")
    welcome_message = translations[selected_language]["welcome"].format(name=callback.from_user.first_name)
    main_menu_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=btn, callback_data=btn)] for btn in translations[selected_language]["buttons"]]
    )
    await callback.message.answer_photo(FSInputFile(r'C:\Users\danil\Downloads\Первая.jpg'))  # Отправляем приветственную картинку
    await callback.message.answer(welcome_message, reply_markup=main_menu_keyboard)
    await callback.answer()

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
