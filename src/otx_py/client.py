from httpx import Client
from otx_py.models import (
    Pulse,
    IndicatorTypeResponse,
    UserSearchResponse,
    PulseSearchResponse,
    User,
    PulseId,
    PulseIdIndicators
)
from msgspec.json import decode
from msgspec import Struct


class PulsesResponse(Struct):
    count: int
    results: list[Pulse]


class OTXClient:
    __slots__ = ("api_key", "client")

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = Client(
            base_url="https://otx.alienvault.com/api/v1",
            headers={"X-OTX-API-KEY": api_key},
        )

    def pulses(self, limit: int = 25) -> PulsesResponse:
        response = self.client.get(
            "https://otx.alienvault.com/otxapi/pulses",
            params={"limit": limit, "page": 1, "sort": "-modified"},
            timeout=60,
        )
        return decode(response.text, type=PulsesResponse)

    def indicator_types(self) -> IndicatorTypeResponse:
        response = self.client.get("/pulses/indicators/types", timeout=60)
        return decode(response.text, type=IndicatorTypeResponse)

    def search_users(
        self, query: str, page: int = 1, limit: int = 20
    ) -> UserSearchResponse:
        response = self.client.get(
            "/search/users",
            params={"q": query, "page": page, "limit": limit},
            timeout=60,
        )
        return decode(response.text, type=UserSearchResponse)

    def search_pulses(
        self, query: str, page: int = 1, limit: int = 20
    ) -> PulseSearchResponse:
        response = self.client.get(
            "/search/pulses",
            params={"q": query, "page": page, "limit": limit},
            timeout=60,
        )
        return decode(response.text, type=PulseSearchResponse)

    def get_user(self, username: str, detail: bool ) -> User:
        response = self.client.get(f"/users/{username}", timeout=60, params={"detailed": int(detail)})
        return decode(response.text, type=User)
    
    def pulse_id(self, pulse_id: str) -> PulseId:
        response = self.client.get(f"/pulses/{pulse_id}", timeout=60)
        return decode(response.text, type=PulseId)
    
    def pulse_id_indicators(self, pulse_id: str, limit: int = 50) -> PulseIdIndicators:
        response = self.client.get(f"/pulses/{pulse_id}/indicators", timeout=60, params={"limit": limit})
        return decode(response.text, type=PulseIdIndicators)
