from aiogram import types, Dispatcher
from database.db import db
from keyboards.client_keyboards import start_keyboard, switch_keyboard, back_keyboard
from create_bot import bot
from contextlib import suppress
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

async def delete_message(message_id, chat_id):
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await bot.delete_message(message_id=message_id, chat_id=chat_id)

async def examples(callback: types.CallbackQuery):
    current_post_id, messages_to_delete, chat_id = db.get_messages_to_delete(callback.from_user.id)
    messages_to_delete = eval(messages_to_delete)
    post_info = db.get_example_post(1)
    if post_info != None:
        for i in range(len(messages_to_delete)):
            await delete_message(messages_to_delete[i], chat_id)

    if post_info[1] != None:
        photos = eval(post_info[1])
    if post_info[2] != None:
        videos = eval(post_info[2])

    if len(photos) + len(videos) > 1:

        media = types.MediaGroup()

        for i in range(videos):
            media.attach_video(videos[i], caption=post_info[3])

        for i in range(photos):
            media.attach_photo(photos[i], caption=post_info[3])
        
        msg = await bot.send_media_group(chat_id, media=media)

    elif len(photos) == 1:
        msg = await bot.send_photo(chat_id, photo=photos[0])
        
    elif len(videos) == 1:
        msg = await bot.send_video(chat_id, video=videos[0])

    msg2 = await bot.send_message(callback.from_user.id, post_info[3], reply_markup=switch_keyboard)
    db.add_messages_to_delete(1, [msg.message_id, msg2.message_id], chat_id)

async def next_post(callback: types.CallbackQuery):
    current_post_id, messages_to_delete, chat_id = db.get_messages_to_delete(callback.from_user.id)
    messages_to_delete = eval(messages_to_delete)
    post_info = db.get_example_post(current_post_id + 1)
    if post_info != None:
        for i in range(len(messages_to_delete)):
            await delete_message(messages_to_delete[i], chat_id) 

        if post_info[1] != None:
            photos = eval(post_info[1])

        if post_info[2] != None:
            videos = eval(post_info[2])

        if len(photos) + len(videos) > 1:

            media = types.MediaGroup()

            for i in range(videos):
                media.attach_video(videos[i], caption=post_info[3])

            for i in range(photos):
                media.attach_photo(photos[i], caption=post_info[3])
            
            msg = await bot.send_media_group(chat_id, media=media)

        elif len(photos) == 1:
            msg = await bot.send_photo(chat_id, photo=photos[0])
            
        elif len(videos) == 1:
            msg = await bot.send_video(chat_id, video=videos[0])

        msg2 = await bot.send_message(callback.from_user.id, post_info[3], reply_markup=switch_keyboard)
        db.add_messages_to_delete(current_post_id + 1, [msg.message_id, msg2.message_id], chat_id)


async def previous_post(callback: types.CallbackQuery):
    current_post_id, messages_to_delete, chat_id = db.get_messages_to_delete(callback.from_user.id)
    messages_to_delete = eval(messages_to_delete)
    post_info = db.get_example_post(current_post_id - 1)
    if post_info != None:
        for i in range(len(messages_to_delete)):
            await delete_message(messages_to_delete[i], chat_id) 

        if post_info[1] != None:
            photos = eval(post_info[1])
            
        if post_info[2] != None:
            videos = eval(post_info[2])

        if len(photos) + len(videos) > 1:

            media = types.MediaGroup()

            for i in range(videos):
                media.attach_video(videos[i], caption=post_info[3])

            for i in range(photos):
                media.attach_photo(photos[i], caption=post_info[3])
            
            msg = await bot.send_media_group(chat_id, media=media)

        elif len(photos) == 1:
            msg = await bot.send_photo(chat_id, photo=photos[0])
            
        elif len(videos) == 1:
            msg = await bot.send_video(chat_id, video=videos[0])

        msg2 = await bot.send_message(callback.from_user.id, post_info[3], reply_markup=switch_keyboard)
        db.add_messages_to_delete(current_post_id - 1, [msg.message_id, msg2.message_id], chat_id)

async def booking(callback: types.CallbackQuery):
    current_post_id, messages_to_delete, chat_id = db.get_messages_to_delete(callback.from_user.id)
    messages_to_delete = eval(messages_to_delete)
    for i in range(len(messages_to_delete)):
        await delete_message(messages_to_delete[i], chat_id) 

    msg = await bot.send_message(callback.from_user.id, 'Запись:\n\n`+ 7 911 761 5472`\n\ntg: `ks278`\ninst: `s.detailng_`', reply_markup=back_keyboard, parse_mode=types.ParseMode.MARKDOWN)
    db.add_messages_to_delete(0, [msg.message_id], chat_id)

async def get_back(callback: types.CallbackQuery):
    current_post_id, messages_to_delete, chat_id = db.get_messages_to_delete(callback.from_user.id)
    messages_to_delete = eval(messages_to_delete)
    for i in range(len(messages_to_delete)):
        await delete_message(messages_to_delete[i], chat_id) 
    msg = await bot.send_message(callback.from_user.id, 'Добро пожаловать в Sdetailing!', reply_markup=start_keyboard)
    db.add_messages_to_delete(0, [msg.message_id], chat_id)

async def start_commands(message: types.Message):
    chat_id = message.from_user.id
    msg = await bot.send_message(chat_id, 'Добро пожаловать в Sdetailing!', reply_markup=start_keyboard)
    db.add_messages_to_delete(0, [msg.message_id], chat_id)

async def photo_handler(message: types.Message):
    document_id = message.photo[0].file_id
    file_info = await bot.get_file(document_id)
    print(f'file_id: {file_info.file_id}')
    print(f'file_path: {file_info.file_path}')
    print(f'file_size: {file_info.file_size}')
    print(f'file_unique_id: {file_info.file_unique_id}')

async def video_handler(message: types.Message):
    document_id = message.video.file_id
    print(f'file_id: {document_id}')


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(start_commands, commands=['start', 'help'])
    dp.register_callback_query_handler(examples, text='examples')
    dp.register_callback_query_handler(previous_post, text='previous_example')
    dp.register_callback_query_handler(next_post, text='next_example')
    dp.register_callback_query_handler(get_back, text='get_back')
    dp.register_callback_query_handler(booking, text='booking')
    dp.register_message_handler(photo_handler, content_types=['photo'])
    dp.register_message_handler(video_handler, content_types=['video'])