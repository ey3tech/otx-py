from msgspec import Struct
from datetime import datetime


class Author(Struct):
    username: str
    id: str
    avatar_url: str
    is_subscribed: bool
    is_following: bool


class Pulse(Struct):
    id: str
    name: str
    description: str
    modified: datetime
    created: datetime
    tags: list[str]
    references: list[str]
    public: int
    adversary: str
    targeted_countries: list[str]
    malware_families: list[dict]
    attack_ids: list[dict]
    industries: list[str]
    TLP: str
    cloned_from: str | None
    export_count: int
    upvotes_count: int
    downvotes_count: int
    votes_count: int
    locked: bool
    pulse_source: str
    validator_count: int
    comment_count: int
    follower_count: int
    vote: int
    author: Author
    indicator_type_counts: dict[str, int]
    indicator_count: int
    is_author: bool
    is_subscribing: bool | None
    subscriber_count: int
    modified_text: str
    is_modified: bool
    groups: list[str]
    in_group: bool
    threat_hunter_scannable: bool
    threat_hunter_has_agents: int


class IndicatorType(Struct):
    name: str
    description: str
    slug: str


class IndicatorTypeResponse(Struct):
    detail: list[IndicatorType]


class BaseIndicator(Struct):
    id: int
    indicator: str
    type: str
    title: str
    description: str
    content: str
    access_type: str
    access_reason: str


class RelatedIndcator(Struct):
    adversary: list[str]
    malware_families: list[str]
    industries: list[str]


class Related(Struct):
    alienvault: RelatedIndcator
    other: RelatedIndcator


class PulseInfo(Struct):
    count: int
    references: list[str]
    pulses: list[Pulse]
    related: Related


class IndicatorLookUpResponse(Struct):
    base_indicator: BaseIndicator
    whois: str
    reputation: int
    indicator: str
    type: str
    type_title: str
    pulse_info: PulseInfo
    false_positive: list[str]
    validation: list[str]
    asn: str
    city_data: bool
    city: str | None
    region: str | None
    continent_code: str
    country_code3: str
    country_code2: str
    subdivision: str | None
    latitude: float
    postal_code: str | None
    longitude: float
    accuracy_radius: int
    country_code: str
    country_name: str
    dma_code: int
    charset: int
    area_code: int
    flag_url: str
    flag_title: str
    sections: list[str]


class User(Struct):
    subscriber_count: int
    follower_count: int
    member_since: str
    avatar_url: str
    award_count: int
    awards: list[dict]
    user_id: int
    username: str
    indicator_count: int
    pulse_count: int
    accepted_edits_count: int


class UserSearchResponse(Struct):
    count: int
    previous: str | None
    next: str | None
    results: list[User]


class PulseSearchResponse(Struct):
    count: int
    previous: str | None
    next: str | None
    results: list[Pulse]
