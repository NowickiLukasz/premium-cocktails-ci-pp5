from django import forms

from .models import Product, ProductReview


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class ProductReviewForm(forms.ModelForm):
    '''
    Creates the review for the selling product.
    '''
    class Meta:

        model = ProductReview
        fields = ('title', 'user_review', )
