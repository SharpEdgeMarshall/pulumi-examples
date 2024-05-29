import pulumi
from pulumi_random import RandomId, RandomString

my_str = RandomString("my-random-str", length=5)

my_id = RandomId(f"my-random-id-{my_str.result}", byte_length=5)
# my_id = RandomId(my_str.result, byte_length=5)
