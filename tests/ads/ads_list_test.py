import pytest

from ads.serializers import AdsSerializer
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_ads_list(client):
    ads = AdsFactory.create_batch(5)
    expected_response = {
        "count": 5,
        "next": None,
        "previous": None,
        "results": AdsSerializer(ads, many=True).data
    }

    response = client.get("/ads/")

    assert response.status_code == 200
    assert response.data == expected_response
