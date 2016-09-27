# Examples

## Client Initialization

```python
    import shiphawk
    
    shiphawk = shiphawk.Client(api_token='api_token')
```

## Products

### Creating a product

```python
    shiphawk.products.create(product)
```

Expects: [product object](http://docs.shiphawk.com/docs/sku-object-1) without id

Returns: [product object](http://docs.shiphawk.com/docs/sku-object-1) with id


### Getting all products

```python
    shiphawk.products.get()
```

Returns: a list of [product objects](http://docs.shiphawk.com/docs/sku-object-1) with ids

### Getting one product

```python
    shiphawk.products.get(345)
```

Returns: [product object](http://docs.shiphawk.com/docs/sku-object-1) with id

### Deleting a product

```python
    shiphawk.products.delete(345)
```

Expects: product id (number or string)

Returns: None

### Deleting multiple products

```python
    shiphawk.products.delete([345, 346])
```

Expects: list of product ids (numbers or strings)

Returns: None

## Rates

### Requesting a rate quote

```python
    shiphawk.rates.request(request)
```

Expects: [request object](http://docs.shiphawk.com/docs/rates-request-object)

Returns: a list of [rate objects](http://docs.shiphawk.com/docs/rate-object)

To accept a rate and create a shipment, see [shipments.create](#creating-a-shipment).

## Shipments

### Creating a shipment

```python
    shiphawk.shipments.create(rate_id, origin_address, destination_address)
```

Expects: rate_id (string), origin_address ([address](http://docs.shiphawk.com/docs/addresses])), destination_address ([address](http://docs.shiphawk.com/docs/addresses))

Returns: [shipment object](http://docs.shiphawk.com/docs/shipmentproposed-object)

### Cancelling a shipment

```python
    shiphawk.shipments.cancel(shipment_id)
```

Expects: shipment_id

Returns: [shipment object](http://docs.shiphawk.com/docs/shipmentproposed-object)

### Tracking a shipment

```python
    tracking_info = shiphawk.shipments.track(shipment_id)
```

Expects: shipment_id

Returns: [tracking object](http://docs.shiphawk.com/docs/tracking-object)
