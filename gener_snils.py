# -*- coding: utf-8 -*-

__author__ = 'cpn'


from random import randint


def check_snils(snils):
    """
    Функция проверки СНИЛС
    :param snils: СНИЛС
        (пример '127-818-558 91')
    :type: str

    :return: результат проверки
    :rtype: bool
    """
    if len(snils) != 14:
        return False

    # случаай когда снидс вида '000-000-000 00'
    zero_snils = '00000000000'
    if snils.replace('-', '').replace(' ', '') == zero_snils:
        return False

    def snils_csum(snils):
        k = range(9, 0, -1)
        pairs = zip(
            k, [
                int(x) for x in snils.replace('-', '').replace(' ', '')[:-2]
            ]
        )
        return sum([k * v for k, v in pairs])

    csum = snils_csum(snils)

    while csum > 101:
        csum %= 101
    if csum in (100, 101):
        csum = 0

    return csum == int(snils[-2:])


def main(count=50):
    result = []
    r = 0
    while True:
        val = randint(10000000000, 99999999999)
        val_str = '-'.join((str(val)[0:3],str(val)[3:6], str(val)[6:9]))+' ' + str(val)[9:11]
        if check_snils(val_str):

            print val_str
            result.append(val_str)

        if len(set(result)) > count:
            break

    return set(result)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c',
        '--count',
        type=int,
        help='Колличество случайных снилсов'
    )
    args = parser.parse_args()
    count = args.count
    main(int(count))
