from django.forms import ModelForm
from sms.models import Cliente_sms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Fieldset
from crispy_forms.bootstrap import FormActions


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente_sms
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ClienteForm'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        
        
        self.helper.add_input(Submit('thanks', 'submit'))
