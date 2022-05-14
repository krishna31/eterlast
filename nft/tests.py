
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from nft.models import NFT, Collection


class NFTTest(APITestCase):
    # def test_create_nft(self):
    #     """
    #     Ensure we can create a new NFT object.
    #     """
    #     url = 'http://localhost:8000/nft-api/v1/mint'
    #     data = {
    #         "name": "nft10",
    #         "external_link": "https://example.com",
    #         "description": "TEST 2 test 2 test 5",
    #         "picture": "abc.jpeg",
    #         "supply": "3",
    #         "royalties": "10",
    #         "collection": "1",
    #         "buyer": "1"
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_nft_all(self):
        """
        Ensure we can get all NFT object.
        """
        url = 'http://localhost:8000/nft-api/v1/NFT/all'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_nft(self):
    #     """
    #     Ensure we can get a NFT object.
    #     """
    #     url = 'http://localhost:8000/nft-api/v1/NFT/0278758d-61bb-4fb9-8f65-53de307285c3'
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class CollectionTest(APITestCase):
    def test_create_collection(self):
        """
        Ensure we can create a new Collection object.
        """
        url = 'http://localhost:8000/nft-api/v1/create_collection'
        data = {
            "name": "collection name 3",
            "description": "Collection 2 abc",
            "creator_network": "1"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_collection_all(self):
        """
        Ensure we can get all Collection object.
        """
        url = 'http://localhost:8000/nft-api/v1/collection/all'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_collection_nft(self):
    #     """
    #     Ensure we can get a Collection object.
    #     """
    #     url = 'http://localhost:8000/nft-api/v1/collection/7d385c6e-caa6-4443-917d-aaa37d1a6361'
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
