# Running the tests

Before running the tests set the environment variable SHIPHAWK_SANDBOX_API_TOKEN to
your sandbox API token.  On a Linux or Apple machine you can do this with:

```export SHIPHAWK_SANDBOX_API_TOKEN=your_api_token```

In order to run the tests you will need to add a payment method to your
ShipHawk sandbox account.  This can be done by:

1. Logging in to the sandbox account at https://sandbox.shiphawk.com/login/
2. Entering a Stripe test credit card at https://sandbox.shiphawk.com/billing/
    - For example, 4242424242424242 along with any other valid values

Creating a shipment will fail if Stripe hasn't been configured for the ShipHawk account.
The error will state:

    "Your account does not have a stripe_customer_id and is unable to book shipments using ShipHawk's tariffs"
