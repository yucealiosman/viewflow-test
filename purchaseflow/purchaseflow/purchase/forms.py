from material.forms import ModelForm, InlineFormSetField

from .models import Leave


class LeaveForm(ModelForm):
    # items = InlineFormSetField(
    #     Leave,
    #     fields=['name', 'quantity'], can_delete=False)

    class Meta:
        model = Leave
        fields = [
            'shipment_no', 'first_name', 'last_name',
            'email', 'phone', 'address', 'zipcode',
            'city', 'state', 'country'
        ]
