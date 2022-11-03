from generic_app.models import *

from generic_app.submodels.new_applicant_task_tutor_group.tutor_group_structure.Student import Student


class Points(Model):
    id = AutoField(primary_key=True)

    def __str__(self):
        return f""