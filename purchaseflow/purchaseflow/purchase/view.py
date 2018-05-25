from django.views import generic
from material import Layout, Fieldset, Row, Span2, Span5, Span7

from viewflow.flow.views import StartFlowMixin, FlowMixin


from .forms import LeaveForm


class StartView(StartFlowMixin, generic.UpdateView):
    form_class = LeaveForm

    layout = Layout(
        Row('shipment_no'),
        Fieldset('Customer Details',
                 Row('first_name', 'last_name', 'email'),
                 Row('phone')),
        Fieldset('Address',
                 Row(Span7('address'), Span5('zipcode')),
                 Row(Span5('city'), Span2('state'), Span5('country'))),
        'items',
    )

    def get_object(self):
        return self.activation.process.shipment

    def activation_done(self, form):
        shipment = form.save()
        self.activation.process.shipment = shipment
        super(StartView, self).activation_done(form)
