# Python Code Test

## Instructions

1. First clone the repository and navigate to the folder Python_Code_Test in the command line.
2. Run 'pip install -r requirements.txt' in the command line.
3. After this, run 'python producer_consumer.py' which reads a list of URLs, extracts the HTML config and then the associated hyperlinks using a 
queue-based producer-consumer setup. The output on the command line shows the entire process where the producer and consumer run in parallel. 
4. Run 'python test_producer_consumer.py' on the command line for a few unittest results.

## Discussions and thought process

1. A list of 8 URL's have been defined in a list in the main() function. The maximum queue size has been set at 3. These are customizable.
2. The URLs are received by the producer function, which then extracts the respective HTML configurations for each URL and adds these to 
a queue. Simultaneously, the consumer function consumes these queue values and extracts the hyperlinks present in each URL's HTML representation.
It prints 5 hyperlinks for each URL on the command line for readability purposes, and outputs all the hyperlinks to individual text files which are
created in the same directory as the producer_consumer.py file, after running the latter.
3. Threading and multiprocessing concepts have been used to ensure concurrent execution of both the producer and the consumer. A producer is able
to directly add a new item to the queue as long as the queue_size before adding does not exceed the maximum size. If this is the case, then a snippet
has been written to remove an element from the queue. By default, the removed element will be the oldest element as this is a FIFO queue representation.
4. The Queue() class by default ensures internal locking which means that 2 threads do not interfere while using the 'get' function. This is important as
in case the queue size balloons, the element that is being trimmed out by one thread must not be simultaneously accessed by the other thread. As it happens,
to avoid this kind of a race condition, the Queue() class inherently implements blocking new entries (get(block=True)) until a free slot becomes available.
Since this is already implemented, it means that the queue is never at risk of overflowing since the queue will wait. Old elements won't need to
be removed. However, this could cost crucial seconds in the real-world extraction of data.
5. To overcome this, we can override this block and set get((block=False)) which means that we are free to remove the oldest elements of an overloaded
queue as discussed in step 3. Again, we are not at risk of thread interference while removing the element because internalthread locking is already 
implemented.
6. The final point worth mentioning is the risk of a deadlock, a condition in which 2 threads are blocked forever because they are waiting for each other.
I believe I encountered this once while doing the task. Other runs were smooth. If a deadlock does happen, then it's best to kill the execution and re-run,
although in the longer run, it's important to try and prevent this by setting optimal timeout and wait values, which unfortunately is a threat to
achieving low latency. It's important to find the balance between the two.

## Unit testing and robustness

1. Some unittests have been implemented in test_producer_consumer.py, wherein correct and incorrect inputs have been given to verify successes and
failures. Some try-except blocks have also been included in the producer_consumer.py to catch issues like incorrectly formatted URLs or absence 
of hyperlinks. Some other minor, obvious robustness protocols like ensuring max_size is always a positive integer etc. have not been looked at. 
