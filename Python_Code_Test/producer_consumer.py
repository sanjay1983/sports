import threading
from threading import Thread
import multiprocessing
from queue import Queue
import time
from bs4 import BeautifulSoup
import requests


def msg_display(message):
    thread = threading.current_thread().name
    process = multiprocessing.current_process().name
    print('-------------')
    print("Thread: ",thread)
    print("Process: ",process)
    print("Message: ", message)
    print('-------------')


def producer(queue,finished,urls,max_size):
    finished.put(False)
    for i in range(len(urls)):

        try:
            # Extracting markups from URL
            print('Current Queue Size before Producing: ',queue.qsize())
            if (queue.qsize()<=max_size):
                reqs = requests.get(urls[i])
                queue.put(reqs)
                msg_display(f'Producing and extracting URL {i}: {urls[i]}')
            else:
                print("QUEUE OVERLOAD")
                # Trimming oldest queue entry if queue size is going over capacity.
                queue.get()
                reqs = requests.get(urls[i])
                queue.put(reqs)
                msg_display(f'Producing and extracting URL {i}: {urls[i]}')

        except:
            # The URLs are incorrectly formatted as a result of which, the HTML configuration cannot be extracted.
            error_flag = 1
            

    finished.put(True)
    msg_display('Finished')

def consumer(work,finished):
    count = 0
    while True:
        # Introducing a time delay so that the consumer isn't called first with producer not having added anything to the queue
        time.sleep(0.3) 
        if not work.empty():
            print("Current Queue Size before Consuming: ",work.qsize())
            all_tags = work.get()
            hyperlinks=[]
            # Parsing HTML and extracting hyperlinks into a list
            soup = BeautifulSoup(all_tags.text, 'html.parser')
            try: 
                for link in soup.find_all('a'):
                    
                    if 'https' in link.get('href'):
                        hyperlinks.append(link.get('href'))

            except:
                # There are either no hyperlinks in the extracted html or there is missing information
                error_flag = 1
            
            # Only first 5 hyperlinks for a URL's HTML config are displayed for ease of reading in command line    
            msg_display(f'Consuming and extracting hyperlinks from URL {count}:\n {hyperlinks[:5]}\n')
            
            # All the hyperlinks found in a URL's HTML config are written to a file
            filename = 'hyperlink_dump'+str(count)+'.txt'
            with open(filename, "w+") as my_file:
                for hyperlink in hyperlinks:
                    my_file.write(f'{hyperlink}\n')

            count+=1
        else:

            q = finished.get()
            if q == True:
                break
    msg_display('Finished')


def main():
    
    # Add desired URLs to this list
    urls = ['https://txodds.net',
            'https://www.espncricinfo.com',
            'https://www.premierleague.com',
            'https://www.youtube.com',
            'https://www.bbc.co.uk/sport/tennis',
            'https://www.formula1.com',
            'https://www.theguardian.com/uk',
            'https://www.wsj.com']
    max_size = 3
    jobs = Queue(maxsize=max_size)
    finished = Queue()
    prod = Thread(target=producer,args=[jobs,finished,urls,max_size],daemon=True)
    cons = Thread(target=consumer,args=[jobs,finished],daemon=True)

    prod.start()
    cons.start()

    prod.join()
    msg_display('Producer has completed production')

    cons.join()
    msg_display('Consumer has completed consumption')
    msg_display('Producer/Consumer web link extractor demonstration has been completed')
    print("END OF DEMO")

if __name__ == "__main__":
    main()
