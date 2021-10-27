import time
import matplotlib.pyplot as plt

max_nested_loops = 20
loop_limit = 2


def num_nested_loops(num_loops, loop_iter):
    if num_loops >= 1:
        for i in range(1, loop_iter + 1, 1):
            # print(x, end=": ")
            num_nested_loops(num_loops - 1, loop_iter)
    else:
        # print("Hello")
        pass


times_list = []
global_start = time.time()
for i in range(1, max_nested_loops + 1):
    start = time.time()
    num_nested_loops(i, loop_limit)
    end = time.time()
    times_list.append(end - start)
global_end = time.time()
print("Total Duration:", global_end - global_start)

x = range(1, len(times_list) + 1)
plt.xlabel("Number of nested loops")
plt.ylabel("Number of seconds")
plt.plot(x, times_list)
plt.show()
