from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT, MELCOW_NEW_USERS
from database.users_chats_db import db
from database.ia_filterdb import Media
from utils import get_size, temp, get_settings
from Script import script
from pyrogram.errors import ChatAdminRequired

"""-----------------------------------------https://t.me/GetTGLink/4179 --------------------------------------"""

@Client.on_message(filters.new_chat_members & filters.group)
async def save_group(bot, message):
    r_j_check = [u.id for u in message.new_chat_members]
    if temp.ME in r_j_check:
        if not await db.get_chat(message.chat.id):
            total=await bot.get_chat_members_count(message.chat.id)
            r_j = message.from_user.mention if message.from_user else "Anonymous" 
            await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, r_j))       
            await db.add_chat(message.chat.id, message.chat.title)
        if message.chat.id in temp.BANNED_CHATS:
            # Inspired from a boat of a banana tree
            buttons = [[
                InlineKeyboardButton('Support', url=f'https://t.me/{SUPPORT_CHAT}')
            ]]
            reply_markup=InlineKeyboardMarkup(buttons)
            k = await message.reply(
                text='<b>CHAT NOT ALLOWED 🐞\n\n𝙼𝚢 𝚊𝚍𝚖𝚒𝚗𝚜 𝚑𝚊𝚜 𝚛𝚎𝚜𝚝𝚛𝚒𝚌𝚝𝚎𝚍 𝚖𝚎 𝚏𝚛𝚘𝚖 𝚠𝚘𝚛𝚔𝚒𝚗𝚐 𝚑𝚎𝚛𝚎 ! 𝙸𝚏 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚖𝚘𝚛𝚎 𝚊𝚋𝚘𝚞𝚝 𝚒𝚝 𝚌𝚘𝚗𝚝𝚊𝚌𝚝 𝚜𝚞𝚙𝚙𝚘𝚛𝚝..</b>',
                reply_markup=reply_markup,
            )

            try:
                await k.pin()
            except:
                pass
            await bot.leave_chat(message.chat.id)
            return
        buttons = [[
            InlineKeyboardButton('ℹ️ 𝙷𝚎𝚕𝚙', url=f"https://t.me/{temp.U_NAME}?start=help"),
            InlineKeyboardButton('📢 𝚄𝚙𝚍𝚊𝚝𝚎𝚜', url='https://t.me/SECLK')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=f"<b>𝚃𝚑𝚊𝚗𝚔𝚢𝚘𝚞 𝙵𝚘𝚛 𝙰𝚍𝚍𝚒𝚗𝚐 𝙼𝚎 𝙸𝚗 {message.chat.title} ❣️\n\n𝙸𝚏 𝚢𝚘𝚞 𝚑𝚊𝚟𝚎 𝚊𝚗𝚢 𝚚𝚞𝚎𝚜𝚝𝚒𝚘𝚗𝚜 & 𝚍𝚘𝚞𝚋𝚝𝚜 𝚊𝚋𝚘𝚞𝚝 𝚞𝚜𝚒𝚗𝚐 𝚖𝚎 𝚌𝚘𝚗𝚝𝚊𝚌𝚝 𝚜𝚞𝚙𝚙𝚘𝚛𝚝.</b>",
            reply_markup=reply_markup)
    else:
        settings = await get_settings(message.chat.id)
        if settings["welcome"]:
            for u in message.new_chat_members:
                if (temp.MELCOW).get('welcome') is not None:
                    try:
                        await (temp.MELCOW['welcome']).delete()
                    except:
                        pass
                temp.MELCOW['welcome'] = await message.reply(f"<b>Hey , {u.mention}, Welcome to {message.chat.title}</b>")


@Client.on_message(filters.command('leave') & filters.user(ADMINS))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('Support', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text='<b>𝙷𝚎𝚕𝚕𝚘 𝙵𝚛𝚒𝚎𝚗𝚍𝚜, \n𝙼𝚢 𝚊𝚍𝚖𝚒𝚗 𝚑𝚊𝚜 𝚝𝚘𝚕𝚍 𝚖𝚎 𝚝𝚘 𝚕𝚎𝚊𝚟𝚎 𝚏𝚛𝚘𝚖 𝚐𝚛𝚘𝚞𝚙 𝚜𝚘 𝚒 𝚐𝚘! 𝙸𝚏 𝚢𝚘𝚞 𝚠𝚊𝚗𝚗𝚊 𝚊𝚍𝚍 𝚖𝚎 𝚊𝚐𝚊𝚒𝚗 𝚌𝚘𝚗𝚝𝚊𝚌𝚝 𝚖𝚢 𝚜𝚞𝚙𝚙𝚘𝚛𝚝 𝚐𝚛𝚘𝚞𝚙.</b>',
            reply_markup=reply_markup,
        )

        await bot.leave_chat(chat)
        await message.reply(f"left the chat `{chat}`")
    except Exception as e:
        await message.reply(f'Error - {e}')

@Client.on_message(filters.command('disable') & filters.user(ADMINS))
async def disable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Give Me A Valid Chat ID')
    cha_t = await db.get_chat(int(chat_))
    if not cha_t:
        return await message.reply("𝙲𝚑𝚊𝚝 𝙽𝚘𝚝 𝙵𝚘𝚞𝚗𝚍 𝙸𝚗 𝙳𝙱")
    if cha_t['is_disabled']:
        return await message.reply(f"𝚃𝚑𝚒𝚜 𝚌𝚑𝚊𝚝 𝚒𝚜 𝚊𝚕𝚛𝚎𝚊𝚍𝚢 𝚍𝚒𝚜𝚊𝚋𝚕𝚎𝚍:\nReason-<code> {cha_t['reason']} </code>")
    await db.disable_chat(int(chat_), reason)
    temp.BANNED_CHATS.append(int(chat_))
    await message.reply('𝙲𝚑𝚊𝚝 𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝙳𝚒𝚜𝚊𝚋𝚕𝚎𝚍')
    try:
        buttons = [[
            InlineKeyboardButton('𝚂𝚞𝚙𝚙𝚘𝚛𝚝', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat_, 
            text=f'<b>𝙷𝚎𝚕𝚕𝚘 𝙵𝚛𝚒𝚎𝚗𝚍𝚜, \n𝙼𝚢 𝚊𝚍𝚖𝚒𝚗 𝚑𝚊𝚜 𝚝𝚘𝚕𝚍 𝚖𝚎 𝚝𝚘 𝚕𝚎𝚊𝚟𝚎 𝚏𝚛𝚘𝚖 𝚐𝚛𝚘𝚞𝚙 𝚜𝚘 𝚒 𝚐𝚘! 𝙸𝚏 𝚢𝚘𝚞 𝚠𝚊𝚗𝚗𝚊 𝚊𝚍𝚍 𝚖𝚎 𝚊𝚐𝚊𝚒𝚗 𝚌𝚘𝚗𝚝𝚊𝚌𝚝 𝚖𝚢 𝚜𝚞𝚙𝚙𝚘𝚛𝚝 𝚐𝚛𝚘𝚞𝚙.</b> \n𝚁𝚎𝚊𝚜𝚘𝚗 : <code>{reason}</code>',
            reply_markup=reply_markup)
        await bot.leave_chat(chat_)
    except Exception as e:
        await message.reply(f"Error - {e}")


@Client.on_message(filters.command('enable') & filters.user(ADMINS))
async def re_enable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat_ = int(chat)
    except:
        return await message.reply('𝙶𝚒𝚟𝚎 𝙼𝚎 𝙰 𝚅𝚊𝚕𝚒𝚍 𝙲𝚑𝚊𝚝 𝙸𝙳')
    sts = await db.get_chat(int(chat))
    if not sts:
        return await message.reply("𝙲𝚑𝚊𝚝 𝙽𝚘𝚝 𝙵𝚘𝚞𝚗𝚍 𝙸𝚗 𝙳𝙱 !")
    if not sts.get('is_disabled'):
        return await message.reply('𝚃𝚑𝚒𝚜 𝚌𝚑𝚊𝚝 𝚒𝚜 𝚗𝚘𝚝 𝚢𝚎𝚝 𝚍𝚒𝚜𝚊𝚋𝚕𝚎𝚍.')
    await db.re_enable_chat(int(chat_))
    temp.BANNED_CHATS.remove(int(chat_))
    await message.reply("𝙲𝚑𝚊𝚝 𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚛𝚎-𝚎𝚗𝚊𝚋𝚕𝚎𝚍")


@Client.on_message(filters.command('stats') & filters.incoming)
async def get_ststs(bot, message):
    rju = await message.reply('𝙵𝚎𝚝𝚌𝚑𝚒𝚗𝚐 𝚜𝚝𝚊𝚝𝚜..')
    total_users = await db.total_users_count()
    totl_chats = await db.total_chat_count()
    files = await Media.count_documents()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)
    await rju.edit(script.STATUS_TXT.format(files, total_users, totl_chats, size, free))


# a function for trespassing into others groups, Inspired by a Vazha
# Not to be used , But Just to showcase his vazhatharam.
# @Client.on_message(filters.command('invite') & filters.user(ADMINS))
async def gen_invite(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('Give Me A Valid Chat ID')
    try:
        link = await bot.create_chat_invite_link(chat)
    except ChatAdminRequired:
        return await message.reply("Invite Link Generation Failed, Iam Not Having Sufficient Rights")
    except Exception as e:
        return await message.reply(f'Error {e}')
    await message.reply(f'Here is your Invite Link {link.invite_link}')

@Client.on_message(filters.command('ban') & filters.user(ADMINS))
async def ban_a_user(bot, message):
    # https://t.me/GetTGLink/4185
    if len(message.command) == 1:
        return await message.reply('Give me a user id / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("𝚃𝚑𝚒𝚜 𝚒𝚜 𝚊𝚗 𝚒𝚗𝚟𝚊𝚕𝚒𝚍 𝚞𝚜𝚎𝚛, 𝚖𝚊𝚔𝚎 𝚜𝚞𝚛𝚎 𝚒𝚊 𝚑𝚊𝚟𝚎 𝚖𝚎𝚝 𝚑𝚒𝚖 𝚋𝚎𝚏𝚘𝚛𝚎.")
    except IndexError:
        return await message.reply("𝚃𝚑𝚒𝚜 𝚖𝚒𝚐𝚑𝚝 𝚋𝚎 𝚊 𝚌𝚑𝚊𝚗𝚗𝚎𝚕, 𝚖𝚊𝚔𝚎 𝚜𝚞𝚛𝚎 𝚒𝚝𝚜 𝚊 𝚞𝚜𝚎𝚛.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if jar['is_banned']:
            return await message.reply(f"{k.mention} is 𝚊𝚕𝚛𝚎𝚊𝚍𝚢 𝚋𝚊𝚗𝚗𝚎𝚍\n𝚁𝚎𝚊𝚜𝚘𝚗: {jar['ban_reason']}")
        await db.ban_user(k.id, reason)
        temp.BANNED_USERS.append(k.id)
        await message.reply(f"𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚋𝚊𝚗𝚗𝚎𝚍 {k.mention}")


    
@Client.on_message(filters.command('unban') & filters.user(ADMINS))
async def unban_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('𝙶𝚒𝚟𝚎 𝚖𝚎 𝚊 𝚞𝚜𝚎𝚛 𝚒𝚍 / 𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "𝙽𝚘 𝚛𝚎𝚊𝚜𝚘𝚗 𝙿𝚛𝚘𝚟𝚒𝚍𝚎𝚍"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("𝚃𝚑𝚒𝚜 𝚒𝚜 𝚊𝚗 𝚒𝚗𝚟𝚊𝚕𝚒𝚍 𝚞𝚜𝚎𝚛, 𝚖𝚊𝚔𝚎 𝚜𝚞𝚛𝚎 𝚒𝚊 𝚑𝚊𝚟𝚎 𝚖𝚎𝚝 𝚑𝚒𝚖 𝚋𝚎𝚏𝚘𝚛𝚎.")
    except IndexError:
        return await message.reply("𝚃𝚑𝚒𝚜 𝚖𝚒𝚐𝚑𝚝 𝚋𝚎 𝚊 𝚌𝚑𝚊𝚗𝚗𝚎𝚕, 𝚖𝚊𝚔𝚎 𝚜𝚞𝚛𝚎 𝚒𝚝𝚜 𝚊 𝚞𝚜𝚎𝚛.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if not jar['is_banned']:
            return await message.reply(f"{k.mention} is not yet banned.")
        await db.remove_ban(k.id)
        temp.BANNED_USERS.remove(k.id)
        await message.reply(f"Successfully unbanned {k.mention}")


    
@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    # https://t.me/GetTGLink/4184
    raju = await message.reply('𝙶𝚎𝚝𝚝𝚒𝚗𝚐 𝙻𝚒𝚜𝚝 𝙾𝚏 𝚄𝚜𝚎𝚛𝚜')
    users = await db.get_all_users()
    out = "𝚄𝚜𝚎𝚛𝚜 𝚂𝚊𝚟𝚎𝚍 𝙸𝚗 𝙳𝙱 𝙰𝚛𝚎:\n\n"
    async for user in users:
        out += f"<a href=tg://user?id={user['id']}>{user['name']}</a>"
        if user['ban_status']['is_banned']:
            out += '( Banned User )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="List Of Users")

@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def list_chats(bot, message):
    raju = await message.reply('Getting List Of chats')
    chats = await db.get_all_chats()
    out = "𝙲𝚑𝚊𝚝𝚜 𝚂𝚊𝚟𝚎𝚍 𝙸𝚗 𝙳𝙱 𝙰𝚛𝚎:\n\n"
    async for chat in chats:
        out += f"**Title:** `{chat['title']}`\n**- ID:** `{chat['id']}`"
        if chat['chat_status']['is_disabled']:
            out += '( Disabled Chat )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="List Of Chats")
