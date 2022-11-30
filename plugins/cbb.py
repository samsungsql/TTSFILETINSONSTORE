#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>തനി മലയാളം</code>\n○ Library : <a href='ബിരിയാണി റെഡി/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='ബിരിയാണി വേണോ മോനെ '>Click here</a>\n○ Channel : മലയാളം റോക്കർസ് ബിരിയാണി കട\n○ Support Group : ഓടി വാ ബിരിയാണി ഇവിടുണ്ട്</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
