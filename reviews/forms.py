from django import forms
class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100,required=True,
                                error_messages={'required':'Please enter your name'})

    review_text = forms.CharField(label="Your Review", max_length=100,widget=forms.Textarea,required=True,)
    rating = forms.IntegerField(label="Your Rating",min_value=1,max_value=5)