import shelve

# with shelve.open("Fileio/bike") as bike:
#     bike['make'] = "Honda"
#     bike['model'] = "250 dream"
#     bike['color'] = "red"
#     bike['engine_size'] = 250

#     print(bike['engine_size'])
#     print(bike['color'])

with shelve.open("Fileio/bike2") as bike:
    # bike['make'] = "Honda"
    # bike['model'] = "250 dream"
    # bike['color'] = "red"
    # bike['engin_size'] = 250

    #del bike['engin_size']

    for key in bike:
        print(key)
    print(bike['engine_size'])
    print(bike['engin_size'])
    print(bike['color'])
