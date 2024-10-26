from fields.field import Field
from exc import PhoneVerificationError


class Phone(Field):
    @Field.value.setter
    def value(self, phone: str):
        if phone.isdigit() and len(phone) == 10:
            self._value = phone
        else:
            raise PhoneVerificationError
