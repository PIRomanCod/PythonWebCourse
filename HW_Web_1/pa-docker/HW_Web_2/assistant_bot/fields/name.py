from fields.field import Field


class Name(Field):

    @Field.value.setter
    def value(self, value: str):
        if value.isdigit():
            raise ValueError("Name cannot be a numbers")
        self._value = value
