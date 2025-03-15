from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import YourModel, User, GoogleAuth, Score, ScoreMetadata
from .serializers import YourModelSerializer, UserSerializer, GoogleAuthSerializer, ScoreSerializer, ScoreMetadataSerializer
from .filters import ScoreFilter, YourModelFilter
from django.shortcuts import render

def api_root(request):
    return render(request, 'api_root.html')

class YourModelListCreateAPIView(generics.ListCreateAPIView):
    """
    YourModelのリストと作成を提供するAPIView。
    テスト用。
    """
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = YourModelFilter

class YourModelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    YourModelの詳細表示、更新、削除を提供するAPIView。
    テスト用。
    """
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    """
    ユーザーのリストと作成を提供するAPIView。
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    ユーザーの詳細表示、更新、削除を提供するAPIView。
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GoogleAuthListCreateAPIView(generics.ListCreateAPIView):
    """
    Googleアカウント認証のリストと作成を提供するAPIView。
    """
    queryset = GoogleAuth.objects.all()
    serializer_class = GoogleAuthSerializer

class GoogleAuthRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Googleアカウント認証の詳細表示、更新、削除を提供するAPIView。
    """
    queryset = GoogleAuth.objects.all()
    serializer_class = GoogleAuthSerializer

class ScoreListCreateAPIView(generics.ListCreateAPIView):
    """
    楽譜のリストと作成を提供するAPIView。
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ScoreFilter

class ScoreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    楽譜の詳細表示、更新、削除を提供するAPIView。
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class ScoreMetadataListCreateAPIView(generics.ListCreateAPIView):
    """
    楽譜メタデータのリストと作成を提供するAPIView。
    """
    queryset = ScoreMetadata.objects.all()
    serializer_class = ScoreMetadataSerializer

class ScoreMetadataRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    楽譜メタデータの詳細表示、更新、削除を提供するAPIView。
    """
    queryset = ScoreMetadata.objects.all()
    serializer_class = ScoreMetadataSerializer
