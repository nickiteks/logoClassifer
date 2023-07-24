from usecase import Usecase
import logging
import sqlite3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Этапы/состояния разговора
LOCATION, NOISE, KATEGORY, END = range(4)
# Данные обратного вызова
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EITHT, NINE, TEN = range(1, 11)


def start(update, context):
    # Получаем пользователя, который запустил команду '/start'
    user = update.message.from_user
    logger.info("Пользователь %s начал разговор", user.first_name)

    connection = sqlite3.connect("bd.sqlite3")
    usecase = Usecase(connection)
    usecase.repo.create_db()
    usecase.init_user(update.effective_chat.id)
    photos = usecase.list_photo_names(update.effective_chat.id)

    if len(photos) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Вы оценили все фото, спасибо!')
        return END

    context.user_data['PHOTO'] = photos[0]

    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("2", callback_data=str(TWO)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
            InlineKeyboardButton("4", callback_data=str(FOUR)),
            InlineKeyboardButton("5", callback_data=str(FIVE)),
        ],
        [
            InlineKeyboardButton("6", callback_data=str(SIX)),
            InlineKeyboardButton("7", callback_data=str(SEVEN)),
            InlineKeyboardButton("8", callback_data=str(EITHT)),
            InlineKeyboardButton("9", callback_data=str(NINE)),
            InlineKeyboardButton("10", callback_data=str(TEN)),
        ]
    ]
    keyboard_markup = InlineKeyboardMarkup(keyboard)
    # Отправляем сообщение с изображением и добавленной клавиатурой 'reply_markup'
    # current_photo =
    updater.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/dell/Projects/tg_markup_bot/data/' + context.user_data['PHOTO'], 'rb'), caption='Оцените стиль', reply_markup=keyboard_markup)
    # Сообщаем 'ConversationHandler' новое состояние
    return LOCATION


def start_over(update, context):
    # Тот же текст и клавиатура, что и при '/start', но не как новое сообщение
    # Получаем 'CallbackQuery' из обновления `update`
    query = update.callback_query

    mark = query.data
    context.user_data['KATEGORY'] = mark

    connection = sqlite3.connect("bd.sqlite3")
    usecase = Usecase(connection)
    usecase.init_user(update.effective_chat.id)

    usecase.add_mark(context.user_data['PHOTO'], update.effective_chat.id, context.user_data['STYLE'], context.user_data['NOISE'], context.user_data['LOCATION'], context.user_data['KATEGORY'])
    print(context.user_data)
    context.user_data.clear()

    photos = usecase.list_photo_names(update.effective_chat.id)
    context.user_data['PHOTO'] = photos[0]

    query.answer()

    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("2", callback_data=str(TWO)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
            InlineKeyboardButton("4", callback_data=str(FOUR)),
            InlineKeyboardButton("5", callback_data=str(FIVE)),
        ],
        [
            InlineKeyboardButton("6", callback_data=str(SIX)),
            InlineKeyboardButton("7", callback_data=str(SEVEN)),
            InlineKeyboardButton("8", callback_data=str(EITHT)),
            InlineKeyboardButton("9", callback_data=str(NINE)),
            InlineKeyboardButton("10", callback_data=str(TEN)),
        ]
    ]
    keyboard_markup = InlineKeyboardMarkup(keyboard)

   # Редактируем сообщение, вызвавшее обратный вызов.
    query.message.edit_media(
        reply_markup=keyboard_markup,
        media=InputMediaPhoto(
            media=open('/home/dell/Projects/tg_markup_bot/data/' + context.user_data['PHOTO'], 'rb'),
            caption='Оцените стиль',
        )
    )

    return LOCATION


def one(update, context):
    query = update.callback_query

    # Сохраняем предыдущую оценку
    mark = query.data
    context.user_data['STYLE'] = mark
    # Ответ на обратный запрос
    query.answer()

    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("2", callback_data=str(TWO)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
            InlineKeyboardButton("4", callback_data=str(FOUR)),
            InlineKeyboardButton("5", callback_data=str(FIVE)),
        ],
        [
            InlineKeyboardButton("6", callback_data=str(SIX)),
            InlineKeyboardButton("7", callback_data=str(SEVEN)),
            InlineKeyboardButton("8", callback_data=str(EITHT)),
            InlineKeyboardButton("9", callback_data=str(NINE)),
            InlineKeyboardButton("10", callback_data=str(TEN)),
        ]
    ]
    keyboard_markup = InlineKeyboardMarkup(keyboard)
    query.message.edit_media(
        reply_markup=keyboard_markup,
        media=InputMediaPhoto(
            media=open('/home/dell/Projects/tg_markup_bot/data/' + context.user_data['PHOTO'], 'rb'),
            caption='Оцените расположение',
        )
    )
    return NOISE


def two(update, context):
    query = update.callback_query

    mark = query.data
    context.user_data['LOCATION'] = mark

    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("2", callback_data=str(TWO)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
            InlineKeyboardButton("4", callback_data=str(FOUR)),
            InlineKeyboardButton("5", callback_data=str(FIVE)),
        ],
        [
            InlineKeyboardButton("6", callback_data=str(SIX)),
            InlineKeyboardButton("7", callback_data=str(SEVEN)),
            InlineKeyboardButton("8", callback_data=str(EITHT)),
            InlineKeyboardButton("9", callback_data=str(NINE)),
            InlineKeyboardButton("10", callback_data=str(TEN)),
        ]
    ]
    keyboard_markup = InlineKeyboardMarkup(keyboard)
    query.message.edit_media(
        reply_markup=keyboard_markup,
        media=InputMediaPhoto(
            media=open('/home/dell/Projects/tg_markup_bot/data/' + context.user_data['PHOTO'], 'rb'),
            caption='Оцените количество информационного шума',
        )
    )

    return KATEGORY


def three(update, context):
    query = update.callback_query

    mark = query.data
    context.user_data['NOISE'] = mark

    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Еда", callback_data=str('Еда')),
            InlineKeyboardButton("Аптеки", callback_data=str('Аптеки')),
            InlineKeyboardButton("Красота", callback_data=str('Красота'))
        ],
        [
            InlineKeyboardButton("Магазины", callback_data=str('Магазины')),
            InlineKeyboardButton("Услуги", callback_data=str('Услуги')),
        ]
    ]
    keyboard_markup = InlineKeyboardMarkup(keyboard)
    query.message.edit_media(
        reply_markup=keyboard_markup,
        media=InputMediaPhoto(
            media=open('/home/dell/Projects/tg_markup_bot/data/' + context.user_data['PHOTO'], 'rb'),
            caption='Выберите категорию',
        )
    )
    return END

def get_data(update, context):
    connection = sqlite3.connect("bd.sqlite3")
    usecase = Usecase(connection)
    usecase.init_user(update.effective_chat.id)

    updater.bot.send_document(chat_id=update.effective_chat.id, document=open('/home/dell/Projects/tg_markup_bot/' + usecase.get_dataset(), 'rb'))


def end(update, context):
    """Возвращает 'ConversationHandler.END', который говорит 
    'ConversationHandler', что разговор окончен"""
    query = update.callback_query
    context.bot.send_message(chat_id=update.effective_chat.id, text='Оценка приостановлена')
    context.user_data.clear()
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater("6394042503:AAExAD9WKGV-F8BvRS__TJ4fCrlBOkZjzS4")
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={  # словарь состояний разговора, возвращаемых callback функциями
            LOCATION: [
                CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(one, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(one, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(one, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(one, pattern='^' + str(FIVE) + '$'),
                CallbackQueryHandler(one, pattern='^' + str(SIX) + '$'),
                CallbackQueryHandler(one, pattern='^' + str(SEVEN) + '$'),
                CallbackQueryHandler(one, pattern='^' + str(EITHT) + '$'),
                CallbackQueryHandler(one, pattern='^' + str(NINE) + '$'),
                CallbackQueryHandler(one, pattern='^' + str(TEN) + '$'),
                CommandHandler('end', end)
            ],
            NOISE: [
                CallbackQueryHandler(two, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(FIVE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(SIX) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(SEVEN) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(EITHT) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(NINE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TEN) + '$'),
                CommandHandler('end', end)
            ],
            KATEGORY: [
                CallbackQueryHandler(three, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(FIVE) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(SIX) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(SEVEN) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(EITHT) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(NINE) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(TEN) + '$'),
                CommandHandler('end', end)
            ],
            END: [
                CallbackQueryHandler(start_over, pattern='^' + 'Еда' + '$'),
                CallbackQueryHandler(start_over, pattern='^' + 'Магазины' + '$'),
                CallbackQueryHandler(start_over, pattern='^' + 'Аптеки' + '$'),
                CallbackQueryHandler(start_over, pattern='^' + 'Красота' + '$'),
                CallbackQueryHandler(start_over, pattern='^' + 'Услуги' + '$'),
                CommandHandler('end', end)
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Добавляем 'ConversationHandler' в диспетчер, который
    # будет использоваться для обработки обновлений
    dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(CommandHandler('get_data', get_data))

    updater.start_polling()
    updater.idle()