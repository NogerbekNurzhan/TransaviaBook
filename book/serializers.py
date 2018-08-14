from rest_framework import serializers
from book.models import Book


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'text')


class BookFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'text')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        elements = data['text'].split()
        for word in self.context['request'].data.get('cutouts'):
            for element in elements:
                if word in element:
                    elements.remove(element)
            data['text'] = " ".join(elements)
        return data
