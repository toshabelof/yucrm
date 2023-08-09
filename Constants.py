from pip._internal.utils.misc import enum


class Compare(enum):
    EQUALS = '='
    IN = 'in'
    MIN = 'min'
    MAX = 'max'
    NOT = 'not'
    LIKE = 'like'
