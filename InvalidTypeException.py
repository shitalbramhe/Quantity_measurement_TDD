import enum


class ExceptionType(enum.Enum):
    NONE_VALUE_EXCEPTION = "Given value is not None. It must None"
    TYPE_CHECK_EXCEPTION = "Given value is not int type, enter integer value"
    REFERENCE_CHECK_EXCEPTION = "Reference of given value is not same, must enter proper value"
    VALUE_EXCEPTION = "Given value is not proper"
    NOT_FEET_EXCEPTION = "Given unit is not a feet"
    NOT_INCH_EXCEPTION = "Given unit is not a Inch"
    NOT_YARD_EXCEPTION = "Given unit is not a yard"
    


class InvalidTypeException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"{self.message}"