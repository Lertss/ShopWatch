from rest_framework import serializers

from .models import *


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username','password')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("first_name",
                  "last_name",
                  "get_absolute_url"
                  )
        # extra_kwargs = {'actors': {'required': False}}


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id",
                  "counts",)


class GenreSerializator(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id",
                  "genr")


class TegsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id",
                  "teg")


# class CategorySerializer(serializers.ModelSerializer):
#     cin = SerializerMethodField()
#
#     class Meta:
#         model = Categorys
#         fields = ("id",
#                   "title",
#                   "cin",
#                   'get_absolute_url',
#                   )


class CategorySerializer(serializers.ModelSerializer):
    accounts_items = serializers.SerializerMethodField()

    class Meta:
        fields = ("id",
                  "title",
                  'accounts_items',
                  'get_absolute_url',
                  )
        model = Categorys

    def get_accounts_items(self, obj):
        customer_account_query = Manga.objects.filter(
            category_id=obj.id)
        serializer = MangaSerializer(customer_account_query, many=True)

        return serializer.data


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ("id",
                  "get_image",)


class GlawaSerializer(serializers.ModelSerializer):
    galleries = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = Glawa
        fields = ("id",
                  "num",
                  "get_absolute_url",
                  "title",
                  "time_prod",
                  "data_g",
                  "galleries",
                  "manga_id",)


class MangaSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)
    counts = CountrySerializer(many=True, read_only=True)
    glaws = GlawaSerializer(many=True, read_only=True, )

    class Meta:
        model = Manga
        fields = ('id',
                  'name_manga',
                  'name_original',
                  'author',
                  'time_prod',
                  'counts',
                  'genre',
                  'glaws',
                  'review',
                  'get_thumbnail',
                  'get_avatar',
                  'get_absolute_url',
                  )


