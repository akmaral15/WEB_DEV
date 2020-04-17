from rest_framework import serializers

from api.models import Company , Vacancy


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data.get('name'))
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class CompanySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name','city', 'description',  'address')


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer2(read_only=True)
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company', 'company_id')


class CompanyWithVacanciesSerializer(serializers.ModelSerializer):

    vacancies = VacancySerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'vacancies')