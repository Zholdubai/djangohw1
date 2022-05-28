from django.shortcuts import render

import datetime

from django.shortcuts import render
from django.http import HttpResponse
now = datetime.datetime.now().replace(microsecond=0)

def index(request):
    return HttpResponse('<h1 style="color:red;">ЭТО ГЛАВНАЯ СТРАНИЦА!</h1>')

def test1(request):
    dict_={
        'title': 'Science app',
        'text': 'rwrwrwr'
    }
    return render(request, template_name='index.html', context=dict_)

def tes2(request):
    dict_={
        'title': 'Как создать сайт?',
        'text': 'Перед вами — очень простое руководство о том, как всего за час сделать сайт с нуля.'

'Чтобы создать сайт, нужно выполнить всего три простых шага:'

'1. Выбрать платформу для сайта'
'2. Выбрать доменное имя (www.) и хостинг'
'3. Настроить и кастомизировать сайт'
    }
    return render(request, template_name='index.html', context=dict_)


def tes3(request):
    dict_={
        'title': 'Продающий слоган',
        'text': 'Как только потенциальный клиент заходит на ваш сайт, он уже подсознательно ищет то,'
                ' что может приковать его внимание, смотивирует остаться на странице. '
                'Это может быть картинка, логотип компании, приветственные слова, а еще лучше - запоминающийся слоган или девиз. Совсем необязательно бросаться обещаниями о том, что за пару дней у заказчика будет готовый сайт и система привлечения клиентов. '
                'Сейчас это вызывает скорее отторжение, чем интерес.'
    }
    return render(request, template_name='index.html', context=dict_)


def tes4(request):
    dict_={
        'title': 'Полезная информация',
        'text': 'Прежде, чем приступить к написанию продающего текста для сайта, нам необходимо понять, кто является нашей целевой аудиторией. '
                'Только так мы сможем определить, какую именно информацию мы хотим до нее донести и будет ли эта информация представлять ценность для потенциального потребителя. '
                'В первую очередь стоит акцентировать внимание человека на том, что подтолкнет его к принятию решения.',
        'data': f"{now}"


    }
    return render(request, template_name='index.html', context=dict_)