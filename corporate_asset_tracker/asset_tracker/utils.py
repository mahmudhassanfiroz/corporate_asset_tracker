
from django.core.validators import RegexValidator
from .models import Subscriber


def process_payment(subscriber):
    # Placeholder for payment processing logic
    # You can simulate payment processing here
    # For example, you might return True for successful payment and False for failed payment
    return True

def subscribe_company(company, subscriber):
    # Placeholder for subscription logic
    # You can simulate subscription logic here
    # For example, you might return True for successful subscription and False for failed subscription
    return True

def create_subscriber(company, first_name, last_name, email, phone_number, address):    
    # Create a new subscriber
    subscriber = Subscriber.objects.create(
        company=company,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        address=address
    )
    
    # Process payment and subscription
    if process_payment(subscriber) and subscribe_company(company, subscriber):
        return subscriber
    else:
        # Delete the subscriber if payment or subscription fails
        subscriber.delete()
        return None
