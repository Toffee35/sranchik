from typing import List


class BotSettings:
    channels: List[int]
    admins: List[int]

    def __init__(self, channels: List[int], admins: List[int]):
        self.channels = channels
        self.admins = admins
