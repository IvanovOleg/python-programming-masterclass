# Create a program that receives a list of products to buy in a string format. Usually a sting
# contains only numeric values, but the program should be tolerated against literals as well.

# You have only $5000 in your pocket and you need to buy as much products as possible keeping in mind
# that the first product should always be bought.

# You need to count a number of products that could be bought in addition to the first one in the list.

# For example a list of products contains 4570,200,40,40,100,50,300 , would result in an output of :5

# 5000 - 4570
# 430 remaining products -> 200,40,40,100,50,300
# 430 - 40 (count 1)
# 390 remaining products -> 200,40,100,50,300
# 390 - 40 (count 2)
# 350 remaining products -> 200,100,50,300
# 350 - 50 (count 3)
# 300 remaining products -> 200,100,300
# 300 - 100 (count 4)
# 200 remaining products -> 200,300
# 200 - 200 (count 5)
# 0 remaining products -> 300

# If the product list contains literals, you program should output: invalid
# for example a product list of apples, honey, bread should return :invalid

# 5000 - apples
# invalid

# Testcase1: 4570,200,40,40,100,50,300 output 3
# Testcase2: apples,honey,bread output 'invalid'
# Testcase3: apples, 200,40,40,100,50,300 output 'invalid'
# Testcase4: 200,40,40,bread,100,50,300 output 'invalid'
# Testcase5: 5500, 200,40,40,100,50,300 output 0


def shopping(n):
    budget = 5000
    product_count = 0
    if n.replace(',', '').isnumeric():
        product_list = list(map(lambda x: int(x), n.split(',')))
        remaining_budget = budget - product_list[0]
        del(product_list[0])
        for _ in range(len(product_list)):
            if remaining_budget >= min(product_list):
                remaining_budget = remaining_budget - min(product_list)
                product_list.remove(min(product_list))
                product_count += 1
        print(product_count)
    else:
        print('invalid')

if __name__ == '__main__':
    n = "4570,200,40,40,100,50,300"
    # n = "apples,honey,bread"
    # n = "200,40,40,bread,100,50,300"

    shopping(n)
