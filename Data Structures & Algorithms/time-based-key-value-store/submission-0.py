from collections import defaultdict
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.key_to_time_value = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_time_value[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_time_value:
            return ''
        
        time_value_list = self.key_to_time_value[key]

        insertion_index = bisect_right(time_value_list, (timestamp, chr(127)))

        return time_value_list[insertion_index - 1][1] if insertion_index else ''