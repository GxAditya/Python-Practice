#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Learn Python dictionaries — methods, usage, patterns, and key points.

Run this file directly to see printed examples.
Python version: 3.9+ recommended (uses dict union operators | and |=)
"""

from __future__ import annotations
from pprint import pprint
from copy import deepcopy


def print_heading(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def creation_and_basics():
    print_heading("1) Creation and basics")

    # Literal and constructor
    user = {"name": "Asha", "age": 29}  # literal
    coords = dict(x=10, y=20)  # constructor with keyword args
    pairs = dict([("a", 1), ("b", 2)])  # from iterable of pairs

    print("Literal:", user)
    print("Constructor (kwargs):", coords)
    print("From pairs:", pairs)

    # Accessing values
    print("Access with []:", user["name"])  # raises KeyError if missing
    print("Safe access with get():", user.get("city"))  # returns None if missing
    print("get() with default:", user.get("city", "unknown"))

    # Membership and size
    print("'age' in user:", "age" in user)  # membership checks keys
    print("len(user):", len(user))

    # Adding / updating
    user["city"] = "Pune"
    print("After adding city:", user)

    # fromkeys: creates keys with same default value for each key
    zeros = dict.fromkeys(["p", "q", "r"], 0)
    print("fromkeys with 0:", zeros)

    # BEWARE: fromkeys with a mutable default shares the SAME object for all keys
    shared = dict.fromkeys(["k1", "k2"], [])
    shared["k1"].append(1)
    print("fromkeys with [] (shared list!):", shared, "<-- same list referenced")


def iterating_and_views():
    print_heading("2) Iterating and dictionary views")

    d = {"a": 1, "b": 2, "c": 3}

    print("Iterate keys (default):", end=" ")
    for k in d:
        print(k, end=" ")
    print()

    print("Iterate values:", end=" ")
    for v in d.values():
        print(v, end=" ")
    print()

    print("Iterate items (key, value):", end=" ")
    for k, v in d.items():
        print((k, v), end=" ")
    print()

    # Views are dynamic; they reflect updates
    keys_view = d.keys()
    print("Before update, keys view:", list(keys_view))
    d["d"] = 4
    print("After update, keys view:", list(keys_view), "<-- updated automatically")


def modifying_and_merging():
    print_heading("3) Modifying and merging")

    a = {"x": 1, "y": 2}
    b = {"y": 20, "z": 3}

    # update mutates left operand; right overwrites matching keys
    a_copy = a.copy()
    a_copy.update(b)
    print("update() result (mutates):", a_copy, "(original a unchanged?)", a)

    # Union operator (Python 3.9+): does NOT mutate; right side wins on conflicts
    c = a | b
    print("Union | (new dict):", c, "(a unchanged)", a)

    # In-place union (mutates left operand)
    a_union = a.copy()
    a_union |= b
    print("In-place union |=:", a_union)

    # Dict unpacking (also right-wins)
    merged = {**a, **b}
    print("Unpacking merge {**a, **b}:", merged)

    # setdefault: get value if present; if missing, set to default and return it
    groups = {}
    val = groups.setdefault("admins", [])
    val.append("asha")
    print("setdefault to build list:", groups, "(note: creates key if absent)")

    # Be cautious: setdefault with mutable defaults can create and keep an empty container even if unused.


def removing_and_errors():
    print_heading("4) Removing items and handling missing keys")

    d = {"a": 1, "b": 2, "c": 3}

    # del removes a key; raises KeyError if missing
    del d["b"]
    print("After del d['b']:", d)

    # pop returns the removed value; can provide default to avoid KeyError
    removed = d.pop("c")
    print("pop('c') ->", removed, "; dict now:", d)
    missing = d.pop("not_there", "default")
    print("pop('not_there', 'default') ->", missing)

    # popitem removes and returns last inserted (LIFO in 3.7+)
    d["x"] = 10
    d["y"] = 20
    last_key, last_val = d.popitem()
    print("popitem() ->", (last_key, last_val), "; dict now:", d)

    # clear removes all items
    d.clear()
    print("After clear():", d)


def copying_and_shallow_vs_deep():
    print_heading("5) Copying: shallow vs deep")

    nested = {"user": {"name": "Asha", "skills": ["python", "sql"]}}
    alias = nested  # no copy; both names refer to same dict
    shallow = nested.copy()  # shallow copy (one level)
    deep = deepcopy(nested)  # deep copy

    nested["user"]["skills"].append("docker")
    print("Original after mutate nested['user']['skills']:", nested)
    print("Alias sees change (same object):", alias)
    print("Shallow copy ALSO sees inner change:", shallow, "<-- inner objects shared")
    print("Deep copy isolated:", deep)


def sorting_and_order():
    print_heading("6) Ordering and sorting")

    # Python 3.7+ preserves insertion order as an implementation detail (now a language guarantee).
    d = {}
    for k in ["b", "a", "c"]:
        d[k] = ord(k)
    print("Insertion order preserved:", list(d.items()))

    # Sorting produces a new list of tuples (not a dict)
    by_key = sorted(d.items())  # ascending by key
    by_val_desc = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    print("Sorted by key:", by_key)
    print("Sorted by value desc:", by_val_desc)

    # To make a sorted dict (rarely necessary), rebuild:
    sorted_dict = dict(by_key)
    print("Rebuilt sorted dict:", sorted_dict)


def comprehensions_and_transforms():
    print_heading("7) Dict comprehensions and transforms")

    words = ["apple", "banana", "avocado", "blueberry"]
    lengths = {w: len(w) for w in words}
    print("Comprehension (word -> length):", lengths)

    # Filtering and transforming
    a_words = {w: len(w) for w in words if w.startswith("a")}
    print("Filter words starting with 'a':", a_words)

    # Inverting a mapping (beware duplicates!)
    capitals = {"IN": "Delhi", "FR": "Paris", "JP": "Tokyo"}
    inverted = {v: k for k, v in capitals.items()}
    print("Inverted mapping (value -> key):", inverted, "(fails if values not unique)")

    # Build frequency map without imports
    nums = [1, 2, 2, 3, 3, 3]
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    print("Frequency with get():", freq)


def immutability_and_hashability():
    print_heading("8) Keys must be hashable (immutable)")

    d = {}
    d[(1, 2)] = "tuple is ok"  # tuples are hashable if their contents are hashable
    print("Tuple key:", d)

    try:
        d[[1, 2]] = "list is not ok"  # lists are unhashable
    except TypeError as e:
        print("Using list as key raises:", e)

    # Custom objects can be keys if they define __hash__ and __eq__ appropriately.


def safe_modification_during_iteration():
    print_heading("9) Modifying while iterating (do it safely)")

    d = {"a": 1, "b": 2, "c": 3}
    try:
        for k in d:
            if k == "b":
                del d[k]  # RuntimeError: dictionary changed size during iteration
    except RuntimeError as e:
        print("Modifying during iteration raises:", e)

    # Safe patterns:
    d = {"a": 1, "b": 2, "c": 3}
    for k in list(d):  # iterate over a static list of keys
        if k == "b":
            del d[k]
    print("Safe delete during iteration:", d)

    # Or accumulate changes and apply after the loop.


def pretty_print_and_inspection():
    print_heading("10) Pretty printing and inspection helpers")

    profile = {
        "name": "Asha",
        "age": 29,
        "skills": ["python", "sql", "docker"],
        "projects": [{"id": 1, "title": "ETL"}, {"id": 2, "title": "API"}],
    }
    print("Default print:")
    print(profile)
    print("Pretty print with pprint:")
    pprint(profile, width=60, sort_dicts=False)

    # Keys, values, items views:
    print("keys():", list(profile.keys()))
    print("values():", list(profile.values()))
    print("items():", list(profile.items()))


def method_cheat_sheet():
    print_heading("11) Method cheat sheet (with examples)")

    d = {"a": 1, "b": 2}

    print("get(key, default=None):", d.get("c"), d.get("c", 99))
    print("setdefault(key, default):", d.setdefault("c", 3), "; d now:", d)
    print("update([other], **kwargs):", end=" ")
    d.update({"b": 20}, d=4)  # note: 'd' here is a new key 'd'
    print(d)

    print("keys(), values(), items():", list(d.keys()), list(d.values()), list(d.items()))
    print("pop(key[, default]):", d.pop("d", "nope"), "; d now:", d)
    print("popitem():", d.popitem(), "; d now:", d)
    print("copy() (shallow):", d.copy())
    print("clear():", end=" ")
    e = d.copy()
    e.clear()
    print(e)

    print("fromkeys(iterable, value):", dict.fromkeys(["x", "y"], 0))
    print("Union | and |= (3.9+):", {"x": 1} | {"x": 2, "y": 3})


def key_points_to_keep_in_mind():
    print_heading("12) Key points to keep in mind")

    points = [
        "Keys must be hashable (immutable); typical: str, int, float, tuple of immutables.",
        "Keys are unique; assigning an existing key overwrites its value.",
        "Average O(1) operations for get/set/in, but avoid mutating during iteration.",
        "Views (keys(), values(), items()) are dynamic; cast to list for a snapshot.",
        "fromkeys with a mutable default shares the SAME object across keys.",
        "copy() is shallow; inner mutable objects are shared. Use deepcopy for isolation.",
        "Use get() to avoid KeyError; provide a default where appropriate.",
        "setdefault() creates the key if missing; be mindful of side effects with mutable defaults.",
        "Right-hand side wins in merges: update(), |, and {**a, **b} all prefer the right.",
        "Insertion order is preserved (Python 3.7+); don't rely on order for algorithmic logic unless intended.",
        "Prefer membership tests ('in') on keys; 'x in d' checks keys, not values.",
        "popitem() removes the last inserted item (LIFO) in 3.7+.",
    ]
    for i, p in enumerate(points, 1):
        print(f"{i}. {p}")


def practical_patterns():
    print_heading("13) Practical patterns")

    # 1) Grouping items by a key
    people = [
        {"name": "Asha", "team": "ML"},
        {"name": "Rahul", "team": "Platform"},
        {"name": "Meera", "team": "ML"},
    ]
    grouped = {}
    for person in people:
        grouped.setdefault(person["team"], []).append(person["name"])
    print("Group names by team:", grouped)

    # 2) Renaming keys in a dict
    row = {"first_name": "Asha", "last_name": "Iyer", "age": 29}
    rename_map = {"first_name": "firstName", "last_name": "lastName"}
    renamed = {rename_map.get(k, k): v for k, v in row.items()}
    print("Renamed keys:", renamed)

    # 3) Safe nested access (without external libs)
    user = {"profile": {"location": {"city": "Pune"}}}
    city = user.get("profile", {}).get("location", {}).get("city")
    print("Safe nested get:", city)

    # 4) Deduplicate while preserving last occurrence (right-wins merge trick)
    items = [("a", 1), ("b", 2), ("a", 3)]
    dedup = dict(items)  # later 'a' overwrites earlier 'a'
    print("Deduplicate (last wins):", dedup)

    # 5) Counting with a single pass
    text = "mississippi"
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    print("Counts:", counts)


def mini_exercises():
    print_heading("14) Mini exercises (try mentally before viewing output)")

    # 1) Merge two dicts; right should overwrite; verify
    a = {"id": 1, "role": "user"}
    b = {"role": "admin", "active": True}
    merged = a | b
    print("Exercise 1 - merged:", merged)  # expect role=admin

    # 2) Remove all items with falsy values
    data = {"a": 0, "b": "", "c": None, "d": 42}
    filtered = {k: v for k, v in data.items() if v}
    print("Exercise 2 - filtered:", filtered)  # expect {'d': 42}

    # 3) Invert mapping with duplicates by collecting into lists
    colors = {"apple": "red", "strawberry": "red", "banana": "yellow"}
    inverted = {}
    for k, v in colors.items():
        inverted.setdefault(v, []).append(k)
    print("Exercise 3 - invert with lists:", inverted)


def main():
    creation_and_basics()
    iterating_and_views()
    modifying_and_merging()
    removing_and_errors()
    copying_and_shallow_vs_deep()
    sorting_and_order()
    comprehensions_and_transforms()
    immutability_and_hashability()
    safe_modification_during_iteration()
    pretty_print_and_inspection()
    method_cheat_sheet()
    key_points_to_keep_in_mind()
    practical_patterns()
    mini_exercises()


if __name__ == "__main__":
    main()