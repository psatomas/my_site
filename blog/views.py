from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Tomas",
        "date": date(2024, 7, 15),
        "title": "Hike in the Mountains",
        "excerpt": "A wonderful hike in the mountains.",
        "content": "Full content of the hike in the mountains post."
    },
    {
        "slug": "beach-adventure",
        "image": "beach.jpg",
        "author": "Tomas",
        "date": date(2023, 7, 15),
        "title": "Beach Adventure",
        "excerpt": "An exciting adventure at the beach.",
        "content": "Full content of the beach adventure post."
    },
    {
        "slug": "city-exploration",
        "image": "city.jpg",
        "author": "Tomas",
        "date": date(2022, 7, 15),
        "title": "City Exploration",
        "excerpt": "Exploring the vibrant city life.",
        "content": "Full content of the city exploration post."
    }
]

def get_date(post):
    return post.get('date')

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html",{
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
