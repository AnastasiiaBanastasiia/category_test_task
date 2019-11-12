from rest_framework import serializers

from categories.models import Category


class SimpleCategorySerializer(serializers.ModelSerializer):
    children = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'children')


class CategorySerializer(serializers.ModelSerializer):
    children = SimpleCategorySerializer(many=True, required=False)
    parents = SimpleCategorySerializer(many=True, read_only=True)
    siblings = SimpleCategorySerializer(many=True, read_only=True)

    def create(self, validated_data):
        children = validated_data.pop('children', [])
        category = super().create(validated_data)
        for child in children:
            serializer = CategorySerializer(data=child)
            serializer.is_valid(raise_exception=True)
            serializer.save(parent=category)

        return category

    class Meta:
        model = Category
        fields = ('id', 'name', 'children', 'parents', 'siblings')
