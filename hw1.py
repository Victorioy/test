# def isdiv(n):
#     i = 1
#     while i<n:
#         if n%i == 0:
#             print('divisor_list',i)
#         i = i + 1
#
#
#
# def filter_list(a):
#     divisor_list = []
#     if isdiv(a):
#         divisor_list.append(a)
#     return divisor_list
#
# def main():
#     a = float(input('Enter a number:'))
#     print("divisor_list", filter_list(a))
# if __name__ == '__main__':
#     main()

def give_divisors(num):
    divisors = []
    for i in range (1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    num = int(input('Enter a number:'))
    print('Divisors:', give_divisors(num))

if __name__ == '__main__':
    main()
