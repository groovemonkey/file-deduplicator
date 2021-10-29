# Dave's File Content Deduplicator

Takes a filename as an argument, and gives you deduplicated lines as output. It does not modify the original file.

`➜  ~ cat /tmp/test`

```
floof

# bloop
schnerg

'\test yes "
jaa
foo
foo

floof
jaa
'''zoo
hehe
'''"""
bloopm
```

`➜  ~ ./code/deduplicator/dedup.py /tmp/test`
```
floof

# bloop
schnerg

'\test yes "
jaa
foo

'''zoo
hehe
'''"""
bloopm
```

