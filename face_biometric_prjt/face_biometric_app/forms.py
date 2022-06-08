from django import forms

from face_biometric_app.models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'id': forms.NumberInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            # 'photo': forms.ImageField(attrs={'class': 'form-control-file'}),
        }