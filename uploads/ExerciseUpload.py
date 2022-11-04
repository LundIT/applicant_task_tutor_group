import pandas as pd

from generic_app.models import *


class ExerciseUpload(UploadModelMixin, Model):
    id = AutoField(primary_key=True)


    def update(self):
        try:
            print("Upload Exercise Files")
        except AttributeError:
            pass
