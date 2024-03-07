from django.shortcuts import render
from django.http import HttpResponse
from .models import Feed

def show_feed(request):
    return HttpResponse("show feed")

def all_feed(request):
    feeds = Feed.objects.all()
    # return HttpResponse("all feed")
	# return render(request, "feeds.html")
    return render(request, "feeds.html", {"feeds":feeds, "content":"내용"})

def one_feed(request, feed_id, feed_content):
    return HttpResponse(f"feed id: {feed_id}, feed content: {feed_content}")