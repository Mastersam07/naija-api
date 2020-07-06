
from rest_framework import serializers

from .models import State, LocalGovernmentArea


class LocalGovernmentAreaSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        fields = ('name', 'id')
        model = LocalGovernmentArea

    def get_name(self, obj):
        return obj.name.title()


class StateSerializer(serializers.HyperlinkedModelSerializer):
    lgas = serializers.HyperlinkedIdentityField(
        view_name='state-lga-list', lookup_field='slug')
    name = serializers.SerializerMethodField()
    capital = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'lgas', 'name', 'capital')
        model = State

    def get_name(self, obj):
        return obj.name.title()

    def get_capital(self, obj):
        return obj.capital.title()
