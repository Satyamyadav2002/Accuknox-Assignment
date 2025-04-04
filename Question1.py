import time
from django.dispatch import Signal, receiver
from django.test import TestCase

# Create a signal
test_signal = Signal()

# Create a receiver that will simulate some work
@receiver(test_signal)
def slow_receiver(sender, **kwargs):
    print("Receiver started")
    time.sleep(2)  # Simulate some work
    print("Receiver finished")

class SignalTest(TestCase):
    def test_signal_execution(self):
        print("Test started")
        start_time = time.time()
        
        # Send the signal
        test_signal.send(sender=None)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"Test finished. Total execution time: {execution_time:.2f} seconds")
        
        # If signals were asynchronous, this would complete almost immediately
        # Since it's synchronous, it will take at least 2 seconds
        self.assertGreaterEqual(execution_time, 2.0) 