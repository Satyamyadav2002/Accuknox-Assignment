import threading
import time
from django.dispatch import Signal, receiver
from django.core.signals import request_started

# Create a custom signal
my_signal = Signal()

@receiver(my_signal)
def signal_handler(sender, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")
    time.sleep(2)  # Simulate some work
    print("Signal handler completed")

def main():
    print(f"Main thread: {threading.current_thread().name}")
    
    # Send the signal
    print("Sending signal...")
    my_signal.send(sender=None)
    print("Signal sent, continuing main thread...")

if __name__ == "__main__":
    main() 