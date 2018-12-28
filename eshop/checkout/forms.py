from oscar.apps.checkout import forms as base_forms


class ShippingAddressForm(base_forms.ShippingAddressForm):

    class Meta(base_forms.ShippingAddressForm.Meta):
        fields = [
            'title', 'first_name', 'last_name',
            'line1', 'line2', 'line3', 'line4',
            'state', 'postcode', 'country',
            'phone_number', 'notes', 'event', 'event_date', 'marketing_source']
