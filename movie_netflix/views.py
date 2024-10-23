from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Movie, Payment, Profile, Review, Subscription, User, WatchList
from .forms import (CategoryForm, MovieForm, PaymentForm, ProfileForm,
                    ReviewForm, SubscriptionForm, UserForm, WatchListForm)

# Category Views
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})

# Repeat similar views for Movie, Payment, Profile, Review, Subscription, User, and WatchList
# Here’s an example for the Movie views:

# Movie Views
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payment': payments})

def watch_list(request):
    watch = WatchList.objects.all()
    return render(request, 'watch_list.html', {'watch': watch})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'review': reviews})

def profile_list(request):
    profile = Profile.objects.all()
    return render(request, 'profile_list.html', {'profile': profile})

def user_list(request):
    user = User.objects.all()
    return render(request, 'user_list.html', {'user': user})

def subscription_list(request):
    subscription =Subscription.objects.all()
    return render(request, 'subscription_list.html', {'payment': subscription})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {'form': form})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_form.html', {'form': form})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movie_confirm_delete.html', {'movie': movie})

# Continue with similar CRUD functions for Payment, Profile, Review, Subscription, User, WatchList
