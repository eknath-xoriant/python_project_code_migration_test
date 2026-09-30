from dataclasses import dataclass
from typing import List


@dataclass
class UserProfile:
    first_name: str
    index: int

    def display_name(self) -> str:
        return f"{self.first_name}-{self.index}"


def build_profiles(first_name: str, count: int) -> List[UserProfile]:
    return [UserProfile(first_name, idx) for idx in range(count)]
