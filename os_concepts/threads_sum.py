from __future__ import print_function
from threading import Thread
from datetime import datetime


def sum(results, thread_id, SUM_RANGE):
    sum = i = 0
    start = thread_id * SUM_RANGE

    while(i < SUM_RANGE):
        sum += (i + start)
        i += 1
    results[thread_id] = sum


def sum_runner(NO_OF_THREADS, SUM_RANGE):

    results = [None] * NO_OF_THREADS
    threads = [None] * NO_OF_THREADS

    startTime = datetime.now()

    DIVIDED_SUM_RANGE = (SUM_RANGE / NO_OF_THREADS)

    for i in range(len(threads)):
        threads[i] = Thread(target=sum, args=(results, i, DIVIDED_SUM_RANGE))
        threads[i].start()

    for i in range(len(threads)):
        threads[i].join()

    total_sum = 0

    for i in range(len(results)):
        total_sum += results[i]

    print("Time taken to sum numbers = {}".format(datetime.now() - startTime))
    print("total_sum = {}".format(total_sum))


SUM_RANGE = 100000000


# ------- Using 1 thread
NO_OF_THREADS = 1
sum_runner(NO_OF_THREADS, SUM_RANGE)


# ----- using 4 threads
NO_OF_THREADS = 4
sum_runner(NO_OF_THREADS, SUM_RANGE)


