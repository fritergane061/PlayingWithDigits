def dig_pow(n, p):
    digits = list(str(n))
    digit_sum = sum(int(digit) ** (p + index) for index, digit in enumerate(digits))
    if digit_sum % n == 0:
        return digit_sum // n
    else:
        return -1

from solution import dig_pow
import codewars_test as test

@test.describe("Fixed tests")
def fixed_test():
    @test.it("Samples")
    def sample_tests():
        test.assert_equals(dig_pow(89, 1), 1)
        test.assert_equals(dig_pow(92, 1), -1)
        test.assert_equals(dig_pow(46288, 3), 51)
        test.assert_equals(dig_pow(41, 5), 25)
        test.assert_equals(dig_pow(114, 3), 9)
        test.assert_equals(dig_pow(8, 3), 64)
