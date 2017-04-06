#! /usr/bin/env python
# -*- coding: utf-8 -*-
import io
import json
import time


class JsonParser:
    def __init__(self):
        self.__parsed_string = ''
        self.__user_answers = []
        self.matching_technologies = {}

    # Функция для парсинга json файла
    def open_file(self, path):
        string_to_parse = ''
        with io.open(path, encoding='utf-8') as json_file:
            for line in json_file:
                string_to_parse += line
        self.__parsed_string = json.loads(string_to_parse)

    # Парсим "базу знаний"
    def parse_question_file(self, path='JSON files/questions.json'):
        self.open_file(path=path)

        for element in self.__parsed_string:
            print("____________________________")
            print(element['QuestionValue'])

            # Выводим варианты ответов
            for subelement in element['Answers']:
                print("{0}: {1}".format(subelement['AnswerId'], subelement['AnswerValue']))

            # Получаем ответы пользователя
            user_answer = input("Ответ: ")

            # Записываем ответы пользователя в "лист""          
            # Сокращенная версия кода ниже
            self.__user_answers.extend(answer['AnswerValue'] for answer in element['Answers'] if str(answer['AnswerId']) == user_answer)
            # for yx in x['Answers']:
            #     if str(yx['AnswerId']) == str(answer):
            #         self.__user_answers.append(yx['AnswerValue'])

        print('------------------------------')
        print("Ваши ответы: ")
        for answer in self.__user_answers:
            print(answer)
        print('------------------------------')

    def parse_answer_file(self, path='JSON files/answer.json'):
        self.open_file(path)
        for element in self.__parsed_string:
            matches = 0
            count = 0
            for tags in element['tags']:
                count += 1
                for ans in self.__user_answers:
                    if ans == tags == "Веб-приложение":
                        matches += 10
                    elif str(ans).lower() == str(tags).lower():
                        matches += 1
                    else:
                        continue

            if matches > 0:
                technology = element['technology']
                self.matching_technologies[matches] = technology

    def print_matching_tech(self):
        print("")
        print("Подбираю Наиболее подходящие технологии...")
        print("")
        time.sleep(1.5)
        print("------------------------------------")
        print("Все подходящие варианты: ")
        print("")
        time.sleep(0.5)
        for number in self.matching_technologies:
            print("Технология - {0}, коэфициент совпадения - {1}".format(self.matching_technologies[number], number))
            time.sleep(.5)

        print("")
        print("------------------------------------")
        print("Оптимально подходящая технология для вас это: {0}".format(
            self.matching_technologies[max(self.matching_technologies)]))
        print("")


if __name__ == "__main__":
    variable = JsonParser()
    variable.parse_question_file()
    variable.parse_answer_file()
    variable.print_matching_tech()
