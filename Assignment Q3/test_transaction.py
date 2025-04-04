import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')
django.setup()

from django.db import transaction
from test_app.models import TestModel

def test_signal_transaction():
    try:
        # Create an instance within a transaction
        with transaction.atomic():
            instance = TestModel.objects.create(name="Test")
            print("Instance created successfully")
    except Exception as e:
        print(f"Exception caught: {e}")
    
    # Check if the instance was actually created
    exists = TestModel.objects.filter(name="Test").exists()
    print(f"Instance exists in database: {exists}")

if __name__ == "__main__":
    test_signal_transaction() 