from django.db import models

class Category(models.Model):
    # Define Category_Id as a primary key with integer type
    Category_Id = models.AutoField(primary_key=True)  # Automatically increments
    category_name = models.CharField(max_length=255)  # Renamed from `name` to `category_name`
    description = models.TextField(blank=True)  # Added description field, can be blank

    def __str__(self):
        return self.category_name

class Movie(models.Model):
    # Define Movie_Id as a primary key with integer type
    Movie_Id = models.AutoField(primary_key=True)  # Automatically increments
    Title = models.CharField(max_length=255)  # Title of the movie
    Description = models.TextField(blank=True)  # Description of the movie
    Release_Year = models.IntegerField() # Date of release
    Duration = models.PositiveIntegerField()  # Duration in minutes (or whatever unit you prefer)
    Channel_Id = models.IntegerField()  # Channel ID as an integer
    Rating = models.DecimalField(max_digits=3, decimal_places=1)  # Movie rating

    # Foreign key to Category model
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

from django.db import models

class Payment(models.Model):
    Payment_Id = models.AutoField(primary_key=True)  # Custom primary key for the payment
    User_Id = models.ForeignKey('User', on_delete=models.CASCADE)  # Foreign key to User model
    Amount = models.DecimalField(max_digits=10, decimal_places=2)  # Payment amount
    Card_Number = models.CharField(max_length=16)  # Card number as a string
    Expiration_Date = models.DateField()  # Expiration date of the card
    Date = models.DateTimeField(auto_now_add=True)  # Date of payment

    def __str__(self):
        return f"Payment of {self.Amount} by {self.User_Id}"


class Profile(models.Model):
    Profile_Id = models.AutoField(primary_key=True)  # Custom primary key for the profile
    User_Id = models.ForeignKey('User', on_delete=models.CASCADE)  # Foreign key to User model
    Profile_Name = models.CharField(max_length=255, blank=True, null=True)  # Profile name

    def __str__(self):
        return self.Profile_Name if self.Profile_Name else self.User_Id.username

class Review(models.Model):
    Review_Id = models.AutoField(primary_key=True)  # Custom primary key for the review
    Movie_Id = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Foreign key to Movie model
    User_Id = models.ForeignKey('User', on_delete=models.CASCADE)  # Foreign key to User model
    Comment = models.TextField()  # Review comment
    Rating = models.IntegerField()  # Rating, consider adding validation (e.g., choices)
    Review_Date = models.DateTimeField(auto_now_add=True)  # Date of review

    def __str__(self):
        return f"{self.User_Id.username} - {self.Movie_Id.title}" 
    
    
class Subscription(models.Model):
    Subscription_id = models.AutoField(primary_key=True)
    Channel_Id = models.ForeignKey('Channel', on_delete=models.CASCADE)  # Channel ID as an integer
    User_Id = models.ForeignKey('User', on_delete=models.CASCADE)  # Foreign key to User model
    Subscription_Type = models.CharField(max_length=255)  # Type of subscription
    Price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the subscription
    Duration = models.PositiveIntegerField()  # Duration in days (or any other unit you prefer)

    def __str__(self):
        return f"{self.User_Id.username} - {self.Subscription_Type}"

class Channel(models.Model):
    Channel_Id = models.AutoField(primary_key=True)    # Channel ID as an integer
    Channel_name = models.CharField(max_length=255)  # Type of subscription
    

class User(models.Model):
    User_Id = models.AutoField(primary_key=True)  # Custom primary key for the user
    Username = models.CharField(max_length=255, unique=True)  # Username field
    Email = models.EmailField(unique=True)  # Email field
    Password = models.CharField(max_length=255)  # Password field
    DOB = models.DateField(null=True, blank=True)  # Date of birth
    Reg_Date = models.DateTimeField(auto_now_add=True)  # Registration date

    def __str__(self):
        return self.Username

from django.db import models

class WatchList(models.Model):
    Watch_list_Id = models.AutoField(primary_key=True)  # Custom primary key for the watchlist entry
    Profile_Id = models.ForeignKey('Profile', on_delete=models.CASCADE)  # Foreign key to Profile model
    Movie_Id = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Foreign key to Movie model
    added_date = models.DateTimeField(auto_now_add=True)  # Date the movie was added to the watchlist

    def __str__(self):
        return f"{self.Profile_Id.Profile_Name} - {self.Movie_Id.title}"