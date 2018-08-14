from django.db.models import Q
from book.models import Book
from book.serializers import (
    BookListSerializer,
    BookFilterSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookFilterView(APIView):
    @staticmethod
    def post(request):
        book_filter = Q()
        for word in request.data.get('pieces'):
            book_filter &= Q(text__icontains=word)
        queryset = Book.objects.filter(book_filter)
        if queryset.exists():
            serializer = BookFilterSerializer(queryset, many=True, context={"request": request})
            return Response(data=serializer.data)
        return Response({"message": "Нет данных!"})
