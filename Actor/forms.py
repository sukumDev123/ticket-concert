
from django.forms import ModelForm
from .models import ActorModel


class ActorForm(ModelForm):
    class Meta:
        model = ActorModel
        fields = ['name_actor', 'detail_actor', 'age_actor']
