from django.shortcuts import render
from .models import Category, Complex, Side, Repair, Portfolio, Call
import os
from django.utils import timezone
from repairMyRoom.forms import CallForm


def index(request):
    complex_all = Complex.objects.all()
    repair_all = Repair.objects.all()
    repair_main = Repair.objects.filter(main=True)
    portfolio = Portfolio.objects.all()
    category_all = Category.objects.all()

    if request.method == 'POST':
        form = CallForm(data=request.POST)
        # if form.is_valid():
        #     call = Call(client=request.POST.get("name"), phone=request.POST.get("phone"), date=timezone.now())
        #     call.save()
    else:
        form = CallForm(data=request.POST)


    return render(request, 'index.html', context={'complex_all': complex_all,
                                                  'repair_all': repair_all,
                                                  'repair_main': repair_main,
                                                  'category_all': category_all,
                                                  'portfolio': portfolio,
                                                  'form': form})


def managment(request):
    if request.method == 'POST':
        if request.POST.get("complex"):
            Complex.objects.all().delete()
            for com in complex:
                comp = Complex(complex=com[0], description=com[1], price=com[2])
                comp.save()
        elif request.POST.get("repair"):
            Repair.objects.all().delete()
            Category.objects.all().delete()
            Side.objects.all().delete()
            for s in side:
                si = Side(side=s)
                si.save()
            for ci in category:
                ca = Category(category=ci)
                ca.save()
            for re in repair:
                rep = Repair(repair=re[0],
                             recat=Category.objects.get(category=re[1]),
                             reside=Side.objects.get(side=re[2]),
                             main=re[3],
                             price=re[4],
                             unit=re[5])
                rep.save()
        elif request.POST.get("portfolio"):
            Portfolio.objects.all().delete()
            for file in os.listdir('static/portfolio'):
                port = Portfolio(picture='static/portfolio/'+file, text='-')
                port.save()


    return render(request, 'managment.html')







category = ['Демонтажные работы',
            'Электрика',
            'Черновые отделочные работы',
            'Чистовые отделочные работы',
            'Подготовительные работы']

side = ['полы', 'стены', 'потолки', 'окна', 'прочие', 'сантех', 'электр', 'откосы', 'двери', 'подг']




complex = [['Косметический ремонт квартиры',
           '(входит: демонтаж существующих покрытий; поклейка обоев; окраска потолков; укладка ламината; монтаж плинтусов)',
           '3190'],
            ['Капитальный ремонт квартиры',
           '(входит: демонтаж существующих покрытий; выравнивание пола; частичная штукатурка стен; грунтовка пола, стен и потолка; шпаклевка стен; поклейка обоев; окраска потолков; укладка ламината; монтаж плинтусов)',
           '4770'],
            ['Ремонт квартиры под ключ',
           '(входит: демонтаж существующих покрытий; поклейка обоев; окраска потолков; укладка ламината; монтаж плинтусов. ВСЕ МАТЕРИАЛЫ ВКЛЮЧЕНЫ В СТОИМОСТЬ)',
           '5620'],
            ['Евроремонт квартиры',
           '(входит: демонтаж существующих покрытий; стяжка пола; штукатурка стен; выравнивание потолка; замена электрики; грунтовка пола, стен и потолка; шпаклевка стен и потолка; поклейка обоев; окраска потолков; укладка паркетной доски; монтаж плинтусов; замена батарей; влажная уборка помещения)',
           '6850'],
          ]
repair = [['Демонтаж плинтуса',
           'Демонтажные работы',
           'полы',
           'False',
           '58',
           'м/п'],
            ['Демонтаж ламината, паркетной доски',
           'Демонтажные работы',
           'полы',
           'False',
           '80',
           'м2'],
          ['Демонтаж фанеры, ДВП',
           'Демонтажные работы',
           'полы',
           'False',
           '69',
           'м2'],
          ['Демонтаж деревянных полов',
           'Демонтажные работы',
           'полы',
           'False',
           '178',
           'м2'],
          ['Демонтаж лаг',
           'Демонтажные работы',
           'полы',
           'False',
           '91',
           'м2'],
          ['Демонтаж стяжки до 3 см',
           'Демонтажные работы',
           'полы',
           'False',
           '281',
           'м2'],
          ['Снятие обоевм',
           'Демонтажные работы',
           'стены',
           'False',
           '71',
           'м2'],
          ['Снятие побелки',
           'Демонтажные работы',
           'стены',
           'False',
           '138',
           'м2'],
          ['Очистка краски со стен',
           'Демонтажные работы',
           'стены',
           'False',
           '138',
           'м2'],
          ['Очистка стен от шпаклевки',
           'Демонтажные работы',
           'стены',
           'False',
           '138',
           'м2'],
          ['Ошкуривание поверхности',
           'Демонтажные работы',
           'стены',
           'False',
           '100',
           'м2'],
          ['Отбивка штукатурки со стен',
           'Демонтажные работы',
           'стены',
           'False',
           '223',
           'м2'],
          ['Демонтаж стен (перегородок) из кирпича',
           'Демонтажные работы',
           'стены',
           'False',
           '566',
           'м2'],
          ['Демонтаж стен из ацеида, гипсолита, ГКЛ',
           'Демонтажные работы',
           'стены',
           'False',
           '338',
           'м2'],
          ['Демонтаж натяжного потолка',
           'Демонтажные работы',
           'потолки',
           'False',
           '69',
           'м2'],
          ['Демонтаж подвесных потолков ГКЛ',
           'Демонтажные работы',
           'потолки',
           'False',
           '166',
           'м2'],
          ['Очистка побелки',
           'Демонтажные работы',
           'потолки',
           'False',
           '183',
           'м2'],
          ['Очистка краски ВЭ',
           'Демонтажные работы',
           'потолки',
           'False',
           '149',
           'м2'],
          ['Снятие обоев',
           'Демонтажные работы',
           'потолки',
           'False',
           '71',
           'м2'],
          ['Демонтаж деревянной двери',
           'Демонтажные работы',
           'двери',
           'False',
           '366',
           'м2'],
          ['Демонтаж оконного блока',
           'Демонтажные работы',
           'окна',
           'False',
           '452',
           'м2'],
          ['Демонтаж подоконников',
           'Демонтажные работы',
           'окна',
           'False',
           '263',
           'м/п'],
          ['Демонтаж вент. решеток',
           'Демонтажные работы',
           'прочие',
           'False',
           '69',
           'шт'],
          ['Демонтаж воздуховодов',
           'Демонтажные работы',
           'прочие',
           'False',
           '138',
           'м/п'],
          ['Очистка радиатора от краски',
           'Демонтажные работы',
           'прочие',
           'False',
           '1133',
           'шт'],
          ['Демонтаж смесителя',
           'Демонтажные работы',
           'сантех',
           'False',
           '279',
           'шт'],
          ['Демонтаж душевой кабины',
           'Демонтажные работы',
           'сантех',
           'False',
           '749',
           'шт'],
          ['Демонтаж ванны',
           'Демонтажные работы',
           'сантех',
           'False',
           '869',
           'шт'],
          ['Демонтаж раковины',
           'Демонтажные работы',
           'сантех',
           'False',
           '434',
           'шт'],
          ['Демонтаж унитаза',
           'Демонтажные работы',
           'сантех',
           'False',
           '566',
           'шт'],
          ['Демонтаж полотенцесушителя',
           'Демонтажные работы',
           'сантех',
           'False',
           '543',
           'шт'],
          ['Демонтаж труб в/с',
           'Демонтажные работы',
           'сантех',
           'False',
           '208',
           'м/п'],
          ['Демонтаж труб канализации',
           'Демонтажные работы',
           'сантех',
           'False',
           '263',
           'м/п'],
          ['Демонтаж розеток и выключателей',
           'Электрика',
           'электр',
           'False',
           '98',
           'шт'],
          ['Демонта люстры',
           'Электрика',
           'электр',
           'False',
           '246',
           'шт'],
          ['Демонтаж электрокабеля',
           'Электрика',
           'электр',
           'False',
           '23',
           'м/п'],
          ['Грунтовка пола',
           'Черновые отделочные работы',
           'полы',
           'False',
           '52',
           'м2'],
          ['Устройство наливных полов',
           'Черновые отделочные работы',
           'полы',
           'False',
           '304',
           'м2'],
          ['Устройство стяжки по маякам',
           'Черновые отделочные работы',
           'полы',
           'False',
           '434',
           'м2'],
          ['Устройство тепло/звукоизоляции',
           'Черновые отделочные работы',
           'полы',
           'False',
           '160',
           'м2'],
          ['Укладка фанеры',
           'Черновые отделочные работы',
           'полы',
           'False',
           '270',
           'м2'],
          ['Штукатурка стен по маякам гипсовой смесью',
           'Черновые отделочные работы',
           'стены',
           'True',
           '511',
           'м2'],
          ['Штукатурка стен (под правило)',
           'Черновые отделочные работы',
           'стены',
           'False',
           '396',
           'м2'],
          ['Грунтовка стен',
           'Черновые отделочные работы',
           'стены',
           'False',
           '52',
           'м2'],
          ['Шпатлевка стен под оклейку обоями (с ошкуриванием)',
           'Черновые отделочные работы',
           'стены',
           'False',
           '331',
           'м2'],
          ['Устройство перегородок из ГКЛ',
           'Черновые отделочные работы',
           'стены',
           'True',
           '652',
           'м2'],
          ['Грунтовка откосов, углов',
           'Черновые отделочные работы',
           'откосы',
           'False',
           '50',
           'м/п'],
          ['Штукатурка откосов',
           'Черновые отделочные работы',
           'откосы',
           'False',
           '350',
           'м/п'],
          ['Утепление откосов',
           'Черновые отделочные работы',
           'откосы',
           'False',
           '98',
           'м/п'],
          ['Штукатурка потолка по маякам',
           'Черновые отделочные работы',
           'потолки',
           'False',
           '592',
           'м2'],
          ['Грунтовка потолков',
           'Черновые отделочные работы',
           'потолки',
           'False',
           '73',
           'м2'],
          ['Шпатлевка потолков под покраску',
           'Черновые отделочные работы',
           'потолки',
           'True',
           '565',
           'м2'],
          ['Укладка ламината',
           'Чистовые отделочные работы',
           'полы',
           'True',
           '378',
           'м2'],
          ['Укладка паркетной доски',
           'Чистовые отделочные работы',
           'полы',
           'False',
           '459',
           'м2'],
          ['Настил линолеума бытового, ковролина',
           'Чистовые отделочные работы',
           'полы',
           'True',
           '258',
           'м2'],
          ['Монтаж плинтусов',
           'Чистовые отделочные работы',
           'полы',
           'False',
           '143',
           'м/п'],
          ['Оклейка стен обоями',
           'Чистовые отделочные работы',
           'стены',
           'True',
           '290',
           'м2'],
          ['Облицовка плиткой стен',
           'Чистовые отделочные работы',
           'стены',
           'True',
           '876',
           'м2'],
          ['Облицовка стен ПВХ панелями (свыше 10м2)',
           'Чистовые отделочные работы',
           'стены',
           'False',
           '515',
           'м2'],
          ['Окраска стен в 2 слоя',
           'Чистовые отделочные работы',
           'стены',
           'True',
           '223',
           'м2'],
          ['Окраска откосов, углов',
           'Чистовые отделочные работы',
           'откосы',
           'False',
           '173',
           'м/п'],
          ['Окраска потолков',
           'Чистовые отделочные работы',
           'потолки',
           'False',
           '258',
           'м2'],
          ['Устройство натяжных потолков',
           'Чистовые отделочные работы',
           'потолки',
           'True',
           '330',
           'м2'],
          ['Установка двери деревянной',
           'Чистовые отделочные работы',
           'двери',
           'False',
           '3850',
           'шт'],
          ['Установка двери металлической',
           'Чистовые отделочные работы',
           'двери',
           'False',
           '5940',
           'шт'],
          ['Окраска окна',
           'Чистовые отделочные работы',
           'окна',
           'False',
           '572',
           'м2'],
          ['Установка подоконников',
           'Чистовые отделочные работы',
           'окна',
           'False',
           '686',
           'м/п'],
          ['Установка розеток',
           'Чистовые отделочные работы',
           'электр',
           'True',
           '258',
           'шт'],
          ['Прокладка кабеля',
           'Чистовые отделочные работы',
           'электр',
           'False',
           '66',
           'м/п'],
          ['Установка люстры',
           'Чистовые отделочные работы',
           'электр',
           'False',
           '824',
           'шт'],
          ['Установка звонка',
           'Чистовые отделочные работы',
           'электр',
           'False',
           '361',
           'шт'],
          ['Установка ванны',
           'Чистовые отделочные работы',
           'сантех',
           'False',
           '3587',
           'шт'],
          ['Установка раковины',
           'Чистовые отделочные работы',
           'сантех',
           'True',
           '1304',
           'шт'],
          ['Установка унитаза',
           'Чистовые отделочные работы',
           'сантех',
           'False',
           '2174',
           'шт'],
          ['Установка душа',
           'Чистовые отделочные работы',
           'сантех',
           'False',
           '626',
           'шт'],
          ['Прокладка труб водоснабжения',
           'Чистовые отделочные работы',
           'сантех',
           'False',
           '326',
           'м/п'],
          ['Укрытие пленкой',
           'Подготовительные работы',
           'подг',
           'False',
           '18',
           'м2'],
          ['Разгрузка материала',
           'Подготовительные работы',
           'подг',
           'False',
           '1716',
           'т'],



          ]
















