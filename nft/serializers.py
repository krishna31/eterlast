from rest_framework import serializers

from nft.models import NFT, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class NFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = '__all__'


# class NFTCollectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NFT

