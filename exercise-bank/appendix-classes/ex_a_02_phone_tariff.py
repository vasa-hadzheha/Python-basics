"""Exercise A.2 - PhoneTariff: days remaining, call cost, running total.
Original: Lab 10, Task 2.

THE BUG IN THE ORIGINAL - and this is the one worth studying:

    class Telephone_tariff:
        sum = 0                      # <-- on the CLASS, not the instance
        ...
        def price_of_call(self):
            self.sum += price_of_call

"self.sum += x" reads the class attribute, adds, and then ASSIGNS, which
creates an instance attribute. So it happens to work - but:
  * two tariffs both see the class-level 0 before either has paid
  * the intent is invisible to a reader
  * had "sum" been a list, every instance would have shared it (see A.1)

Working by accident is not working. All per-instance state belongs in
__init__.

The original also calls input() inside its methods, so you cannot test it
and cannot run it from a scheduled job.
"""

import math


class PhoneTariff:
    """A phone tariff with a validity window and a per-minute price."""

    # A genuine shared constant is fine in the class body: it is immutable
    # and it IS the same for every instance.
    DAYS_IN_MONTH = 31

    def __init__(self, name, start_day, end_day, monthly_fee, price_per_minute):
        if price_per_minute < 0:
            raise ValueError("price per minute cannot be negative")
        self.name = name
        self.start_day = start_day
        self.end_day = end_day
        self.monthly_fee = monthly_fee
        self.price_per_minute = price_per_minute
        self.total_spent = 0.0  # <-- per-instance state, created HERE
        self.call_log = []  # a list, so this MUST be per-instance

    def days_remaining(self, days_used):
        """Days left before the tariff expires. Negative if it has expired."""
        return self.end_day - ((self.start_day + days_used) % self.DAYS_IN_MONTH)

    def describe_remaining(self, days_used):
        remaining = self.days_remaining(days_used)
        if remaining > 0:
            return f"{remaining} day(s) until the tariff expires"
        if remaining == 0:
            return "the tariff expires today"
        return f"the tariff expired {int(math.fabs(remaining))} day(s) ago"

    def make_call(self, minutes):
        """Record a call. Returns its cost."""
        if minutes <= 0:
            raise ValueError("call length must be positive")
        cost = minutes * self.price_per_minute
        self.total_spent += cost
        self.call_log.append({"minutes": minutes, "cost": cost})
        return cost

    def summary(self):
        """A dict, so the caller can print it, log it or store it."""
        return {
            "name": self.name,
            "calls": len(self.call_log),
            "minutes": sum(c["minutes"] for c in self.call_log),
            "spent": round(self.total_spent, 2),
            "with_fee": round(self.total_spent + self.monthly_fee, 2),
        }

    def __str__(self):
        return f"{self.name} ({self.price_per_minute:.2f}/min, fee {self.monthly_fee:.2f})"


if __name__ == "__main__":
    tariff = PhoneTariff("Kyivstar", start_day=23, end_day=15,
                         monthly_fee=75.0, price_per_minute=2.50)
    print(tariff)
    print(tariff.describe_remaining(days_used=5))
    print(tariff.describe_remaining(days_used=20))

    for minutes in (3, 12, 1):
        print(f"  call of {minutes:>2} min costs {tariff.make_call(minutes):>7.2f}")

    print("\nSummary:")
    for key, value in tariff.summary().items():
        print(f"  {key:<10}{value}")

    # --- proof that two tariffs do not share state -------------------
    print("\n" + "=" * 58)
    print("  TWO TARIFFS KEEP SEPARATE TOTALS")
    print("=" * 58)
    a = PhoneTariff("A", 1, 30, 10.0, 1.00)
    b = PhoneTariff("B", 1, 30, 10.0, 2.00)
    a.make_call(10)
    print(f"  a.total_spent = {a.total_spent:.2f}")
    print(f"  b.total_spent = {b.total_spent:.2f}   <- unaffected by a")
    assert a.total_spent == 10.0
    assert b.total_spent == 0.0, "instances must not share state"
    assert a.call_log is not b.call_log, "the list must be per-instance"

    try:
        a.make_call(0)
        raise AssertionError("a zero-length call should have raised")
    except ValueError:
        pass
    print("\nAll tests passed.")
