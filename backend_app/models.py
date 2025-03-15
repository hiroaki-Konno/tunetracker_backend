from django.db import models

# Create your models here.

class YourModel(models.Model):
    """_summary_
    テスト用のモデル
    """    
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.artist}"

class User(models.Model):
    """
    ユーザーモデル。ユーザー情報を保存します。

    Attributes:
        user_id: ユーザーの一意のID。
        username: ユーザーの名前。
        email: ユーザーのメールアドレス。
        profile_information: ユーザーの追加プロフィール情報。
    """
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_information = models.TextField()

    def __str__(self):
        return self.username

class GoogleAuth(models.Model):
    """
    Googleアカウントの認証情報モデル。

    Attributes:
        auth_id: 認証情報の一意のID。
        user: この認証情報に関連付けられたユーザー。
        google_id_token: Google IDトークン。
        access_token: Googleサービスへのアクセストークン。
        refresh_token: アクセストークンを更新するためのリフレッシュトークン。
        token_expiry: アクセストークンの有効期限日時。
    """
    auth_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    google_id_token = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    token_expiry = models.DateTimeField()

    def __str__(self):
        return f"Auth {self.auth_id} for {self.user.username}"

class Score(models.Model):
    """
    楽譜情報を保存するモデル。

    Attributes:
        score_id: 楽譜の一意のID。
        title: 楽譜のタイトル。
        composer: 楽譜の作曲者。
        instrument: 楽譜に関連付けられた楽器。
        generated_score_url: 生成された楽譜のURL。
        version_information: 楽譜のバージョン情報。
        user: この楽譜を作成または所有するユーザー。
        video_url: 関連する動画のURL。
        downloaded_video_path: ダウンロードされた動画のファイルパス。
        start_coordinate: 楽譜の始点座標。
        end_coordinate: 楽譜の終点座標。
    """
    score_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    composer = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    generated_score_url = models.URLField()
    version_information = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_url = models.URLField()
    downloaded_video_path = models.CharField(max_length=255)
    start_coordinate = models.CharField(max_length=100)
    end_coordinate = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class ScoreMetadata(models.Model):
    """
    楽譜のメタデータ情報を保存するモデル。

    Attributes:
        metadata_id: メタデータの一意のID。
        score: このメタデータに関連付けられた楽譜。
        title: 楽譜のタイトル。
        composer: 楽譜の作曲者。
        instrument: 楽譜に関連付けられた楽器。
        genre: 楽譜のジャンル。
        duration: 楽譜の長さ。
        upload_date: 楽譜のアップロード日。
        description: 楽譜の説明。
        tags: 楽譜に関連するタグ。
    """
    metadata_id = models.AutoField(primary_key=True)
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    composer = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    duration = models.DurationField()
    upload_date = models.DateField()
    description = models.TextField()
    tags = models.CharField(max_length=255)

    def __str__(self):
        return f"Metadata for {self.score.title}"

