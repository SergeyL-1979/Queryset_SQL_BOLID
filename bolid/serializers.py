from drf_extra_fields.fields import Base64ImageField
import base64
from rest_framework import serializers

from bolid.models import (
    Authorities, Plist, Ppost, Pcompany, Plogdata,
    Querylog, LogsChangeBd, Events, Pdivision
)
from sqlquerybolid import settings


class PpostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ppost
        fields = '__all__'


class PcompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pcompany
        fields = '__all__'


class PListSerializer(serializers.ModelSerializer):
    post = PpostSerializer(read_only=True)
    company = PcompanySerializer()
    # picture = Base64ImageField(represent_in_base64=False)

    class Meta:
        model = Plist
        fields = ["id", "name", "firstname", "midname", "post", "tabnumber", "company", "picture"]


class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ["event",  "contents", ]


class PlogdataSerializer(serializers.ModelSerializer):
    hozorgan = PListSerializer()
    devicetime = serializers.DateTimeField(settings.DATETIME_FORMAT,)
    timeval = serializers.DateTimeField(settings.DATETIME_FORMAT,)
    event = EventsSerializer()

    class Meta:
        model = Plogdata
        fields = ["devicetime", "hozorgan", "remark", "timeval", "event", ]  # '__all__'


class AuthoritiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authorities
        fields = '__all__'


class QuerylogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Querylog
        fields = '__all__'


class LogsChangeBdSerializer(serializers.ModelSerializer):
    # valueid = PListSerializer(many=True, read_only=True)

    class Meta:
        model = LogsChangeBd
        fields = '__all__'  # ["id", "timeval", "table_name", "valueid", "xml_data", ]


class PdivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pdivision
        fields = '__all__'

