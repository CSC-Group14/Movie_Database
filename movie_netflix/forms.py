from django import forms
from .models import Category, Movie, Payment, Profile, Review, Subscription, User, WatchList

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['Title', 'Description', 'Release_Year', 'Duration', 'Channel_Id', 'Rating', 'category']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['User_Id', 'Amount', 'Card_Number', 'Expiration_Date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['User_Id', 'Profile_Name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['Movie_Id', 'User_Id', 'Comment', 'Rating']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['Channel_Id', 'User_Id', 'Subscription_Type', 'Price', 'Duration']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Username', 'Email', 'Password', 'DOB']

class WatchListForm(forms.ModelForm):
    class Meta:
        model = WatchList
        fields = ['Profile_Id', 'Movie_Id']
