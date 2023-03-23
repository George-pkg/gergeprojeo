import tqdm, time
for e in tqdm.tqdm_ex([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    time.sleep(0.5)  # suppose we are doing something with the elements