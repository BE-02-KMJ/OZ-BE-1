from django.urls import path
from . import views

# urlpatterns = [
#     path("", views.show_feed),
#     path("all", views.all_feed),
#     path("<int:feed_id>/<str:feed_content>/",views.one_feed)
# ]

urlpatterns = [
    path("", views.Feeds.as_view()),
    # path("list", views.FeedList.as_view()),
    path("<int:feed_id>", views.FeedDetail.as_view())
]