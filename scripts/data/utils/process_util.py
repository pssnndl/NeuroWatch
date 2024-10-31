# coding: utf-8

from multiprocessing import Pool
from tqdm import tqdm

# Modify the call in run_multi_process
def run_multi_process(f, l: list, second_arg, n_processes=40):
    n_processes = min(n_processes, len(l))
    print(n_processes)

    results = []
    pool = Pool(processes=n_processes)
    func_args = [(item, second_arg) for item in l]  # Pair each element with the second_arg
    for r in tqdm(pool.imap_unordered(f, func_args), total=len(l), ncols=75):
        results.append(r)

    pool.close()
    pool.join()

    return results