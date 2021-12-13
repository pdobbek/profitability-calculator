ETH_PRICE = 3131.27
ETH_DIFFICULTY = 11.6354
ETH_BLOCK_TIME = 13.15
ETH_NET_HASH_THS = 858.4912
ETH_NET_HASH_GHS = ETH_NET_HASH_THS * 1000
ETH_BLOCK_REWARD = 2.1348
ETH_BLOCK_REWARD_GBP = ETH_BLOCK_REWARD * ETH_PRICE

POOL_FEE = 0.01
KWH_PRICE = 0.1437

class CostCalculator:
    day: float
    week: float
    month: float
    year: float

    def __init__(self, gpu_mhs: float, power: int):
        gpu_ghs = gpu_mhs / 1000
        mine_chance = gpu_ghs / ETH_NET_HASH_GHS  # probability to mine next block
        seconds_in_month = 2628288.0  # number of seconds in an average month
        blocks_per_month = seconds_in_month / ETH_BLOCK_TIME  # total blocks mined each month
        blocked_mined_per_month = mine_chance * blocks_per_month
        monthly_revenue_eth = ETH_BLOCK_REWARD_GBP * blocked_mined_per_month

        kwh_day = power * 24 / 1000
        power_cost_day = kwh_day * KWH_PRICE

        self.month = monthly_revenue_eth - (power_cost_day * 30)
        self.day = (self.month / 30) - power_cost_day
        self.week = (self.day * 7) - (power_cost_day * 7)
        self.year = (self.day * 365) - (power_cost_day * 365)

        # apply pool fee
        pool_fee_multiplier = 1.00 - POOL_FEE
        self.day = self.day * pool_fee_multiplier
        self.week = self.week * pool_fee_multiplier
        self.month = self.month * pool_fee_multiplier
        self.year = self.year * pool_fee_multiplier


if __name__ == '__main__':
    calc = CostCalculator(gpu_mhs=100.00, power=125)
    print(calc.month)
