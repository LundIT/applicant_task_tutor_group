import pandas as pd

from ProcessAdminRestApi.models.upload_model import ConditionalUpdateMixin
from generic_app import models
from generic_app.models import *


class StudentReport(UploadModelMixin, ConditionalUpdateMixin):
    id = AutoField(primary_key=True)
    student_report = XLSXField(null=True, blank=True)

    internal_update = False

    def __str__(self):
        return f"Student Report for {self.id}"

    @ConditionalUpdateMixin.conditional_calculation
    def update(self):
        if not self.internal_update:
            self.internal_update = True
            print(f"Create Student Report")





