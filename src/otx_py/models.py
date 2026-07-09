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
    description: str | None
    modified: datetime
    created: datetime
    tags: list[str]
    references: list[str]
    public: int
    adversary: str | None
    targeted_countries: list[str]
    malware_families: list[dict]
    attack_ids: list[dict]
    industries: list[str]
    TLP: str
    author: Author
    is_subscribing: bool | None
    groups: list[str]
    in_group: bool
    is_modified: bool | None = None
    modified_text: str | None = None
    is_author: bool | None = None
    indicator_type_counts: dict[str, int] | None = None
    indicator_count: int | None = None
    threat_hunter_scannable: bool | None = None
    vote: int | None = None
    threat_hunter_has_agents: int | None = None
    locked: bool | None = None
    validator_count: int | None = None
    pulse_source: str | None = None
    comment_count: int | None = None
    follower_count: int | None = None
    subscriber_count: int | None = None
    upvotes_count: int | None = None
    downvotes_count: int | None = None
    votes_count: int | None = None
    export_count: int | None = None
    cloned_from: str | None = None


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
    username: str
    indicator_count: int
    pulse_count: int
    request_user_is_subscribed: bool | None = None
    request_user_is_following: bool | None = None
    request_user_is_me: bool | None = None
    user_id: int | None = None
    award_count: int | None = None
    accepted_edits_count: int | None = None
    awards: list[dict] | None = None

class Indicators(Struct):
    id: int
    indicator: float
    type: str
    title: str
    description: str
    content: str
    created: datetime
    is_active: int
    expiration: datetime
class PulseId(Struct):
    id: str | None = None
    name: str | None = None
    description: str | None = None
    author_name: str | None = None
    created: datetime | None = None
    modified: datetime | None = None
    public: bool | None = None
    TLP: str | None = None
    adversary: str | None = None
    tags: list[str] | None = None
    references: list[str] | None = None
    targeted_countries: list[str] | None = None
    industries: list[str] | None = None
    malware_families: list[str] | None = None
    attack_ids: list[str] | None = None
    indicator_count: int | None = None
    subscriber_count: int | None = None
    upvotes_count: int | None = None
    group_ids: list[int] | None = None
    details: list[Indicators] | None = None


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


class results(Struct):
    id: int
    indicator: float
    type: str
    title: str
    description: str
    content: str
    created: datetime
    is_active: int
    expiration: datetime
class PulseIdIndicators(Struct):
    next: str
    previous: str
    details: list[results]
    count: int | None = None

