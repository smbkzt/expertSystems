#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Json parser'''
import io
import json
import time


class JsonParser:
    '''Main class of JSON Parser'''
    def __init__(self):
        '''Initializing variables'''
        self.__parsed_string = ''
        self.__user_answers = []
        self.matching_technologies = {}

    def open_file(self, path):
        '''Initialize a parsed string data'''
        string_to_parse = ''
        with io.open(path, encoding='utf-8') as json_file:
            for line in json_file:
                string_to_parse += line
        self.__parsed_string = json.loads(string_to_parse)

    def parse_question_file(self, path='JSON files/questions.json'):
        '''Parsing a question file to ask user'''
        self.open_file(path=path)

        for element in self.__parsed_string:
            print("____________________________")
            print(element['QuestionValue'])

            for sub_element in element['Answers']:
                print("{0}: {1}".format(
                    sub_element['AnswerId'],
                    sub_element['AnswerValue']))

            user_answer = input("Ответ: ")

            self.__user_answers.extend(
                answer['AnswerValue'] for answer in element['Answers']
                if str(answer['AnswerId']) == user_answer)
            # for yx in x['Answers']:
            #     if str(yx['AnswerId']) == str(answer):
            #         self.__user_answers.append(yx['AnswerValue'])

        print('------------------------------')
        print("Ваши ответы: ")
        for answer in self.__user_answers:
            print(answer)
        print('------------------------------')

    def parse_answer_file(self, path='JSON files/answer.json'):
        '''
            Parsing an answer file to compare user's answers with rating system
        '''
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
        '''This method prints found technology'''
        print("")
        print("Подбираю Наиболее подходящие технологии...")
        print("")
        time.sleep(1.5)
        print("------------------------------------")
        print("Все подходящие варианты: ")
        print("")
        time.sleep(0.5)
        for number in self.matching_technologies:
            print("Технология - {0}, коэфициент совпадения - {1}".format(
                self.matching_technologies[number], number))
            time.sleep(.5)

        print("")
        print("------------------------------------")
        print("Оптимально подходящая технология для вас это: {0}".format(
            self.matching_technologies[max(self.matching_technologies)]))
        print("")


if __name__ == "__main__":
    JsonParser = JsonParser()
    JsonParser.parse_question_file()
    JsonParser.parse_answer_file()
    JsonParser.print_matching_tech()
