from generic_app.models import *


class TutorGroup(Model):
    id = AutoField(primary_key=True)
    group_name = TextField()

    def __str__(self):
        return f"{self.group_name}"
