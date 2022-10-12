import unittest
import producer_consumer
from queue import Queue

class TestProcess(unittest.TestCase):
	def test_log_display(self):
		with self.assertRaises(Exception):
			'''
			The below statement will result in a success of the unittest as an exception will be raised,
			because a parameter is required for the log_display function
			'''
			producer_consumer.log_display()

			'''
			The below statement will result in a failure of the unittest as no exception is raised, i.e., the parameters work 
			on the function. Uncomment below and comment above to try.
			'''
			#producer_consumer.log_display("Test Message")
	
	def test_producer(self):
		with self.assertRaises(Exception):
			
			'''
			The below statement will results in a success of the unittest as an exception will be raised, because the parameters are wrong.
			The requests.get part in producer cannot accept a max_size greater than the length of the URL list, and the URL list must contain
			valid URL strings, not numbers
			'''
			producer_consumer.producer(Queue(),Queue(),10,[2])

			'''
			The below statement will result in a failure of the unittest as no exception is raised, i.e., the parameters work 
			on the function. Uncomment below and comment above to try.
			'''
			#producer_consumer.producer(Queue(),Queue(),1,['https://www.espncricinfo.com'])			

	def test_consumer(self):
		with self.assertRaises(Exception):

			'''
			The below statement will result in a success of the unittest as an exception will be raised, i.e., 
			the paramters do not work on the function. The queue elements need to be valid 
			strings (HTML data and bool respectively)
			'''
			producer_consumer.consumer(Queue().put(5),Queue().put(10))


if __name__=='__main__':
	unittest.main()
 
