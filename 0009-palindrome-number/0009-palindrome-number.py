class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 :
            return False
        number = str(x)
        p_number = number[::-1]
        if number == p_number :
            print(f"{number} reads as {p_number} from left to right and from right to left")
            return True
        else:
            print(f"from left to right, it reads {x}. from right to left, it becomes {p_number}. there it is not a palindrome ")
            return False
