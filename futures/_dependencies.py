import pulumi
from pulumi_random import RandomId, RandomInteger

my_int = RandomInteger("my-random-int", max=10, min=3)
my_int2 = RandomInteger("my-random-int2", max=10, min=3)

# my_iny.result: pulumi.Output[int]
# byte_length: pulumi.Input[int]
# byte_length: Union[int, Awaitable[int], "Output[int]"]
my_id = RandomId("my-random-id", byte_length=my_int.result)

pulumi.export("my_int", my_int.result)
pulumi.export("my_id", my_id.hex)
