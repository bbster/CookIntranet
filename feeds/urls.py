from django.urls import path

# router = DefaultRouter()
# router.register('', FeedViewSet)
#
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

from feeds.views import broadcast, conversations, delivered

urlpatterns = [
    path('conversation/', broadcast),
    path('conversations/', conversations),
    path('conversations/<int:id>/delivered/', delivered),
    ]

