from ethereum import Ethereum
from period import Period

POOL_FEE = 0.01  # placeholder


class GPU:
    name: str
    mhs: float
    power: int
    day: Period
    week: Period
    month: Period
    year: Period

    def __init__(self, name: str, mhs: float, power: int, kwh_price_gbp: float):
        self.name = name
        self.mhs = mhs
        self.power = power
        eth = Ethereum.get_instance()
        gpu_ghs = mhs / 1000
        mine_chance = gpu_ghs / eth.net_hash_ghs  # probability to mine next block

        kwh_day = power * 24 / 1000
        power_cost_day = kwh_day * kwh_price_gbp
        blocks_mined_per_month = mine_chance * eth.blocks_per_month

        self.month = Period(blocks_mined_per_month, (power_cost_day * 30), POOL_FEE, 30)
        self.day = Period((blocks_mined_per_month / 30), power_cost_day, POOL_FEE, 1)
        self.week = Period((self.day.blocks_mined * 7), (power_cost_day * 7), POOL_FEE, 7)
        self.year = Period((self.day.blocks_mined * 365), (power_cost_day * 365), POOL_FEE, 365)


if __name__ == '__main__':
    calc = GPU(mhs=100.00, power=125, kwh_price_gbp=0.1437)
    print(f'Monthly revenue = {calc.month.revenue} GBP')
    print(f'Monthly profit = {calc.month.profit} GBP')
    print(f'Monthly pool fee = {calc.month.pool_fee} GBP')
    print(f'Monthly power cost = {calc.month.power_cost} GBP')
