# -*- coding: utf-8 -*-
import config
import telebot
import utils
import pandas as pd

class MyPrice:
    total_price = 0

smartphone_df =pd.read_excel('Smartphones.xlsx')
watch_df =pd.read_excel('Watch.xlsx')


smartphone = []

watch = []
for i in range(0,smartphone_df.shape[0]):
    new_smart = utils.Smartphone(smartphone_df['Бренд'][i],smartphone_df['Модель'][i],smartphone_df['Процессор'][i],smartphone_df['Хранилище'][i],smartphone_df['Оперативная память'][i],smartphone_df['Телефото'][i],smartphone_df['Сверхширокоугольная'][i],smartphone_df['Цена'][i])
    smartphone.append(new_smart)

for i in range(0,watch_df.shape[0]):
    new_watch = utils.Watch(watch_df['Бренд'][i],watch_df['Модель'][i],watch_df['Always on'][i],watch_df['Цена'][i])
    watch.append(new_watch)



bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, 'Добрый день. Вас приветствует консультант по выбору портативных девайсов. Нажмите /store чтобы начать покупки')



@bot.message_handler(commands=['store'])
def shop(message):

    # Формируем разметку
    markup = utils.generate_markup_type(utils.types)
    # Отправляем аудиофайл с вариантами ответа
    bot.send_message(message.chat.id, 'Выберете тип техники, которая вам интересна',reply_markup=markup)


@bot.callback_query_handler(func=lambda c: c.data)
def process_callback(callback_query: telebot.types.CallbackQuery):

    options = []


    if callback_query.data.startswith("types"):
        device = callback_query.data[5:]
        if device == 'Smartphone':
            options.append('Бренд')
            options.append('Модель')
            options.append('Процессор')
            options.append("Хранилище")
            options.append("Оперативная память")
            options.append("Телефото")
            options.append("Сверхширокоугольная")
            options.append("Цена")

        elif device == 'Watch':
            options.append('Бренд')
            options.append('Модель')
            options.append("Always on display")
            options.append("Цена")
        markup = utils.generate_markup_opt(options, device)
        bot.send_message(callback_query.message.chat.id, 'Выберете параметр, с каким вам необходим смартфон',
                         reply_markup=markup)
    elif callback_query.data.startswith("options"):
        device = callback_query.data[7:12]
        features = []
        if device == 'Watch':
            option = callback_query.data[12:]

            if option == 'Бренд':

                for i in watch:
                    if i.brand not in features:
                        features.append(i.brand)

            elif option == 'Модель':

                for i in watch:
                    if i.model not in features:
                        features.append(i.model)

            elif option == 'Always on display':

                for i in watch:
                    if i.display not in features:
                        features.append(i.display)

            elif option == "Цена":

                for i in watch:
                    if i.price not in features:
                        features.append(i.price)

        else:
            option = callback_query.data[17:]

            if option == 'Бренд':

                for i in smartphone:
                    if i.brand  not in features:
                        features.append(i.brand)

            elif option == 'Модель':

                for i in smartphone:
                    if i.model not in features:
                        features.append(i.model)

            elif option == 'Процессор':

                for i in smartphone:
                    if i.processor not in features:
                        features.append(i.processor)

            elif option == 'Хранилище':

                for i in smartphone:
                    if i.storage not in features:
                        features.append(i.storage)

            elif option == 'Оперативная память':
                for i in smartphone:
                    if i.ram not in features:
                        features.append(i.ram)

            elif option == 'Телефото':
                for i in smartphone:
                    if i.tele not in features:
                        features.append(i.tele)

            elif option == 'Сверхширокоугольная':
                for i in smartphone:
                    if i.wide not in features:
                        features.append(i.wide)

            elif option == "Цена":
                for i in smartphone:
                    if i.price not in features:
                        features.append(i.price)
        markup = utils.generate_markup_feature(features,device,option)
        bot.send_message(callback_query.message.chat.id, option,
                         reply_markup=markup)

    elif callback_query.data.startswith("feature"):
        device = callback_query.data[7:12]
        result = []
        if device =='Watch':

            if callback_query.data[12:17] == 'Бренд':
                for i in watch:
                    if i.brand == callback_query.data[17:]:
                        result.append(i)


            elif callback_query.data[12:18] == 'Модель':

                for i in watch:
                    if i.model == callback_query.data[18:]:
                        result.append(i)

            elif callback_query.data[12:29] == 'Always on display':

                for i in watch:
                    if i.display == callback_query.data[29:]:
                        result.append(i)

            elif callback_query.data[12:16] == "Цена":

                for i in watch:
                    if i.price <= int(callback_query.data[16:]):
                        result.append(i)
        else:

            if callback_query.data[12:17] == 'Бренд':
                for i in smartphone:
                    if i.brand == callback_query.data[17:]:
                        result.append(i)

            elif callback_query.data[12:18] == 'Модель':

                for i in smartphone:
                    if i.model == callback_query.data[18:]:
                        result.append(i)

            elif callback_query.data[12:21] == 'Процессор':

                for i in smartphone:
                    if i.processor == callback_query.data[21:]:
                        result.append(i)

            elif callback_query.data[12:21] == 'Хранилище':

                for i in smartphone:
                    if str(i.storage) == callback_query.data[21:]:
                        result.append(i)

            elif callback_query.data[12:30] == 'Оперативная память':
                for i in smartphone:
                    if str(i.ram) == callback_query.data[30:]:
                        result.append(i)

            elif callback_query.data[12:20] == 'Телефото':
                for i in smartphone:
                    if i.tele == callback_query.data[20:]:
                        result.append(i)

            elif callback_query.data[12:31] == 'Сверхширокоугольная':
                for i in smartphone:
                    if i.wide == callback_query.data[31:]:
                        result.append(i)
            elif callback_query.data[12:16] == "Цена":
                for i in smartphone:
                    if i.price <= int(callback_query.data[16:]):
                        result.append(i)
        markup = utils.generate_markup_result(result)
        bot.send_message(callback_query.message.chat.id, 'Кликните по девайсу, чтобы добавить его в корзину.',
                         reply_markup=markup)
        bot.send_message(callback_query.message.chat.id, 'Если вас интересует другой товар, пожалуйста, нажмите /store')

    elif callback_query.data.startswith("result"):
        MyPrice.total_price += int(callback_query.data[6:])
        bot.send_message(callback_query.message.chat.id, 'Нажмите /buy ,чтобы перейти в корзину. \nНажмите /store ,чтобы продолжить покупки ',)


    bot.answer_callback_query(callback_query.id)



@bot.message_handler(commands=['buy'])
def game(message):

    bot.send_message(message.chat.id, 'Текущая стоимость вашего заказа - '+ str(MyPrice.total_price)+' Нажмите /reset , чтобы очистить корзину. Нажмите /store , чтобы продолжить покупки')

@bot.message_handler(commands=['reset'])
def res(message):
    MyPrice.total_price = 0
    bot.send_message(message.chat.id, 'Корзина очищена! ')


'''
@bot.message_handler(func=lambda message: True, content_types=['text'])
def game(message):
    answer = utils.get_type_answer(message.text)
    if not answer:
        bot.send_message(message.chat.id, 'Чтобы начать покупки, нажмите /shop')
    else:
        if answer:

            bot.send_message(message.chat.id, 'Введите правильный вариант')
'''

if __name__ == '__main__':
    bot.infinity_polling()