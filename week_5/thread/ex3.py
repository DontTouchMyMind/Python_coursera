# Пул потоков, concurrent.futures.Future

from concurrent.futures import ThreadPoolExecutor, as_completed


def f(a):
    return a * a


# .shutdown() in exit
with ThreadPoolExecutor(max_workers=3) as pool:
    results = [pool.submit(f, i) for i in range(10)]
    # submit создает объект класса concurrent.futures.Future

    for future in as_completed(results):
        print(future.result())