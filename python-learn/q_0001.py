# coding=utf-8
"""
使用 Python 如何生成 200 个激活码（或者优惠券）
"""

import random


def generate(count,length):
    source = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    gifts = []
    while len(gifts) < count:
        gift = ''
        while len(gift) < length:
            gift += random.choice(source)
        if gift not in gifts:
            gifts.append(gift)
    return gifts




