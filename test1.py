def run_test():
    print("Test 1 - dictionaries")

    me = {
        "first": "Edgar",
        "last": "Castillo",
        "age": 23,
        "hobbies": [],
        "address": {
            "street": "Evergreen",
            "number": "22-B",
            "city": "Springfield",
            "state": "CA",
            "zip": "92101"
        }
    }

    # print dictionary
    print(me)

    # print keys
    print(me["first"] + " " + me["last"])

    # change values
    me["age"] = me["age"] + 1
    me["age"] = 99

    # add new keys
    me["preferred_color"] = "blue"
    print(me)

    # read if exists
    if "middle_name" in me:  # checks for existence
        print(me["middle_name"])

    # print the full address on a single line
    address = me["address"]
    print("----- address -----")
    print(address)
    print(type(address))

    print(
        f"{address['street']} {address['number']}, {address['city']}, {address['state']}, {address['zip']}")


run_test()
