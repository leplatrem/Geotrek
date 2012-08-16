import sys
from django_filters import RangeFilter
from decimal import Decimal


class OptionalRangeFilter(RangeFilter):
    def filter(self, qs, value):
        if value:
            if value.start and not value.stop:
                value = slice(value.start, Decimal(sys.maxint), value.step)
            if not value.start and value.stop:
                value = slice(Decimal(-(sys.maxint +1)), value.stop, value.step)
        return super(OptionalRangeFilter, self).filter(qs, value)