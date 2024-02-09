# Challenge 1
You have a text document containing various data points mixed with regular text. These data points are in the format DataPointName:Value. For example, Age:25, Height:180cm, Weight:70kg. The data points are scattered throughout the document amidst other unnecessary text.

## Part 1
Your task is to complete the `extract_data` function. You must use a regex pattern to extract all data points from the text.

- The regex pattern must identify the data point name followed by a colon and its value.
- Values can be numbers, strings, or alphanumeric combinations.

### Example inputs and outputs
Input:
```
"The subject has Age:25 and Height:180cm. Other details are not relevant. Weight:70kg was noted."
```

Output:
```python
['Age:25', 'Height:180cm', 'Weight:70kg']
```

## Part 2
Your task is to complete the `better_extract_data` function.

- The output must be a list of tuples, each containing the data point name and value as separate elements.

> Hint: You must make use of **capture groups**. Look this up on your own.

### Example inputs and outputs
Input:
```
"The subject has Age:25 and Height:180cm. Other details are not relevant. Weight:70kg was noted."
```

Output:
```python
[("Age", "25"), ("Height", "180cm"), ("Weight", "70kg")]
```