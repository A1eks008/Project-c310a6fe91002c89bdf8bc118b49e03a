from random import randint
from abc import ABC

import pygame

#Тип класса урона наносимого физическому здоровью


class Damage(ABC):
    type_damage = str
    value_damage = int


class PhisicDamage(Damage):
    type_damage = 'red'


class BladeDamage(PhisicDamage):
    pass


class PrickingDamage(PhisicDamage):
    pass

class BrisantSDamage(PhisicDamage):
    pass

class MentalDamage(Damage):
    type_damage = 'white'

    


