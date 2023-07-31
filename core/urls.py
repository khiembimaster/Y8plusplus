from django.urls import path
from .views import GameList, GameDetail, GamePublish, GameUpdate, GameDelete


urlpatterns = [
    path('', GameList.as_view(), name='games'),
    path('game/<int:pk>/', GameDetail.as_view(), name='game'),
    path('game-publish/', GamePublish.as_view(), name='game-publish'),
    path('game-update/<int:pk>/', GameUpdate.as_view(), name='game-update'),
    path('game-delete/<int:pk>/', GameDelete.as_view(), name='game-delete'),
]