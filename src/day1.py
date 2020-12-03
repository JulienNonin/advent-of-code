# %%
import bisect

# %% Part 1
def find_two_entries_that_sum_to_N(entries, N=2020):
    seen_entries = set()
    for entry in entries:
        if N - entry in seen_entries:
            return entry * (N - entry)
        else:
            seen_entries.add(entry)

# %% Part 2
def find_three_entries_that_sum_to_N(entries, N=2020):
    seen_entries = []  # kept sorted using bisect
    sum_two_entries = {}  # a + b -> a * b  (constraint: a + b < N)

    for entry in entries:
        if N - entry in sum_two_entries:
            return entry * sum_two_entries[N - entry]
        else:
            last_idx = bisect.bisect(seen_entries, N - entry)  # after this index, entry + other > N
            for other in seen_entries[:last_idx]:
                assert other + entry <= N
                sum_two_entries[other + entry] = other * entry
            bisect.insort(seen_entries, entry)

# %%
if __name__ == "__main__":
    from os.path import dirname, join, realpath
    import numpy as np
    folder = join(dirname(dirname(realpath(__file__))), "data")
    expenses = np.loadtxt(f"{folder}/day1.txt", dtype=int)

    print("Part 1 —", find_two_entries_that_sum_to_N(expenses))
    print("Part 2 —", find_three_entries_that_sum_to_N(expenses))

# %%
