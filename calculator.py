
import ethereum as eth
from period import Period

class CostCalculator:
    day: Period
    week: Period
    month: Period
    year: Period

    def __init__(self, gpu_mhs: float, power: int, kwh_price: float):
        gpu_ghs = gpu_mhs / 1000
        mine_chance = gpu_ghs / eth.ETH_NET_HASH_GHS  # probability to mine next block
        seconds_in_month = 2628288.0  # number of seconds in an average month
        blocks_per_month = seconds_in_month / eth.ETH_BLOCK_TIME  # total blocks mined each month
        blocked_mined_per_month = mine_chance * blocks_per_month
        monthly_revenue_eth = eth.ETH_BLOCK_REWARD_GBP * blocked_mined_per_month

        kwh_day = power * 24 / 1000
        power_cost_day = kwh_day * kwh_price

        self.month = Period(monthly_revenue_eth, (power_cost_day * 30), eth.POOL_FEE, 30)
        self.day = Period((monthly_revenue_eth / 30), power_cost_day, eth.POOL_FEE, 1)
        self.week = Period((self.day.income * 7), (power_cost_day * 7), eth.POOL_FEE, 7)
        self.year = Period((self.day.income * 365), (power_cost_day * 365), eth.POOL_FEE, 365)


if __name__ == '__main__':
    calc = CostCalculator(gpu_mhs=100.00, power=125, kwh_price=0.1437)
    print(calc.month)
