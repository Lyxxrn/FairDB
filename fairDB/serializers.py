from rest_framework import serializers
from .models import *

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = ['rating']

class ProductRatingResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    new_gold_stars = serializers.IntegerField()
    new_gray_stars = serializers.IntegerField()
    message = serializers.CharField()

class ProductSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, required=False)

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        product = Product.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            ingredient = Ingredient.objects.create(**ingredient_data)
            product.ingredients.add(ingredient)
        return product

    class Meta:
        model = Product
        fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = '__all__'