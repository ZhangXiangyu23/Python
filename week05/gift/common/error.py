# coding:utf-8

"""
    自定义异常类
"""


class NotPathError(Exception):
    def __init__(self, message):
        self.message = message


class FormatError(Exception):
    def __init__(self, message):
        self.message = message


class NotFilePath(Exception):
    def __init__(self, message):
        self.message = message


class UserExistsError(Exception):
    def __init__(self, message):
        self.message = message


class RoleError(Exception):
    def __init__(self, message):
        self.message = message


class LevelError(Exception):
    def __init__(self, message):
        self.message = message


class NegativeNumberError(Exception):
    def __init__(self, message):
        self.message = message


class NotExistError(Exception):
    def __init__(self, message):
        self.message = message


class NotUserError(Exception):
    def __init__(self, message):
        self.message = message


class UserActiveError(Exception):
    def __init__(self, message):
        self.message = message


class CountError(Exception):
    def __init__(self, message):
        self.message = message