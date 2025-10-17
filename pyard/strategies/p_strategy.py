# -*- coding: utf-8 -*-
from typing import override

from .base_strategy import ReductionStrategy


class PGroupStrategy(ReductionStrategy):
    """Strategy for P group reduction"""

    @override
    def reduce(self, allele: str) -> str:
        # Try data repository first for cached access
        if hasattr(self.ard, "data_repository"):
            p_mapping = self.ard.data_repository.get_p_group_mapping(allele)
            if p_mapping:
                return p_mapping

        # Fallback to original mappings
        if allele in self.ard.ars_mappings.p_group:
            return self.ard.ars_mappings.p_group[allele]

        return super().reduce(allele)
