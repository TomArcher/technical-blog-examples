# collision_scenario.py

from dataclasses import dataclass
from typing import Optional
from collision_probability import collision_probability
from collision_threshold import find_collision_threshold
from id_system import IDSystem

@dataclass
class CollisionScenario:
    """Model a production system's collision risk"""
    name: str
    system: IDSystem
    current_items: int
    growth_rate: float  # items per day
    acceptable_risk: float = 1e-6  # 1 in a million

    def current_risk(self) -> float:
        """Current collision probability"""
        return collision_probability(
            self.current_items,
            self.system.space_size
        )

    def days_until_risk(self) -> Optional[float]:
        """Days until we hit acceptable_risk threshold"""
        threshold_items = find_collision_threshold(
            self.system.space_size,
            self.acceptable_risk
        )
        if self.current_items >= threshold_items:
            return 0.0
        return (threshold_items - self.current_items) / self.growth_rate

    def safety_factor(self) -> float:
        """How many times current load before 50% collision"""
        n_half = find_collision_threshold(self.system.space_size, 0.5)
        return n_half / self.current_items
