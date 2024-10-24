from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Movie, Payment, Profile, Review, Subscription, User, WatchList
from .forms import (CategoryForm, MovieForm, PaymentForm, ProfileForm,
                    ReviewForm, SubscriptionForm, UserForm, WatchListForm)

# Category Views
# views.py
from django.shortcuts import render
from django.db import connection

def category_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM movie_netflix.movie_netflix_category;")
        rows = cursor.fetchall()

        # Optional: You can map the rows to a dictionary for better access in the template
        columns = [col[0] for col in cursor.description]  # Get column names
        categories = [dict(zip(columns, row)) for row in rows]  # Zip column names with row values

    return render(request, 'categories.html', {'categories': categories})


def movie_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM movie_netflix.movie_netflix_movie;")
        rows = cursor.fetchall()

        # Get column names to use in the template
        columns = [col[0] for col in cursor.description]

        # Map rows to dictionaries with column names as keys
        movies = [dict(zip(columns, row)) for row in rows]

    return render(request, 'movies.html', {'movies': movies})


def payment_list(request):
    with connection.cursor() as cursor:
        # Execute raw SQL query
        cursor.execute("SELECT * FROM movie_netflix.movie_netflix_payment;")
        rows = cursor.fetchall()

        # Get column names to use in the template
        columns = [col[0] for col in cursor.description]

        # Convert rows into dictionaries for better access in the template
        payments = [dict(zip(columns, row)) for row in rows]

    # Pass the result to the template
    return render(request, 'payments.html', {'payments': payments})

def user_list(request):
    with connection.cursor() as cursor:
        # Execute raw SQL query
        cursor.execute("SELECT * FROM movie_netflix.movie_netflix_user;")
        rows = cursor.fetchall()

        # Get column names to use in the template
        columns = [col[0] for col in cursor.description]

        # Convert rows into dictionaries for better access in the template
        users = [dict(zip(columns, row)) for row in rows]

    # Pass the result to the template
    return render(request, 'users.html', {'users': users})

def subscription_list(request):
    with connection.cursor() as cursor:
        # Execute raw SQL query
        cursor.execute("SELECT * FROM movie_netflix.movie_netflix_subscription;")
        rows = cursor.fetchall()

        # Get column names to use in the template
        columns = [col[0] for col in cursor.description]

        # Convert rows into dictionaries for better access in the template
        subscriptions = [dict(zip(columns, row)) for row in rows]

    # Pass the result to the template
    return render(request, 'subscriptions.html', {'subscriptions': subscriptions})

def profile_list(request):
    with connection.cursor() as cursor:
        # Execute raw SQL query
        cursor.execute("SELECT * FROM movie_netflix.movie_netflix_profile;")
        rows = cursor.fetchall()

        # Get column names to use in the template
        columns = [col[0] for col in cursor.description]

        # Convert rows into dictionaries for better access in the template
        profiles = [dict(zip(columns, row)) for row in rows]

    # Pass the result to the template
    return render(request, 'profiles.html', {'profiles': profiles})

def review_list(request):
    with connection.cursor() as cursor:
        # Execute raw SQL query
        cursor.execute("SELECT * FROM movie_netflix.movie_netflix_review;")
        rows = cursor.fetchall()

        # Get column names to use in the template
        columns = [col[0] for col in cursor.description]

        # Convert rows into dictionaries for better access in the template
        reviews = [dict(zip(columns, row)) for row in rows]

    # Pass the result to the template
    return render(request, 'reviews.html', {'reviews': reviews})

def channel_list(request):
    with connection.cursor() as cursor:
        # Execute raw SQL query
        cursor.execute("SELECT * FROM movie_netflix.movie_netflix_channel;")
        rows = cursor.fetchall()

        # Get column names to use in the template
        columns = [col[0] for col in cursor.description]

        # Convert rows into dictionaries for better access in the template
        channels = [dict(zip(columns, row)) for row in rows]

    # Pass the result to the template
    return render(request, 'channels.html', {'channels': channels})



def query(request):
    with connection.cursor() as cursor:
        # Execute the combined SQL query
        cursor.execute("""
            SELECT 
                u.username AS user_name,
                m.title AS movie_title,
                c.category_name AS category,
                ch.channel_name AS channel,
                s.subscription_type AS subscription,
                s.expiration_date AS subscription_expiration
            FROM 
                movie_netflix_user AS u
            JOIN 
                movie_netflix_profile AS p ON u.id = p.user_id
            JOIN 
                movie_netflix_subscription AS s ON p.id = s.profile_id
            JOIN 
                movie_netflix_payment AS pay ON u.id = pay.user_id
            JOIN 
                movie_netflix_movie AS m ON pay.movie_id = m.id
            JOIN 
                movie_netflix_category AS c ON m.category_id = c.id
            JOIN 
                movie_netflix_channel AS ch ON m.channel_id = ch.id
            WHERE 
                s.expiration_date > NOW()
            ORDER BY 
                u.username, m.title;
        """)
        
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in rows]

    return render(request, 'query.html', {'results': results})

