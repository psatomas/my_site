from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "weekend-in-the-fields",
        "image": "field.jpg",
        "author": "Tomas",
        "date": date(2024, 7, 15),
        "title": "Weekend in the Fields",
        "excerpt": "A wonderful weekend spent in the countryside, where I reconnected with nature with my family.",
        "content": "Full content of the field post."
    },
    {
        "slug": "boat-ride",
        "image": "boat.jpg",
        "author": "Tomas",
        "date": date(2023, 7, 15),
        "title": "Boat Ride",
        "excerpt": "An exciting adventure at the beach where I enjoyed a boat ride with which I explored the sea.",
        "content": "Full content of the boat adventure post."
    },
    {
        "slug": "tour-in-jungle",
        "image": "jungle.jpg",
        "author": "Tomas",
        "date": date(2022, 7, 15),
        "title": "Tour in Jungle",
        "excerpt": "Exploring the vibrant flora and fauna of the jungle, beatutiful experience!",
        "content": "Full content of the jungle exploration post."
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
