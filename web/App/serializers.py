from rest_framework import serializers
from .models import Courtpdfprocesstion, Requestjson

class RequestjsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requestjson
        fields =['Court','start_date','end_date']
    def create(self, validated_data):
        return Requestjson.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.Court = validated_data.get('Court', instance.Court)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)

class CourtpdfprocesstionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courtpdfprocesstion
        fields = ['File_Name','Judge_Name','Judgement_Date','Party_One','Party_Two','Case_Number','Judgement_Order','Judgement_Type','Court_Name']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Courtpdfprocesstion.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.File_Name = validated_data.get('File_Name', instance.File_Name)
        instance.Judge_Name = validated_data.get('Judge_Name', instance.Judge_Name)
        instance.Judgement_Date = validated_data.get('Judgement_Date', instance.Judgement_Date)
        instance.Party_One = validated_data.get('Party_One', instance.Party_One)
        instance.Party_Two = validated_data.get('Party_Two', instance.Party_Two)
        instance.Case_Number = validated_data.get('Case_Number', instance.Case_Number)
        instance.Judgement_Order = validated_data.get('Judgement_Order', instance.Judgement_Order)
        instance.Judgement_Type = validated_data.get('Judgement_Type', instance.Judgement_Type)
        instance.Court_Name = validated_data.get('Court_Name', instance.Court_Name)
        instance.save()
        return instance