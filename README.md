# Лабораторные работы для 2-го курса ФПЛ  (2019/2020)

В рамках предмета: 
["Программирование для лингвистов"](https://www.hse.ru/edu/courses/292724600) 
в НИУ ВШЭ - Нижний Новгород.

Преподаватели: 

* [Демидовский Александр Владимирович](https://www.hse.ru/staff/demidovs)
* Фатехов Марат Анвярович

План лабораторных работ:

1. Построение частотного словаря по заданному тексту
2. TBD (to be defined)
3. TBD (to be defined)
4. TBD (to be defined)

## Запуск тестов

Для запуска тестов выполните следующую команду:

```bash
python -m unittest discover -p "*_test.py" -s .
```

## Что делать если в родительском репозитории есть изменения и они мне нужны?

1. Создаем `upstream` таргет в репозитории:

```bash
git remote add upstream https://github.com/fipl-hse/2019-2-level-labs
```

2. Получаем данные об изменениях в удаленном репозитории:

```bash
git fetch upstream
```

3. Обновляем свой репозиторий с изменениями из удаленного репозитория:

```bash
git merge upstream/master
```
