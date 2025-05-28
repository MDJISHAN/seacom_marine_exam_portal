from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms 
 
class Question_DB(models.Model):
    professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE, null=True)
    qno = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    question_image = models.ImageField(upload_to='faculty_profile_pics', null=True, blank=True)
    optionA = models.CharField(max_length=100, null=True, blank=True)
    optionA_image = models.ImageField(upload_to='faculty_profile_pics', null=True, blank=True)
    optionB = models.CharField(max_length=100, null=True, blank=True)
    optionB_image = models.ImageField(upload_to='faculty_profile_pics', null=True, blank=True)
    optionC = models.CharField(max_length=100, null=True, blank=True)
    optionC_image = models.ImageField(upload_to='faculty_profile_pics', null=True, blank=True)
    optionD = models.CharField(max_length=100, null=True, blank=True)
    optionD_image = models.ImageField(upload_to='faculty_profile_pics', null=True, blank=True)
    answer = models.CharField(max_length=200, null=True, blank=True)
    max_marks = models.IntegerField(default=0)

     # New fields for image uploads for each option

    def __str__(self):
        return f'Question No.{self.qno}: {self.question} \t\t Options: \nA. {self.optionA} \nB.{self.optionB} \nC.{self.optionC} \nD.{self.optionD}'

    #def __str__(self):
        #return f'Question No.{self.qno}: {self.question} \t\t Options: \nA. {self.optionA_image} \nB.{self.optionB_image} \nC.{self.optionC_image} \nD.{self.optionD_image} '


class QForm(ModelForm):
    class Meta:
        model = Question_DB
        fields = '__all__'
        exclude = ['qno', 'professor']
        widgets = {
            'question': forms.TextInput(attrs = {'class':'form-control'}),
            'optionA': forms.TextInput(attrs = {'class':'form-control'}),
            'optionB': forms.TextInput(attrs = {'class':'form-control'}),
            'optionC': forms.TextInput(attrs = {'class':'form-control'}),
            'optionD': forms.TextInput(attrs = {'class':'form-control'}),
            'answer': forms.TextInput(attrs = {'class':'form-control'}),
            'max_marks': forms.NumberInput(attrs = {'class':'form-control'}),
        }

         # Additional fields for image uploads
    question_image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    optionA_image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    optionB_image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    optionC_image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    optionD_image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))