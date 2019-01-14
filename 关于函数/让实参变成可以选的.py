# -*- coding: utf-8 -*-
def get_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + middle_name + last_name
    else:
        full_name = first_name + last_name
    return full_name
nameA = get_name('姓','名','中间')
nameB = get_name('李','小龙')

print nameA
print nameB