# coding=utf-8
from survey import AnonymousSurvey
# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "你第一门的学习语言是什么?--如需退出请按q"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
while True:
    response = raw_input("语言:")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("\n谢谢参与调查!")
my_survey.show_results()