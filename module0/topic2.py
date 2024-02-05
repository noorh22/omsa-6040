# NOTEBOOK 2 - ASSOCIATION RULE MINING
from collections import defaultdict
from itertools import combinations  # Hint!


def normalize_string(s):
    assert type(s) is str
    return ''.join([c for c in s.lower() if c.isalpha() or c.isspace()])


def get_normalized_words(s):
    assert type(s) is str
    return normalize_string(s).split()


def make_itemsets(words):
    return [set(w) for w in words]


def update_pair_counts(pair_counts, itemset):
    assert type(pair_counts) is defaultdict
    for a, b in combinations(itemset, 2):
        pair_counts[(a, b)] += 1
        pair_counts[(b, a)] += 1


def update_item_counts(item_counts, itemset):
    for a in itemset:
        item_counts[a] += 1


def filter_rules_by_conf(pair_counts, item_counts, threshold):
    rules = {}  # (item_a, item_b) -> conf (item_a => item_b)
    for (a, b) in pair_counts:
        assert a in item_counts
        conf_ab = pair_counts[(a, b)] / item_counts[a]
        if conf_ab >= threshold:
            rules[(a, b)] = conf_ab
    return rules


def find_assoc_rules(receipts, threshold):
    pair_counts = defaultdict(int)
    item_counts = defaultdict(int)
    for itemset in receipts:
        update_pair_counts(pair_counts, itemset)
        update_item_counts(item_counts, itemset)
    rules = filter_rules_by_conf(pair_counts, item_counts, threshold)
    return rules


def intersect_keys(d1, d2):
    assert type(d1) is dict or type(d1) is defaultdict
    assert type(d2) is dict or type(d2) is defaultdict
    return {key: d1[key] for key in d1 if key in d2}


# Exercise 11 - Actual Task
# Confidence threshold
THRESHOLD = 0.5

# Only consider rules for items appearing at least `MIN_COUNT` times.
MIN_COUNT = 10


def filter_rules_by_conf_new(pair_counts, item_counts, threshold, min_count):
    rules = {}  # (item_a, item_b) -> conf (item_a => item_b)
    for (a, b) in pair_counts:
        assert a in item_counts
        conf_ab = pair_counts[(a, b)] / item_counts[a]
        if item_counts[a] >= min_count and conf_ab >= threshold:
            rules[(a, b)] = conf_ab
    return rules


def find_assoc_rules_new(receipts, threshold, min_count):
    pair_counts = defaultdict(int)
    item_counts = defaultdict(int)
    for itemset in receipts:
        update_pair_counts(pair_counts, itemset)
        update_item_counts(item_counts, itemset)
    rules = filter_rules_by_conf_new(pair_counts, item_counts, threshold, min_count)
    return rules
