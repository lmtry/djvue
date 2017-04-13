from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet
from django.db import models

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')