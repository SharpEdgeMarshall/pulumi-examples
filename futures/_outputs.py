from pulumi_random import RandomId

my_id = RandomId("my-random-id", byte_length=8)

# print(my_id.hex)
# my_id.hex.apply(lambda hex: print(f"Hex: {hex}"))
