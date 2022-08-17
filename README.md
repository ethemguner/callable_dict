# callable_dict
I get tired to use "get" for dictionaries. So...


# Usages

```
usual_dict = {
    "a": 1,
    "b": {
        "inner_key": 2,
        "inner_key2": 3,
        "inner_key3": {
            "very_inner_key": 4, 
            "very_inner_key2": 5
        },
    },
    "c": [1, 2, 3, 4],
}

callable_dict = CallableDict(usual_dict)

print(callable_dict.a)
# 1

print(callable_dict.b)
# <__main__.CallableDict at 0x106202220>

print(callable_dict.b.inner_key)
# 2

print(callable_dict.b.inner_key2)
# 3

print(callable_dict.b.inner_key3)
# <__main__.CallableDict object at 0x106bcd2b0>

print(callable_dict.b.inner_key3.very_inner_key)
# 4

print(callable_dict.c)
# [1, 2, 3, 4]
```
