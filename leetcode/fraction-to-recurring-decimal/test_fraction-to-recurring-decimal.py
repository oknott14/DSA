class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result = []
        # Abs and track sign
        if numerator / denominator < 0:
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        remainders = dict()
        result.append(str(numerator // denominator))
        numerator = (numerator % denominator) * 10  # 50

        if numerator != 0:
            result.append(".")

        while numerator != 0:
            if numerator in remainders:
                split = remainders[numerator]
                result.insert(split, "(")
                result.append(")")
                break

            remainders[numerator] = len(result)
            result.append(str(numerator // denominator))
            numerator = (numerator % denominator) * 10

        return "".join(result)


soln = Solution()


def test_case_1():
    assert soln.fractionToDecimal(2, 1) == "2"


def test_case_2():
    assert soln.fractionToDecimal(1, 2) == "0.5"


def test_case_3():
    assert soln.fractionToDecimal(4, 333) == "0.(012)"


def test_whole_then_frac():
    assert soln.fractionToDecimal(105, 10) == "10.5"


def test_case_4():
    assert soln.fractionToDecimal(4, 9) == "0.(4)"


def test_negative():
    assert soln.fractionToDecimal(-4, 9) == "-0.(4)"


def test_dec_then_repeating():
    assert soln.fractionToDecimal(1, 6) == "0.1(6)"


print(soln.fractionToDecimal(1, 6))
