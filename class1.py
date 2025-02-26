# Python Data Types Demonstration

# Numeric Types
integer_num = 10  # int
decimal_num = 10.5  # float
complex_num = 3 + 4j  # complex

# Sequence Types
string_value = "Hello, Python!"  # str
list_value = [1, 2, 3, "Python", 4.5]  # list
tuple_value = (10, 20, "Tuple", 3.14)  # tuple
range_value = range(5)  # range

# Set Types
set_value = {1, 2, 3, 4, 5}  # set
frozenset_value = frozenset([1, 2, 3, 4, 5])  # frozenset (immutable set)

# Mapping Type
dict_value = {"name": "Python", "type": "Programming Language"}  # dict

# Boolean Type
bool_value = True  # bool

# Binary Types
bytes_value = b"Hello"  # bytes
bytearray_value = bytearray([65, 66, 67])  # bytearray
memoryview_value = memoryview(bytearray([65, 66, 67]))  # memoryview

# None Type
none_value = None  # NoneType

# Special Python Keywords
import keyword
print("Python Special Keywords:")
print(keyword.kwlist)

# Output all values
data_types = {
    "Integer": integer_num,
    "Float": decimal_num,
    "Complex": complex_num,
    "String": string_value,
    "List": list_value,
    "Tuple": tuple_value,
    "Range": list(range_value),
    "Set": set_value,
    "Frozenset": frozenset_value,
    "Dictionary": dict_value,
    "Boolean": bool_value,
    "Bytes": bytes_value,
    "Bytearray": bytearray_value,
    "Memoryview": list(memoryview_value),
    "NoneType": none_value,
}

for dtype, value in data_types.items():
    print(f"{dtype}: {value} ({type(value)})")
