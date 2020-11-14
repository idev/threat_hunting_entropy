# threat_hunting_entropy
Python code mirror for various entropy calculation.
Original Code source and description on the great blog post of Red Canary https://redcanary.com/blog/threat-hunting-entropy/

The various algorithms are stored in a class dictionary so all supported algorithms can be iterated through.
See the calculate function for an example.

```python
self.algorithms = {
    'Hartley': self.hartley_entropy,
    'Metric': self.metric_entropy,
    'Relative': self.relative_entropy,
    'Renyi': self.renyi_entropy,
    'Shannon': self.shannon_entropy,
    'Theil': self.theil_index,
    }
```
