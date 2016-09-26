# Examples

## Client Initialization

```python
    import shiphawk
    
    client = shiphawk.Client(api_token='api_token')
```

## Getting all or one product

### Getting all products

```python
    import shiphawk

    shiphawk = shiphawk.Client(api_token='api_token')
    shiphawk.products.get()
```

### Getting one product

```python
    import shiphawk

    shiphawk = shiphawk.Client(api_token='api_token')
    shiphawk.products.get(345)

```
