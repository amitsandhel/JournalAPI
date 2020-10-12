#serializers.py
from rest_framework import serializers

from .models import JMIR

class JMIRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JMIR
        fields = ["pk", "reference_count", "publisher", "issuex", "short_container_title", "DOI","article_type",
        			"page","source", "title", "prefix", "volume", "member", "container_title", "language",
        			"score", "issn", "url"]