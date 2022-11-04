from generic_app.models import *


class Student(Model):
    id = AutoField(primary_key=True)
    name = TextField()
    matriculation_number = TextField()
    tutor_group = TextField()

    def __str__(self):
        return f"{self.name}"
