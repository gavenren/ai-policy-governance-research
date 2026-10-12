"""Conditional receipt bounds; all central arithmetic uses exact fractions."""
from fractions import Fraction as F


def validate(s, members, cap):
    if not s or any(x < 0 for x in s) or sum(s) != 1:
        raise ValueError("sales must be a nonnegative simplex vector")
    if cap < 1 or len(set(members)) != len(members):
        raise ValueError("cap must be at least one; members must be unique")
    if any(i < 0 or i >= len(s) for i in members):
        raise ValueError("invalid member index")


def receipts(s, members, cap):
    validate(s, members, cap)
    mass = sum((s[i] for i in members), F(0))
    multiplier = min(cap, 1 / mass) if mass else F(0)
    return tuple(s[i] * multiplier if i in members else F(0)
                 for i in range(len(s)))


def bounds(s, members, cap):
    validate(s, members, cap)
    mass = sum((s[i] for i in members), F(0))
    holdout = 1 - mass
    lower = tuple(s[i] if i in members else F(0) for i in range(len(s)))
    upper = tuple(min(cap * s[i], s[i] + holdout) if i in members else F(0)
                  for i in range(len(s)))
    return mass, min(F(1), cap * mass), lower, upper


def destinations(s):
    """A common population attaining every club's total lower bound."""
    validate(s, (), F(1))
    return [(x, tuple(F(int(i == j)) for j in range(len(s))))
            for i, x in enumerate(s) if x]


def witness(s, members, cap, target):
    """Construct a population for one feasible full member receipt vector."""
    validate(s, members, cap)
    if len(target) != len(s) or sum(target) > 1:
        raise ValueError("infeasible target")
    for i in range(len(s)):
        if i in members:
            if not s[i] <= target[i] <= cap * s[i]:
                raise ValueError("target outside member constraint")
        elif target[i] != 0:
            raise ValueError("holdouts have no receipts")
    h = 1 - sum(s[i] for i in members)
    if not h:
        return [(F(1), tuple(s))]
    holdout = tuple(s[j] / h if j not in members else F(0)
                    for j in range(len(s)))
    firms = []
    for i in members:
        if not target[i]:
            continue
        own = s[i] / target[i]
        profile = tuple(own if j == i else (1 - own) * holdout[j]
                        for j in range(len(s)))
        firms.append((target[i], profile))
    if sum(target) < 1:
        firms.append((1 - sum(target), holdout))
    return firms


def evaluate(population, members, cap):
    if not population or any(w < 0 for w, _ in population):
        raise ValueError("invalid firm weights")
    if sum(w for w, _ in population) != 1:
        raise ValueError("firm weights must sum to one")
    n = len(population[0][1])
    mean, take = [F(0)] * n, [F(0)] * n
    for weight, profile in population:
        if len(profile) != n:
            raise ValueError("inconsistent dimensions")
        amounts = receipts(profile, members, cap)
        if sum(amounts) > 1:
            raise AssertionError("firm overcharged")
        for i in range(n):
            mean[i] += weight * profile[i]
            take[i] += weight * amounts[i]
    return tuple(mean), tuple(take)


def ratio_bounds(revenue_mean, lower, upper):
    """Additional positive-revenue, bounded value/revenue-ratio assumptions."""
    if not 0 <= revenue_mean <= 1 or not 0 < lower <= upper:
        raise ValueError("invalid revenue share or ratio bounds")
    m = revenue_mean
    return (lower * m / (lower * m + upper * (1 - m)),
            upper * m / (upper * m + lower * (1 - m)))
