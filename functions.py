import pandas as pd

def file_open(path):
    print(path)
    print(type(path))
    data_file = pd.read_excel(path).to_dict()  # Считываем файл и переводим его в словарь
    columns_list = data_file.keys()  # Получаем список названий колонок, чтобы потом можно было выбрать
    columns_pos = dict(enumerate([i for i in columns_list]))  # Создаем словарь позиция: название колонки
    return None




def main_algorithm(external_id_dict: dict, id_list=[], columns_num_list=[], errors_list=[]):
    '''
    Тут описан основной алгоритм проверки ID покупок, чтобы они шли последовательно
    :param external_id_dict: Словарь, где ключ - позиция элемента, а значение - проверяемый ID
    :param id_list: Пустой список, для некорректных ID
    :param columns_num_list: Пустой список, для номеров строк с некорректным ID
    :param errors_list: Пустой список, для ошибки
    :return: Кортеж с номером строки, ID и ошибкой
    '''

    def dtf_lists(row_numb: int, order_id: str, error: str):
        '''
        Функция, которая добавляет в списки нужные значения
        :param row_numb: Числовая переменная, с индексм ID в external_id_dict
        :param order_id: Текстовая переменная. Содержит ID заказа
        :param error: Текстовая переменная. Содержит текст ошибки
        :return: None
        '''
        columns_num_list.append(row_numb + 1)
        id_list.append(order_id)
        errors_list.append(error)
        return None

    # Основной алгоритм проверки
    ex_id_values = list(external_id_dict.values())  # Создаем список из значений словаря с уникальными id
    ex_id_counter = {value: ex_id_values.count(value) for value in
                     set(ex_id_values)}  # Создаем словарь, где ключ-id, значение-кол-во вхождений
    id_in_early = {value: False for value in set(ex_id_values)}  # Словарь ID входили ли они ранее в файл
    for ex_id_key, ex_id_value in external_id_dict.items():  # Цикл прохода по каждому значению словаря
        if id_in_early[ex_id_value] is False:  # Проверяем, что не входил
            if ex_id_counter[ex_id_value] > 1:  # Если id входит больше 1 раза, то запускаем проверку
                if ex_id_key == 0:  # Проверяем, равен ли индекс 0
                    if external_id_dict[
                        ex_id_key + 1] != ex_id_values:  # Проверяем следующий элемент равен этому или нет
                        dtf_lists(ex_id_key, ex_id_value, error='Не на своем месте')

                elif ex_id_key == len(external_id_dict) - 1:  # Проверяем последний ли это элемент
                    if external_id_dict[ex_id_key - 1] != ex_id_value:  # Проверяем равен ли id предыдущему
                        dtf_lists(ex_id_key, ex_id_value, error='Не на своем месте')

                else:
                    if (ex_id_value != external_id_dict[ex_id_key - 1] and ex_id_value != external_id_dict[
                        ex_id_key + 1] and
                            id_in_early[ex_id_value] is True):  # Проверяем равен ли id соседним
                        dtf_lists(ex_id_key, ex_id_value, error='Не на своем месте')

            if ex_id_key < len(external_id_dict) - 1 and ex_id_value != external_id_dict[
                ex_id_key + 1]:  # Если следующее значение отличается, то влагаем, что оно уже было в списке
                id_in_early[ex_id_value] = True
        else:
            columns_num_list.append(ex_id_key + 1)
            id_list.append(ex_id_value)
            errors_list.append('Не на своем месте')
    return columns_num_list, id_list, errors_list


