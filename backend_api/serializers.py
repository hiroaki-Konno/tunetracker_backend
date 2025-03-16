from rest_framework import serializers
from .models import YourModel
from .models import User, GoogleAuth, Score, ScoreMetadata

class YourModelSerializer(serializers.ModelSerializer):
    """
    YourModelのシリアライザー。
    モデルの全フィールドをシリアライズします。
    """
    class Meta:
        model = YourModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    """
    Userモデルのシリアライザー。
    モデルの全フィールドをシリアライズします。
    """
    class Meta:
        model = User
        fields = '__all__'

class GoogleAuthSerializer(serializers.ModelSerializer):
    """
    GoogleAuthモデルのシリアライザー。
    モデルの全フィールドをシリアライズします。
    """
    class Meta:
        model = GoogleAuth
        fields = '__all__'

class ScoreMetadataSerializer(serializers.ModelSerializer):
    """
    ScoreMetadataモデルのシリアライザー。
    モデルの全フィールドをシリアライズします。
    """
    class Meta:
        model = ScoreMetadata
        fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):
    """
    Scoreモデルのシリアライザー。
    ScoreMetadataのネストされたシリアライザーを含みます。

    属性:
        scoremetadata_set (ScoreMetadataSerializer): ScoreMetadataのネストされたシリアライザー、読み取り専用。
    """
    metadata  = ScoreMetadataSerializer(read_only=True)

    class Meta:
        model = Score
        fields = '__all__'
