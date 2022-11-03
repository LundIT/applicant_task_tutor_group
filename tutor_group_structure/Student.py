from generic_app.models import *
from generic_app.submodels.new_applicant_task_tutor_group.tutor_group_structure.TutorGroup import TutorGroup


class Student(Model):
    id = AutoField(primary_key=True)
    name = TextField()
    matriculation_number = TextField()
    tutor_group = ForeignKey(to=TutorGroup, on_delete=CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"
