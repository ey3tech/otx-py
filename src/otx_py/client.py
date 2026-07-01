from httpx import Client
from otx_py.models import Pulse,IndcaterTypeResponse
from msgspec.json import decode
from msgspec import Struct

class PulsesResponse(Struct):
    count: int
    results: list[Pulse]

class OTXClient:
    __slots__ = ("api_key", "client")
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = Client(base_url="https://otx.alienvault.com/api/v1", headers={"X-OTX-API-KEY": api_key})

    def pulses(self, limit: int = 25) -> PulsesResponse:
        response = self.client.get("https://otx.alienvault.com/otxapi/pulses", params={"limit": limit, "page": 1, "sort": "-modified"}, timeout=60)
        return decode(response.text, type=PulsesResponse)
    
    def indcater_type_response(self) -> IndcaterTypeResponse:
        response = self.client.get("/pulses/indicators/types", timeout=60)
        return decode(response.text, type=IndcaterTypeResponse)
