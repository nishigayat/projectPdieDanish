from django import forms
from .models import Register_Case, Disciplinary_Case

class RegisterCaseUpdateForm(forms.ModelForm):
    class Meta:
        model = Register_Case
        fields = ['caseCode', 'caseClass', 'offences', 'punishment', 'registerText']

    def __init__(self, *args, **kwargs):
        super(RegisterCaseUpdateForm, self).__init__(*args, **kwargs)
        # Set the 'readonly' attribute for the 'caseCode' field
        self.fields['caseCode'].widget.attrs['readonly'] = True

class DisciplinaryCaseForm(forms.ModelForm):
    class Meta:
        model = Disciplinary_Case
        fields = ['studentName', 'studentID', 'studentClass', 'caseCode', 'disciplinaryText', 'disciplinaryDate']

    labels = {
        'studentName': 'Student Name',
        'studentID': 'Student ID',
        'studentClass': 'Student Class',
        'caseCode': 'Case Code',
        'disciplinaryText': 'Disciplinary Text',
        'disciplinaryDate': 'Disciplinary Date',
    }
