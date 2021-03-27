from aiogram import Bot, Dispatcher, types, executor
from asyncio import sleep


bot = Bot('1775416764:AAE05rKKLfYuKdRKuh4ytffGMGsHED0Hsko')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет, {message.from_user.username}! Начнем игру!")
    await sleep(1)

    bot_dice_value = await bot.send_dice(message.from_user.id)
    bot_dice_value = bot_dice_value['dice']['value']
    await sleep(4)

    user_dice_value = await bot.send_dice(message.from_user.id)
    user_dice_value = user_dice_value['dice']['value']
    await sleep(4)


    if bot_dice_value > user_dice_value:
        await bot.send_message(message.from_user.id, 'Вы проиграли!')
    elif bot_dice_value < user_dice_value:
        await bot.send_message(message.from_user.id, 'Вы победили')
    else:
        await bot.send_message(message.from_user.id, 'Ничья!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
