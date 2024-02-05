from django import forms

from core.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'name',
            'completed',
        )


TaskFormSet = forms.modelformset_factory(
    Task,
    form=TaskForm,
    extra=1,
    can_delete=True
)