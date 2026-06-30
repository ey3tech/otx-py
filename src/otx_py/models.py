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
    attack_ids: list[str]
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