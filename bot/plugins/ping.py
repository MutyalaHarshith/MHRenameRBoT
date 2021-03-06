# (c) @AbirHasan2005 & @MutyalaHarshith

from bot.client import Client
from pyrogram import filters
from pyrogram import types
from bot.core.db.add import add_user_to_database


@Client.on_message(filters.command(["start", "ping"]) & filters.private & ~filters.edited)
async def ping_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("πΈ πππ'π ππππ  πππππ π’ππ ππππ :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="π·π, πΈ ππ π΅πππ π΅πππ πππππππ π±ππ!\n\n"
             "I α΄α΄Ι΄ Κα΄Ι΄α΄α΄α΄ α΄α΄α΄Ιͺα΄ & α΄α΄α΄α΄α΄α΄Ι΄α΄s!\n"
             "πΉππ ππππ ππππππππ‘πππ πΆππππ /help.\n\n"
             "ααα΄α©Tα΄αͺ α·Y : @MutyalaHarshith",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("ππππ  ππππππππ",
                                      callback_data="showSettings")
        ]])
    )


@Client.on_message(filters.command("help") & filters.private & ~filters.edited)
async def help_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("πΈ πππ'π ππππ  πππππ π’ππ ππππ :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="πΈ πππ ππππππ πππππ π ππππππ πππ ππππππππ ππ!\n"
             "πππππ πππππππ ππ π’πππ πππππ π³πππ π²πππππ.\n\n"
             "πΉπππ ππππ ππ πππππ ππ ππππππππ ππππ πππ πππππ’ ππ ππ π πππ /rename πππππππ.\n\n"
             "ππ π ππ‘ ππ’π π‘ππ π‘βπ’ππππππ πππππ¦ π‘π πππ¦ πππππ π€ππ‘β /set_thumbnail\n\n"
             "ππ π ππ ππ’π π‘ππ π‘βπ’ππππππ ππππ π  /show_thumbnail",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("ππππ  ππππππππ",
                                      callback_data="showSettings")]])
    )
