from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from libreqda.models import Annotation, Code, Document, Project
from libreqda.validators import DocumentValidator


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('owner', 'version', 'creation_date', 'modified_date')


class AddUserToProjectForm(forms.Form):
    users = forms.ModelMultipleChoiceField(
                        queryset=User.objects.all(),
                        label=_('Usuarios'))


class NewDocumentForm(forms.Form):
    document = forms.ModelChoiceField(
                        queryset=Document.objects.all(),
                        label="Documento")
    name = forms.CharField(max_length=250, label='Nombre')
    comment = forms.CharField(required=False,
                              widget=forms.Textarea,
                              label='Comentario')


class UploadDocumentForm(forms.Form):
    document = forms.FileField(label="Documento",
                               validators=[DocumentValidator()])
    name = forms.CharField(max_length=250, label='Nombre')
    comment = forms.CharField(required=False,
                              widget=forms.Textarea,
                              label='Comentario')


class CodeForm(forms.ModelForm):
    class Meta:
        WEIGHTS = [(i, i) for i in range(-100, 101)][::-1]

        model = Code
        exclude = ('created_by', 'creation_date', 'modified_date', 'project',
                   'citations', 'parent_code')
        widgets = {'name': forms.TextInput(),
                   'weight': forms.Select(choices=WEIGHTS)}


class AnnotationForm(forms.ModelForm):
    class Meta:
        model = Annotation
        exclude = ('created_by', 'creation_date', 'modified_date', 'project')


class AddCodeToAnnotation(forms.Form):
    codes = forms.ModelMultipleChoiceField(label=_('Códigos'))
