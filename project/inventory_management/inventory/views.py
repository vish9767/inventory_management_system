from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.core.cache import cache
from .models import Item
from .serializers import ItemSerializer

class ItemCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, item_id):
        cache_key = f"item_{item_id}"
        item = cache.get(cache_key)
        if not item:
            try:
                item = Item.objects.get(id=item_id)
            except Item.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
            # Serialize and store in Redis cache
            serializer = ItemSerializer(item)
            cache.set(cache_key, serializer.data, timeout=60*15)  # Cache for 15 minutes
            return Response(serializer.data)
        return Response(item)  # Cached data

    def put(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Update cache after update
            cache_key = f"item_{item_id}"
            cache.set(cache_key, serializer.data, timeout=60*15)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
            item.delete()
            # Remove from cache
            cache_key = f"item_{item_id}"
            cache.delete(cache_key)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
