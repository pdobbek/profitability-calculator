class Period:
    """
    This class contains information regarding income and expenditure during a certain time period.
    """

    duration: int  # total duration of the period in days.
    expenditure_total: float  # total expenditure for this period (GBP).
    income: float  # total income for this period (GBP).
    pool_fee_cash: float  # GBP
    pool_fee_modifier: float  # pool_fee_modifier = 1.0 - pool_fee_percent
    pool_fee_percent: float
    power_cost: float  # cost of electricity for this period.

    def __init__(self, income: float, power_cost: float, pool_fee_percent: float, duration: float):
        self.income = income
        self.duration = duration
        self.pool_fee_percent = pool_fee_percent
        self.pool_fee_modifier = 1.0 - pool_fee_percent
        self.pool_fee_cash = income * pool_fee_percent
        self.power_cost = power_cost
        self.expenditure_total = power_cost + self.pool_fee_cash
