from icecream import ic



# two collections for the zip function (new parameters will be called from main.py and test.py but keeping these here just in case it's a requirement in the test)
it1 = [1, 2, 3]
it2 = ['a', 'b', 'c']


# Zips it1 and it2 together.
def myzip(it1, it2):
    print("==Zipping Sample==")
    ic(it1)
    ic(it2)
    print("Zip result: ", list(zip(it1, it2)))
    ic(list(zip(it1, it2)))
    return list(zip(it1, it2))

