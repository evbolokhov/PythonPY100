if __name__ == "__main__":
    list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
    unique_numbers = set(list_)

    sum_ = sum(unique_numbers)
    len_ = len(unique_numbers)

    print(sum_)
    print(len_)
    print(sum_ / len_)
    # TODO найти суммуб количество и среднее уникальных чисел
