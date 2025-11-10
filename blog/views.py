from django.shortcuts import render
from datetime import date

posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Tomas",
        "date": date(2024-01-15),
        "title": "Hike in the Mountains",
        "excerpt": "A wonderful hike in the mountains.",
        "content": "Full content of the hike in the mountains post."
    },
    {
        "slug": "beach-adventure",
        "image": "beach.jpg",
        "author": "Tomas",
        "date": "2024-02-20",
        "title": "Beach Adventure",
        "excerpt": "An exciting adventure at the beach.",
        "content": "Full content of the beach adventure post."
    },
    {
        "slug": "city-exploration",
        "image": "city.jpg",
        "author": "Tomas",
        "date": "2024-03-10",
        "title": "City Exploration",
        "excerpt": "Exploring the vibrant city life.",
        "content": "Full content of the city exploration post."
    }
]
# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
