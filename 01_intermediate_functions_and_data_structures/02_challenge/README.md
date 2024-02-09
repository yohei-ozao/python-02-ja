# Challenge 2
You have a list of products, each represented by a dictionary containing the product's name, category, and price. Your task is to complete the `apply_discount` function. You must use list comprehensions and lambdas to filter products based on a minimum price threshold and apply a discount to the filtered products. The output should be a list of product names and their discounted prices.

- Use a list comprehension to filter the products above or equal to the minimum price threshold.
- Apply a discount to the filtered products using a lambda function within the list comprehension.
- The output must be a list of tuples, each containing the product's name and its discounted price.

## Example inputs and outputs
Input:
```python
[
    {"name": "Laptop", "category": "Electronics", "price": 1200},
    {"name": "Bread", "category": "Food", "price": 2},
    {"name": "Jacket", "category": "Apparel", "price": 100}
]
```

- Minimum Price Threshold: 50
- Discount Rate: 10

Output:
```python
[("Laptop", 1080.0), ("Jacket", 90.0)]
```

Input:
```python
[
    {"name": "Smartphone", "category": "Electronics", "price": 800},
    {"name": "Sneakers", "category": "Footwear", "price": 120},
    {"name": "Coffee", "category": "Beverage", "price": 5}
]
```

- Minimum Price Threshold: 100
- Discount Rate: 15

Output:
```python
[("Smartphone", 680.0), ("Sneakers", 102.0)]
```