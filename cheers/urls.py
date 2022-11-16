from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # 레시피
    path('recipes/', views.RecipeListView.as_view(), name='recipe-list'),
    path('recipes/following/', views.FollowingRecipeListView.as_view(), name='following-recipe-list'),
    path('recipes/<int:recipe_id>/', views.RecipeDetailView.as_view(),name='recipe-detail'),
    path('recipes/create/', views.RecipeCreateView.as_view(), name="recipe-create"),
    path('recipes/<int:recipe_id>/edit/', views.RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipes/<int:recipe_id>/delete/', views.RecipeDeleteView.as_view(), name="recipe-delete"),
    # 유저 
    path('users/<int:user_id>/', views.ProfileView.as_view(), name="profile"),
    path('users/<int:user_id>/recipes/', views.UserRecipesListView.as_view(), name="user-recipe-list"),
    path('setting-profile/', views.ProfileSettingView.as_view(), name='profile-setting'),
    path('update-profile/', views.ProfileUpdateView.as_view(), name='profile-update'),
    # 댓글
    path('recipes/<int:recipe_id>/comments/create/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:comment_id>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:comment_id>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    # 좋아요
    path('like/<int:content_type_id>/<int:object_id>/', views.ProcessLikeView.as_view(), name='process-like'),
    # 팔로우
    path('users/<int:user_id>/follow/', views.ProcessFollowView.as_view(), name='process-follow'),
    path('users/<int:user_id>/following/', views.FollowingListView.as_view(), name='following-list'),
    path('users/<int:user_id>/followers/', views.FollowerListView.as_view(), name='follower-list'),
    # 검색
    path('search/', views.SearchView.as_view(), name='search'),
]