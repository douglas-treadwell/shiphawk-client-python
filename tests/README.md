# Running the tests

Before running the tests set the environment variable SHIPHAWK_SANDBOX_API_TOKEN to
your sandbox API token.  On a Linux or Apple machine you can do this with:

```export SHIPHAWK_SANDBOX_API_TOKEN=your_api_token```

The tests include a workaround for a manual process with setting up sandbox accounts.
A ShipHawk administrator must enable your sandbox account to create shipments.
Otherwise the attempt will fail with a UnprocessableEntityError (422) with an error
message that states:

    "Your account does not have a stripe_customer_id and is unable to book shipments using ShipHawk's tariffs"

Because ShipHawk also provides an API for adding external shipments to their platform,
the tests catch the above error and add an external shipment instead.  That external
shipment can be used by subsequent tests in the same way.
