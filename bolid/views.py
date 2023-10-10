import django

from rest_framework import viewsets
from rest_framework import generics
from django_filters import rest_framework as filters
from bolid.models import (
    Authorities, Plist, Ppost, Plogdata, Querylog,
    LogsChangeBd, Events, Pdivision, Pcompany
)
from bolid.serializers import (
    AuthoritiesSerializer, PListSerializer,
    PpostSerializer, PlogdataSerializer, QuerylogSerializer, LogsChangeBdSerializer,
    EventsSerializer, PdivisionSerializer, PcompanySerializer
)


class QuerylogViewSet(viewsets.ModelViewSet):
    queryset = Querylog.objects.all()
    serializer_class = QuerylogSerializer


class AuthoritiesViewSet(viewsets.ModelViewSet):
    queryset = Authorities.objects.all()
    serializer_class = AuthoritiesSerializer


class PlistViewSet(viewsets.ModelViewSet):
    queryset = Plist.objects.all()
    serializer_class = PListSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filterset_fields = ["company", "post"]


class PpostViewSet(viewsets.ModelViewSet):
    queryset = Ppost.objects.all()
    serializer_class = PpostSerializer


class PcompanyViewSet(viewsets.ModelViewSet):
    queryset = Pcompany.objects.all()
    serializer_class = PcompanySerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filterset_fields = ["name"]


class PlogdataFilter(filters.FilterSet):
    min_date = filters.DateFilter(lookup_expr='gte', field_name='devicetime',
                                  widget=django.forms.DateInput(attrs={'type': 'date'})
                                  )
    max_date = filters.DateFilter(lookup_expr='lte', field_name='devicetime',
                                  widget=django.forms.DateInput(attrs={'type': 'date'})
                                  )

    class Meta:
        model = Plogdata
        fields = ['hozorgan', 'event']


class PlogdataViewSet(viewsets.ModelViewSet):
    queryset = Plogdata.objects.all()
    serializer_class = PlogdataSerializer
    filter_backends = [filters.DjangoFilterBackend, ]  # filters.SearchFilter]
    filterset_class = PlogdataFilter


class LogsChangeBdViewSet(viewsets.ModelViewSet):
    queryset = LogsChangeBd.objects.all()
    serializer_class = LogsChangeBdSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class PdivisionViewSet(viewsets.ModelViewSet):
    queryset = Pdivision.objects.all()
    serializer_class = PdivisionSerializer

