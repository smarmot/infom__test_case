import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def dict_sort(my_dict):
    keys = []
    values = []
    my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    for k, v in my_dict:
        keys.append(k)
        values.append(v)
    return (keys, values)


if __name__ == '__main__':
    # Чтение данных
    df = pd.read_csv('data.csv', sep=';',  quotechar='"', low_memory=False)

    # df.info()

    # Сконвертируем Общее время выполния процесса в секунды, добавим новый столбец
    df['time'] = df['Общее_время_выполнения_процесса'].apply(lambda x: int(x.split(':')[0]) * 3600
                                                                       + int(x.split(':')[1]) * 60
                                                                       + int(x.split(':')[2]))

    # Гистограмма Количество_операций_в_выполнении_процесса
    plt.subplots(figsize=(10, 10))
    sns.distplot(df['Количество_операций_в_выполнении_процесса'], bins=10, kde=False)
    plt.grid()
    plt.show()

    # Гистограмма времени выполнения процесса
    plt.subplots(figsize=(10, 10))
    sns.distplot(df['time'], bins=200, kde=False)
    plt.grid()
    plt.show()

    print(df['Региональный_филиал'].value_counts())
    print(df['Населенный_пункт'].value_counts())
    print(df['Код_открытия_обращения'].value_counts())
    print(df['Код_закрытия_обращения'].value_counts())
    print(df['Технология'].value_counts())
    print(df['Услуга'].value_counts())

    # print(df.describe())

    # Распределение количества заявок по коду открытия обращения
    code_open_count = pd.value_counts(df['Код_открытия_обращения'].values, sort=True)
    code_open_count_keys, code_open_count_values = dict_sort(dict(code_open_count))
    plt.yticks(fontsize=7)
    plt.subplots(figsize=(10, 10))
    sns.barplot(x=code_open_count_values, y=code_open_count_keys)
    plt.show()

    # Распределение количества заявок по технологиям
    code_open_count = pd.value_counts(df['Технология'].values, sort=True)
    code_open_count_keys, code_open_count_values = dict_sort(dict(code_open_count))
    plt.yticks(fontsize=10)
    plt.subplots(figsize=(10, 10))
    sns.barplot(x=code_open_count_values, y=code_open_count_keys)
    plt.show()

    # Распределение количества заявок по услугам
    code_open_count = pd.value_counts(df['Услуга'].values, sort=True)
    code_open_count_keys, code_open_count_values = dict_sort(dict(code_open_count))
    plt.yticks(fontsize=7)
    plt.subplots(figsize=(10, 10))
    sns.barplot(x=code_open_count_values, y=code_open_count_keys)
    plt.show()

    # Количество заявок по каждому коду открытия обращения для каждого вида технологии
    # teh = df.pivot_table(index='Технология', columns='Код_открытия_обращения', aggfunc='size', fill_value=0)
    # fig, ax = plt.subplots(figsize=(20, 7))
    # sns.heatmap(teh, fmt='d', annot=True, linewidths=.3, ax=ax, cbar=False, cmap='RdPu')
    # plt.show()

    # teh3 = df.pivot_table(index='Код_открытия_обращения', columns='Код_закрытия_обращения'
    #                       , aggfunc='size', fill_value=0)
    # fig5, ax3 = plt.subplots(figsize=(20, 20))
    # sns.heatmap(teh3, fmt='d', annot=True, annot_kws={"size": 6}, linewidths=.3, ax=ax3, cbar=False, cmap="RdPu")
    # plt.show()

    print(df.groupby(['Технология'])['time'].aggregate('median'))

    print(np.corrcoef(df['Количество_операций_в_выполнении_процесса'], df['time']))






