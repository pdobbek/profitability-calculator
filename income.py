import ethereum as eth


class Income:
    day: float
    week: float
    month: float
    year: float

    def __init__(self, gpu_mhs):
        gpu_ghs = gpu_mhs / 1000
        mine_chance = gpu_ghs / eth.ETH_NET_HASH_GHS  # probability to mine next block
        blocked_mined_per_month = mine_chance * eth.BLOCKS_PER_MONTH
        monthly_revenue_eth = eth.ETH_BLOCK_REWARD_GBP * blocked_mined_per_month

        self.month = monthly_revenue_eth
        self.day = (self.month / 30)
        self.week = (self.day * 7)
        self.year = (self.day * 365)
