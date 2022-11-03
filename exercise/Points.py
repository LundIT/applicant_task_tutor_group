from generic_app.models import *

from generic_app.submodels.new_applicant_task_tutor_group.tutor_group_structure.Student import Student


class Points(Model):
    id = AutoField(primary_key=True)
    exercise = TextField()
    student = ForeignKey(to=Student, on_delete=CASCADE)
    points = FloatField()
    max_points = FloatField()

    def __str__(self):
        return f"Student {self.student} with Exercise: {self.exercise}"