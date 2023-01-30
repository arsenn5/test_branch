from rest_framework import serializers
from car.models import Brand



class BrandSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(min_length=1,
                                  max_length=50,
                                  )

    class Meta:
        model = Brand
        fields = '__all__'
