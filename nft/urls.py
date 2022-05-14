from django.urls import path

from nft import views as nft_viwes

urlpatterns = [
    path(
        "v1/mint",
        nft_viwes.NFTMintView.as_view(
            {"post": "create_nft"},
            http_method_names=["post"]
        ),
    ),
    path(
        "v1/NFT/all",
        nft_viwes.NFTMintView.as_view(
            {"get": "list"},
            http_method_names=["get"]
        ),
        name="get_nft_data_all"
    ),
    path(
        "v1/NFT/<str:asset_id>",
        nft_viwes.NFTMintView.as_view(
            {"get": "retrieve"},
            http_method_names=["get"]
        ),
        name="get_nft_data"
    ),
    path(
        "v1/create_collection",
        nft_viwes.CollectionView.as_view(
            {"post": "create_collection"},
            http_method_names=["post"]
        ),
    ),
    path(
        "v1/collection/all",
        nft_viwes.CollectionView.as_view(
            {"get": "list"},
            http_method_names=["get"]
        ),
        name="get_collection_data_all"
    ),
    path(
        "v1/collection/<str:uuid>",
        nft_viwes.CollectionView.as_view(
            {"get": "retrieve"},
            http_method_names=["get"]
        ),
        name="get_collection_data"
    ),
]
