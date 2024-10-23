from django.contrib import admin
from .models import Category, Movie, Payment, Profile, Review, Subscription, User, WatchList

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Category_Id', 'category_name', 'description')
    search_fields = ('category_name',)
    ordering = ('category_name',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('Movie_Id', 'Title', 'Release_Year', 'Duration', 'Rating', 'category')
    search_fields = ('Title', 'Description')
    list_filter = ('Release_Year', 'category')
    ordering = ('-Release_Year',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('Payment_Id', 'User_Id', 'Amount', 'Date')
    search_fields = ('User_Id__Username', 'Card_Number')
    list_filter = ('Date',)
    ordering = ('-Date',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('Profile_Id', 'User_Id', 'Profile_Name')
    search_fields = ('Profile_Name', 'User_Id__Username')
    ordering = ('User_Id',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('Review_Id', 'Movie_Id', 'User_Id', 'Rating', 'Review_Date')
    search_fields = ('Movie_Id__Title', 'User_Id__Username', 'Comment')
    list_filter = ('Rating', 'Review_Date')
    ordering = ('-Review_Date',)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('Channel_Id', 'User_Id', 'Subscription_Type', 'Price', 'Duration')
    search_fields = ('User_Id__Username', 'Subscription_Type')
    ordering = ('User_Id',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('User_Id', 'Username', 'Email', 'DOB', 'Reg_Date')
    search_fields = ('Username', 'Email')
    ordering = ('Username',)

class WatchListAdmin(admin.ModelAdmin):
    list_display = ('Watch_list_Id', 'Profile_Id', 'Movie_Id', 'added_date')
    search_fields = ('Profile_Id__Profile_Name', 'Movie_Id__Title')
    ordering = ('-added_date',)

# Register your models here
admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(WatchList, WatchListAdmin)
