import io
import json
import time


class JsonParser:
    __parsed_string = ''
    __user_answers = []
    matching_technologies = {}

    def open_file(self, path):
        string_to_parse = ''
        with io.open(path, encoding='utf-8') as file:
            for line in file:
                string_to_parse += line
        self.__parsed_string = json.loads(string_to_parse)

    def parse_question_file(self, path='JSON files/questions.json'):
        self.open_file(path=path)
        for x in self.__parsed_string:
            print(x['QuestionValue'])
            for y in x['Answers']:
                print(str(y['AnswerId']) + ": " + str(y['AnswerValue']))

            answer = int(input())
            for yx in x['Answers']:
                if str(yx['AnswerId']) == str(answer):
                    self.__user_answers.append(yx['AnswerValue'])

        print("Ваши ответы: ")
        for x in self.__user_answers:
            print(x)

    def parse_answer_file(self, path='JSON files/answer.json'):
        self.open_file(path)

        for x in self.__parsed_string:
            matches = 0
            for y in x['tags']:
                for ans in self.__user_answers:
                    if ans == y:
                        matches += 1
                    else:
                        continue
                    if ans == y == "Веб-приложение":
                        matches += 10

            if matches > 0:
                technology = x['technology']
                self.matching_technologies[matches] = technology

    def print_matching_tech(self):
        print()
        print("Подбираю Наиболее подходящие технологии...")
        time.sleep(1)
        print("...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")
        time.sleep(1.5)
        print("------------------------------------")
        print("Все подходящие варианты: ")
        print()
        time.sleep(0.5)
        for ttotal in self.matching_technologies:
            print("Технология - {0}, коэфициент совпадения - {1}".format(self.matching_technologies[ttotal], ttotal))
            print()
            time.sleep(1)

        print("------------------------------------")
        print("Оптимально подходящая технология для вас это: " + self.matching_technologies[max(self.matching_technologies)])


if __name__ == "__main__":
    variable = JsonParser()
    print("Введите путь к файлу или оставтье это поле пустым: ")
    _path = input()
    variable.parse_question_file()
    variable.parse_answer_file()
    variable.print_matching_tech()
