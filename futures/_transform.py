import pulumi
from pulumi_random import RandomId, RandomString


def apply_example():
    my_str = RandomString("my-random-str", length=5)

    my_prefix = my_str.result.apply(lambda val: f"{val}-myhardcodedstring-")

    my_id = RandomId("my-random-id", byte_length=8, prefix=my_prefix)

    pulumi.export("my_str", my_str.result)
    pulumi.export("my_id", my_id.hex)


def all_example():
    my_str = RandomString("my-random-str", length=5)
    my_str2 = RandomString("my-random-str2", length=5)

    my_prefix = pulumi.Output.all(my_str.result, my_str2.result).apply(
        lambda args: f"{args[0]}-{args[1]}"
    )

    my_id = RandomId("my-random-id", byte_length=8, prefix=my_prefix)

    pulumi.export("my_str", my_str.result)
    pulumi.export("my_str2", my_str2.result)
    pulumi.export("my_id", my_id.hex)


def concat_example():
    my_str = RandomString("my-random-str", length=5)
    my_str2 = RandomString("my-random-str2", length=5)

    my_prefix = pulumi.Output.concat(my_str.result, "-", my_str2.result)
    my_id = RandomId("my-random-id", byte_length=8, prefix=my_prefix)

    pulumi.export("my_str", my_str.result)
    pulumi.export("my_str2", my_str2.result)
    pulumi.export("my_id", my_id.hex)


def from_input_example(my_str: pulumi.Input[str]):

    my_prefix = pulumi.Output.from_input(my_str).apply(
        lambda val: f"{val}-myhardcodedstring-"
    )

    my_id = RandomId("my-random-id", byte_length=8, prefix=my_prefix)

    pulumi.export("my_id", my_id.hex)


def wrong_way():
    my_str = RandomString("my-random-str", length=5)

    my_str.result.apply(
        lambda val: RandomId(
            "my-random-id", byte_length=8, prefix=f"{val}-myhardcodedstring-"
        )
    )


# apply_example()
# all_example()
# concat_example()
# from_input_example(RandomString("my-random-str", length=5).result)
# from_input_example("mystr")
wrong_way()
