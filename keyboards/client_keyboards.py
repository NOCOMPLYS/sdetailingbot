from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup


support_button = InlineKeyboardButton(text='🆘Поддержка', callback_data='Кепка давит на мозги')
subscribe_button = InlineKeyboardButton(text='✅Подписаться', callback_data='subscribe')
unsubscribe_button = InlineKeyboardButton(text='❌Отписаться', callback_data='unsubscribe')

examples_button = InlineKeyboardButton(text='📄Услуги', callback_data='examples')
booking_button = InlineKeyboardButton(text='☎️Запись', callback_data='booking')
next_example = InlineKeyboardButton(text='➡️', callback_data='next_example')
previous_example = InlineKeyboardButton(text='⬅️', callback_data='previous_example')
blank_button = InlineKeyboardButton(text='      ', callback_data='None')
back_button = InlineKeyboardButton(text='⬅️Назад', callback_data='get_back')
insta_button = InlineKeyboardButton(text='📷Instagaram', url='https://instagram.com/s.detailing_?igshid=YmMyMTA2M2Y=')

start_keyboard = InlineKeyboardMarkup(row_width=3).row(examples_button, booking_button).row(insta_button)
back_keyboard = InlineKeyboardMarkup(row_width=1).row(back_button)
switch_keyboard = InlineKeyboardMarkup(row_width=3).row(previous_example, blank_button, next_example).row(back_button)
#subscription_keyboard = InlineKeyboardMarkup(row_width=1).row(subscribe_button, unsubscribe_button).add(back_button)
#confirm_unsubscription_keyboard = InlineKeyboardMarkup(row_width=1).row(no_button, yes_button)
