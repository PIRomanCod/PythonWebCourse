from fields.field import Field
from exc import EmailVerificationError
import re


class Email(Field):

    @Field.value.setter
    def value(self, email: str):
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            self._value = email
        else:
            raise EmailVerificationError("Email is not valid")
