from django.urls import path
from . import views

urlpatterns = [
    # path('data/<str:search_term>/', views.get_filtered_data_by_id, name='get_filtered_data'),
    # path('data/', views.get_filtered_data, name='get_filtered_data'),
    path('data/', views.YourModelListCreateAPIView.as_view(), name='yourmodel_list_create'),
    path('data/<int:pk>/', views.YourModelRetrieveUpdateDestroyAPIView.as_view(), name='yourmodel_detail'),

    # ユーザーテーブル関連のAPI URL
    path('users/', views.UserListCreateAPIView.as_view(), name='user_list_create'),
    path('users/<int:user_id>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='user_detail'),
    
    # Googleアカウント認証関連のAPI URL
    path('google-auth/', views.GoogleAuthListCreateAPIView.as_view(), name='google_auth_list_create'),
    path('google-auth/<int:auth_id>/', views.GoogleAuthRetrieveUpdateDestroyAPIView.as_view(), name='google_auth_detail'),
    
    # 楽譜関連のAPI URL
    path('scores/', views.ScoreListCreateAPIView.as_view(), name='score_list_create'),
    path('scores/<int:score_id>/', views.ScoreRetrieveUpdateDestroyAPIView.as_view(), name='score_detail'),
    
    # 楽譜メタデータ関連のAPI URL
    path('metadata/', views.ScoreMetadataListCreateAPIView.as_view(), name='metadata_list_create'),
    path('metadata/<int:metadata_id>/', views.ScoreMetadataRetrieveUpdateDestroyAPIView.as_view(), name='metadata_detail'),
]