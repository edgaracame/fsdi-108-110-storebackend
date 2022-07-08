from unicodedata import name


def start_tests():
    print("----- List tests -----")

    # list
    nums = [1, 2, 3, 4, 5, 6]

    # print list
    print(nums[0])
    print(nums[1])

    # add elements to a list
    nums.append(9)
    print(nums)

    # for loop
    for n in nums:
        print(n)

    # for loop from 0 to 20
    for number in range(0, 21):
        print(number)
    print()


def test1():
    print("----- test 1 -----")

    prices = [123, 3, 23, 6475, 58, 89, 45, 34, 87,
              34, -12, 23, 123, -23, -123, 0, 123, 0, -29, 10]

    # 1.- print numbers lower than 50
    # 2.- count how many numbers are lower than 50
    # 3.- the sum of all numbers
    # 4.- the sum of all numbers greater than zero
    # 5.- count how manu zeros there are
    count_fifty = 0
    count_zeros = 0
    all_numbers = 0
    sum_zero = 0
    for p in prices:
        if p < 50:
            print(p)
            count_fifty += 1

        all_numbers += p

        if p > 0:
            sum_zero += p

        if p == 0:
            count_zeros += 1

    print()
    print(f"There are {count_fifty} prices lower than $50")
    print(f"The sum of all prices is ${all_numbers}")
    print(f"The sum of all prices greater than zero is ${sum_zero}")
    print(f"There are {count_zeros} zeros")
    print()


def test2():
    print("----- Test 2 -----")

    users = [
        {
            "gender": "F",
            "name": "Louis",
            "color": "Green"
        },
        {
            "gender": "M",
            "name": "Manuel",
            "color": "Gray"
        },
        {
            "gender": "F",
            "name": "Rossy",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Renny",
            "color": "pink"
        },
        {
            "gender": "M",
            "name": "Roman",
            "color": "Purple"
        },
        {
            "gender": "m",
            "name": "John",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Susan",
            "color": "Black"
        }
    ]

    # 1.- print all the names
    # 2.- print how many users there are in the list
    # 3.- print the name of users who likes pink or PINK or Pink or PiNk

    for u in users:
        print(u["name"])

    print()
    print(f"There are {len(users)} users in the list")

    print()
    print("Users who like color pink:")
    for u in users:
        if u["color"].lower() == "pink":
            print(u["name"])


print()


def test3():
    print()
    print("----- Test 3 -----")
    print()

    prices = [123, 3, 23, 6475, 58, 89, 45, 34, 87,
              34, -12, 23, 123, -23, -123, 0, 123, 0, -29, 10]

    greatest = prices[0]

    for p in prices:
        if(p > greatest):
            greatest = p

    print(f"The highest price is ${greatest}")


start_tests()
test1()
test2()
test3()
