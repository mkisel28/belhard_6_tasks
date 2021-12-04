school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}
name_of_class = school_data.keys()


def incr_students(school_data, name_of_class):
    school_data[name_of_class] = school_data[name_of_class] + 1
    return school_data


def decr_students(school_data, name_of_class):
    if school_data[name_of_class] > 0:
        school_data[name_of_class] = school_data[name_of_class] - 1
        return school_data
    else:
        raise ValueError("закончились")


def add_class(school_data, name_of_class):
    school_data[name_of_class] = 0
    return school_data


def remove_class(school_data, name_of_class):
    school_data.pop(name_of_class)
    return school_data


def calc_students(school_data):
    return sum(school_data.values())


print(incr_students(school_data, name_of_class='1b'))
print(decr_students(school_data, name_of_class='2b'))
print(add_class(school_data, name_of_class='5a'))
print(add_class(school_data, name_of_class='5a'))
print(calc_students(school_data))
