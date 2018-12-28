from oscar.apps.basket import forms as base_forms


class BasketLineForm(base_forms.BasketLineForm):

    class Meta(base_forms.BasketLineForm.Meta):
        fields = ['quantity', 'title', 'price', 'comments']
