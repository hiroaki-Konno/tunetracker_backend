from django_filters import rest_framework as filters
from .models import Score, YourModel

class YourModelFilter(filters.FilterSet):
    """
    YourModelのインスタンスをフィルタリングするためのFilterSetです。
    タイトル、アーティスト、アルバム、ジャンル、リリース日でフィルタリングできます。

    属性:
        title (CharFilter): タイトルでフィルタリング（大文字小文字を区別しない）。
        artist (CharFilter): アーティストでフィルタリング（大文字小文字を区別しない）。
        album (CharFilter): アルバムでフィルタリング（大文字小文字を区別しない）。
        genre (CharFilter): ジャンルでフィルタリング（完全一致）。
        release_date (NumberFilter): リリース年でフィルタリング。

    Meta:
        model (YourModel): フィルタリングされるモデル。
        fields (list): フィルタリング可能なフィールドのリスト。
    """
    title = filters.CharFilter(lookup_expr='icontains')
    artist = filters.CharFilter(lookup_expr='icontains')
    album = filters.CharFilter(lookup_expr='icontains')
    genre = filters.CharFilter(lookup_expr='exact')
    release_date = filters.NumberFilter(field_name='release_date', lookup_expr='year')

    class Meta:
        model = YourModel
        fields = ['title', 'artist', 'album', 'genre', 'release_date']


class ScoreFilter(filters.FilterSet):
    """
    ScoreのインスタンスをフィルタリングするためのFilterSetです。
    タイトル、作曲者、楽器でフィルタリングできます。

    属性:
        title (CharFilter): タイトルでフィルタリング（大文字小文字を区別しない）。
        composer (CharFilter): 作曲者でフィルタリング（大文字小文字を区別しない）。
        instrument (CharFilter): 楽器でフィルタリング（大文字小文字を区別しない）。

    Meta:
        model (Score): フィルタリングされるモデル。
        fields (list): フィルタリング可能なフィールドのリスト。
    """
    title = filters.CharFilter(lookup_expr='icontains')
    composer = filters.CharFilter(lookup_expr='icontains')
    instrument = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Score
        fields = ['title', 'composer', 'instrument']
