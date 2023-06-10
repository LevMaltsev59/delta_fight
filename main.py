# -*- coding: utf-8 -*-
import random
from sys import exit

if __name__ == '__main__':

    print(
        '''
        Это версия боёв 2.5. Здесь вы уже будите сражаться в команде против 1 сильного врага
          Кпопки:
          А - Атака
          З - ЗАЩИТА (-15 урона)
          М - МАГИЯ
          Д - ДЕЙСТВИЕ
          П - ПОЩАДА
        ==== Персонажи ===
        В вашей команде 3 персонажа:
        Крис: Мечник. 50 здоровья и атака от 20-40. Действие - говорить, добавляет +10% к пощаде. Магия - отсутствует
        Сьюзи: Очень сильный боец с секирой, 150 здоровья, атака от 60-90. Действие - нагрубить, -5% к пощаде. 
            Магия - ярый взмах, тратит 50 магии
        Ральзей: Персонаж-маг, 30 здоровья. Бьёт от 10-30, действие - говорить, +25 к пощаде. 
            Магия - излечение, востанавливает 25 здоровья выбраному бойцу
        Ноэль: Персонаж абсолютно не умеющий драться, 65 здоровья, атакует от 5-10 единиц урона, 
            действие - подбодрить, +5 защиты к выбранному участнику, Магия - фокус, 
            хоть фокус не являеться магией зато он отлично веселит врага, +20% к пощаде. А ещё он отнимает 10 маны
        
        К сожалению, вы можите выбрать либо Сьюзи либо Ноэль (Напишите С или Н)
        ''')

    SN = input("")
    if SN == "С":
        Seazy = True
        Noel = False
    if SN == "Н":
        Noel = True
        Seazy = False
        if SN == "С" or SN == "Н":
            print("А, ещё момент. Какая будет сложность? (Напишите любую букву из списка: Л Н С)")
            Xz = input()
            if Xz == 'Л':
                print("У Вимсалота 500 ОЗ")
                Vumsalot = 500
            if Xz == "Н":
                print("У Вимсалота 1000 ОЗ")
                Vumsalot = 1000
            if Xz == "С":
                print("У Вимсалота 2500 ОЗ")
                Vumsalot = 1500
                print("Любитель хард-кора? Ладно.")

    Krus = True
    Ralsey = True
    Mersy = 0
    many = 200
    Krus_hp = 50
    Seaze_hp = 150
    Ralsey_hp = 30
    deff_1 = 0
    deff_2 = 0
    deff_3 = 0
    deff_4 = 0
    Noel_hp = 65
    print(
        "Команды находяться в самом начале, если вы хотите атаковать то просто напишите допустим А, промотайте в самый низ если вы не помните или забыли, если команда будет введенна не верно то ваш ход просто пропуститься, сообщения будут вылазить если вы напишите команду верно, если-же команда будет не верная то ничего не напишет и ход перейдёт следующему участнику (если он жив), а если он мёртв то снова вам."
        "Бой начинаеться!")
    while True:
        if Krus == True:
            print("Ход Криса!")
            hod = input("")
            if hod == "А":
                Xz = random.randint(19, 41)
                Vumsalot -= Xz
                print(f"Вы атаковали Вимсалота на {Xz} единиц урона!")
            if hod == "З":
                print("Вы повысили защиту")
                deff_1 = 15
            if hod == "Д":
                Mersy += 10
            if hod == "П":
                if Mersy < 100:
                    print("Слишком мало очков пощады что-бы пощадить Вимсалота")
                if Mersy >= 100:
                    print("Вы пощадили Вимсалота!")
                    exit()
        print("==============")
        if Seazy == True:
            print("Ход Сьюзи!")
            hod = input("")
            if hod == "А":
                Xz = random.randint(59, 91)
                Vumsalot -= Xz
                print(f"Вы атаковали Вимсалота на {Xz} единиц урона!")
            if hod == "З":
                print("Вы повысили защиту")
                deff_2 = 15
            if hod == "Д":
                Mersy -= 5
                print(
                    "Cьюзи нагрубила Вимсалоту. Вимсалот разозлися как и Сьюзи, Вимсалоту бьёт на 5 единиц урона больше а Сьюзи атакует на 10 единиц урона.")
                if hod == "П":
                    if Mersy < 100:
                        print("Слишком мало очков пощады что-бы пощадить Вимсалота")
                    if Mersy >= 100:
                        print("Вы пощадили Вимсалота!")
                        exit()
            if hod == "М":
                if many < 50:
                    print("У вас не достаточно маны.")
                if many >= 50:
                    print("УМРИ!")
                    Xz = random.randint(119, 201)
                    many -= 50
                    print(
                        f"С этими словами Сьюзи мощно ударила по Вимсалоту в {Xz} единиц урона своей Секирой и тяжело дыша отскачила назад")
        if Noel == True:
            print("Ход Ноэль!")
            hod = input("")
            if hod == "А":
                Xz = random.randint(4, 11)
                Vumsalot -= Xz
                print(f"Вы атаковали Вимсалота на {Xz} единиц урона!")
            if hod == "З":
                print("Вы повысили защиту")
                deff_4 = 15
            if hod == "Д":
                Mersy += 25
                print("Ноэль подбадривает...")
                hod = input("К, Н, Р?:")
                if hod == "К":
                    print("Криса!")
                    Krus_hp += 5
                if hod == "Н":
                    print("Cебя! (Пожалуйста, не спрашивайте как это работает.)")
                    Noel_hp += 5
                if hod == "Р":
                    print("Ральзея!")
                    Ralsey_hp += 5
                if hod == "П":
                    if Mersy < 100:
                        print("Слишком мало очков пощады что-бы пощадить Вимсалота")
                    if Mersy >= 100:
                        print("Вы пощадили Вимсалота!")
                        exit()
            if hod == "М":
                if many < 10:
                    print("У вас не достаточно маны.")
                if many >= 10:
                    print("Ноэль показала фокус Вимсалоту, он посмеялся")
                    Mersy += 20
        if Ralsey == True:
            print("Ход Ральзея!")
            hod = input("")
            if hod == "А":
                Xz = random.randint(9, 31)
                Vumsalot -= Xz
                print(f"Вы атаковали Вимсалота на {Xz} единиц урона!")
            if hod == "З":
                print("Вы повысили защиту")
                deff_3 = 15
            if hod == "Д":
                Mersy += 25
                print("Ральзей вежливо пообщался с Вимсалотом.")
                if hod == "П":
                    if Mersy < 100:
                        print("Слишком мало очков пощады что-бы пощадить Вимсалота")
                    if Mersy >= 100:
                        print("Вы пощадили Вимсалота!")
                        exit()
            if hod == "М":
                if many < 25:
                    print("У вас не достаточно маны.")
                if many > 25:
                    print("Ральзей использует магию излечения на...")
                    if SN == "С":
                        hod = input("К, С, Р?:")
                        if hod == "К":
                            print("Крисе")
                            Krus_hp += 25
                        if hod == "С":
                            Seaze_hp += 25
                            print("Сьюзи")
                        if hod == "РС":
                            print("Себе")
                            Ralsey_hp += 25
                    if SN == "Н":
                        hod = input("К, Н, Р?:")
                        if hod == "К":
                            print("Крисе")
                            Krus_hp += 25
                        if hod == "Н":
                            Noel_hp += 25
                            print("Ноэль")
                        if hod == "Р":
                            print("Себе")
                            Ralsey_hp += 25
                    many -= 25
        print("Вимсалот атакует...")
        Xz = random.randint(1, 3)
        if Xz == 1 and Krus == True:
            Krus_hp -= 25
            Krus_hp += deff_1

        if Xz == 2 and Seazy == True or Noel == True:
            if Seazy == True:
                print("Сьюзи!")
                Seaze_hp -= 25
                Seaze_hp += deff_2
            if Noel == True:
                print("Ноэль!")
                Noel_hp -= 25
                Noel_hp += deff_4

        if Xz == 3 and Ralsey == True:
            print("Ральзея!")
            Ralsey_hp -= 25
            Ralsey_hp += deff_3
        print("Параметры")
        if SN == ("С"):
            print("Здоровье (К С Р   В)")
            print(Krus_hp)
            print(Seaze_hp)
            print(Ralsey_hp)
        if SN == ("Н"):
            print("Здоровье (К Н Р   В)")
            print(Krus_hp)
            print(Noel_hp)
            print(Ralsey_hp)

        print(Vumsalot)
        print("Уровень пощады:")
        print(Mersy)
        print("Мана:")
        print(many)
        print("Следующий круг!")
        if Krus_hp <= 0:
            Krus = False
        if Ralsey_hp <= 0:
            Ralsey = False
        if Seaze_hp <= 0:
            Seazy = False
        if Noel_hp <= 0:
            Noel = False
        if Vumsalot <= 0:
            print("Поздравляю, вы победили Вимсалота и выиграли")
            exit(0)
        if SN == "C":
            if Krus <= False and Ralsey <= False and Seazy <= False:
                print("Все ваши персонажи погибли, вы проиграли")
                exit(0)
        if SN == "Н":
            if Krus <= False and Noel <= False and Seazy <= False:
                print("Все ваши персонажи погибли, вы проиграли")
                exit(0)


p