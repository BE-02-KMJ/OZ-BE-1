from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Feed
from .serializers import FeedSerializer

# def show_feed(request):
#     return HttpResponse("show feed")

# def all_feed(request):
#     feeds = Feed.objects.all()
#     # return HttpResponse("all feed")
# 	# return render(request, "feeds.html")
#     return render(request, "feeds.html", {"feeds":feeds, "content":"내용"})

# def one_feed(request, feed_id, feed_content):
#     return HttpResponse(f"feed id: {feed_id}, feed content: {feed_content}")

# (1) 전체 데이터를 다 보여주는 Serialize
class Feeds(APIView):
    def get(self, request):
        feeds = Feed.objects.all() # 전체 게시물 조회

        # 객체 시리얼화
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FeedSerializer(data=request.data)

        if serializer.is_valid():
            feed = serializer.save(user=request.user)
            serializer = FeedSerializer(feed)
            # print("post serializer", serializer)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
# (2) 전체 데이터에서 일부 정보만 보여주는 Serialize
#  class FeedList(APIView):
#     def get(self, request):
#         feeds = Feed.objects.all()
#         serializer = FeedListSerializer(feeds, many=True)
#         return Response(serializer.data)

# (2) 일부 데이터를 보여주는 Serialize
class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound
        
    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        serializer = FeedSerializer(feed)
        return Response(serializer.data)
