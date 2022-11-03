import pandas as pd

from generic_app.models import *


class GroupStructureUpload(UploadModelMixin, Model):
    id = AutoField(primary_key=True)
    student_file = FileField()
    tutor_file = FileField()
    group_file = FileField()

    def update(self):
        try:
            groups = pd.read_excel(self.group_file.file)
        except AttributeError:
            pass
        try:
            tutors = pd.read_excel(self.tutor_file.file)
        except AttributeError:
            pass
        try:
            students = pd.read_excel(self.student_file.file)
        except AttributeError:
            pass
