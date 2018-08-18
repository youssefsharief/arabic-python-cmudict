* Add the dict files in "ar_cmudict/data" as the following names
    * haraka_moshakal.dic
    * haraka.phone

```python
ar_cmudict.entries()
>>> [('آباط', ['<', 'aa', 'b', 'AA', 'T', '1']),
 ('آباق', ['<', 'aa', 'b', 'AA', 'q', '1'])]
```

```python
ar_cmudict.phones()
>>> [ ('UU0', []),
 ('Z', []),
 ('^', []),
 ('a', []),
 ('aa', []),
 ('b', []),
 ('d', []),
 ('f', []),
 ('g', []),
 ('h', []),
 ('i0', []),
 ('i1', []),
 ('ii0', []),
 ('j', []),
 ('k', [])]
```
* Test
    * `python -m pytest`
* Install lib locally
    * `pip install -e .`