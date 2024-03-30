**ЭКГ** - повсеместно распространенный метод изучения работы сердца, в основе которого лежит графическое изображение электрических импульсов сердца. Электрокардиограф измеряет интенсивность сокращений сердечной мышцы и преобразует их в графическое изображение (на ленте в виде зубцов). По результатам определяется отсутствие или наличие отклонений в работе сердца.

Но при этом есть общенаучный факт, что на работу сердца, а также на график ЭКГ влияют следующие параметры: 
1. Возраст
2. Пол
3. Тип боли в груди (всего 4 вида боли)
4. Артериальное давление
5. Максимальный пульс
6. Бывала ли стенокардия, вызванная сильными физическими нагрузкам

**Стоит отметить, что так как сердце диабетиков работает по-другомму, то корректно с высокой точностью их паталогии сердца в их случаях не получится (точноть модели у диабетиков ~53%) **

**Инстурменты проекта: **
1. NumPy
2. Pandas
3. Sklearn 
4. Telebot
5. Matplotlib

**База данных включает в себе около 300 пациентов,  человек имеют паталогии сердца, в БД 81 женщина и 213 мужчин, возраст всех участников от 23 до 66 лет.** 

Лучшая точность на данный момент достигает метод классификации **Random Tree**. (Accurasy score 0.814). 
Телеграмм бот был создан с помощью модуля Telebot. 

**Ссылку на телеграмм бота вы можете найти сверху гита**