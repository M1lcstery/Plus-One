class Solution:
    def plusOne(self, digits):
        n = len(digits)
        j = n - 1

        while j >= 0:
            if digits[j] == 9:
                digits[j] = 0
                j -= 1
            else:
                digits[j] += 1
                return digits

        # If we are here, all digits were 9, so we need to carry over
        return [1] + digits