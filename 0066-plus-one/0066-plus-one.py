class Solution(object):
    def plusOne(self, digits):
         # Convert the list of digits into a string
        str_val = "".join(map(str, digits))
        # Convert the string to an integer and add one
        total_sum = int(str_val) + 1
        # Convert the resulting number back into a list of digits
        result = list(map(int, str(total_sum)))
        return result



        