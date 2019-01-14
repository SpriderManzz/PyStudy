# coding=utf-8
def get_formatted_name(first_name, last_name, middle_name=''):
    """一个使用户得到一个完整的姓名的程序
    版本1是只能输出姓和名
    版本2是能输入中间姓"""
    if middle_name:
        full_name = first_name + middle_name + last_name
    else:
        full_name = first_name + last_name

    return full_name.title()

# a = get_formatted_name('tom','cat')    # 为什么写了这些就会在执行names会输出Tomcat
# print amiddle_name=''
