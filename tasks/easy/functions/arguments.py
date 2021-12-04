def dict_from_args(*args, **kwargs):
    if all(isinstance(key, int) for key in args):
        summa = {"args_sum": sum(args)}
    else:
        raise TypeError("Все позиционные аргументы должны быть целыми")
    if all(isinstance(values, str) for values in kwargs):
        maxima_len = {
            "kwargs_max_len":
            max(len(values) for values in kwargs.values())
            }
    else:
        raise TypeError("Все аргументы - ключевые слова должны быть строками")
    summa.update(maxima_len)
    return summa


print(dict_from_args(*(41, 50, 13), **{"1": "aaggh", "2": "bhgjhhg"}))
