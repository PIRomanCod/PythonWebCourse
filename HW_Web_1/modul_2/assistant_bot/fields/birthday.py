from fields.field import Field
from datetime import datetime, date, timedelta


class Birthday(Field):

    @Field.value.setter
    def value(self, birthday: str) -> date:
        current_date = datetime.now().date()
        birthday_date = datetime.strptime(birthday, '%d/%m/%Y').date()
        if birthday_date > current_date:
            raise ValueError("You entered date that earlier current date")
        self._value = birthday
