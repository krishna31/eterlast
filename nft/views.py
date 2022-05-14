# from django.shortcuts import render

from rest_framework import status, views, viewsets

from rest_framework.response import Response

from django.shortcuts import get_object_or_404

# from rest_framework.permissions import IsAuthenticated

from eterlast.mixins import JSONResponseMixin

from nft.serializers import NFTSerializer, CollectionSerializer

from nft.models import NFT, Collection
# Create your views here.


class NFTMintView(JSONResponseMixin, viewsets.ViewSetMixin, views.APIView):
    """Post NFT Data."""

    # permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = NFT.objects.all()
        serializer = NFTSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, asset_id=None):
        obj = NFT.objects.get(asset_id=asset_id)
        serializer = NFTSerializer(obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create_nft(self, request, format=None):
        """Create NFT API"""
        serializer = NFTSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionView(JSONResponseMixin, viewsets.ViewSetMixin, views.APIView):
    """Post Collection Data."""

    # permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Collection.objects.all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, uuid=None):
        obj = Collection.objects.get(uuid=uuid)
        serializer = CollectionSerializer(obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create_collection(self, request, format=None):
        """Create Collection API"""
        serializer = CollectionSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)