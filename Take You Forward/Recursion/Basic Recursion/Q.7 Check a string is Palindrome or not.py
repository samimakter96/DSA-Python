def isPalindrome(s):
    # Initialize pointers at the beginning and end of the string
    left = 0
    right = len(s) - 1

    # Continue the loop until the pointers meet or cross each other
    while left < right:
        # Skip non-alphanumeric characters from the left
        if not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from the right
        elif not s[right].isalnum():
            right -= 1
        else:
            # Compare characters at the current positions (case-insensitive)
            if s[left].lower() != s[right].lower():
                # If not equal, the string is not a palindrome
                return False
            # Move pointers towards the center of the string
            else:
                left += 1
                right -= 1

    # If the loop completes without returning False, the string is a palindrome
    return True


if __name__ == "__main__":
    # Example usage
    str = "A man, a plan, a canal, Panama!"
    ans = isPalindrome(str)

    # Output the result
    if ans == True:
        print("Palindrome")
    else:
        print("Not Palindrome")

# Time Complexity: O(N)  Space Complexity: O(1)


""" Using Recursion: check if a given string is palindrome or not """


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Helper function to check if a character is alphanumeric
        def is_alphanumeric(char):
            return char.isalnum()

        # Helper function to convert a character to lowercase
        def to_lower(char):
            return char.lower()

        # Recursive function to check if the substring is a palindrome
        def check_palindrome(start, end):
            # Base case: if the pointers meet or cross, the substring is a palindrome
            if start >= end:
                return True

            # Skip non-alphanumeric characters from the start
            while start < end and not is_alphanumeric(s[start]):
                start += 1

            # Skip non-alphanumeric characters from the end
            while start < end and not is_alphanumeric(s[end]):
                end -= 1

            # Compare characters at the current positions (case-insensitive)
            if to_lower(s[start]) != to_lower(s[end]):
                return False

            # Move pointers towards the center of the substring and continue recursion
            return check_palindrome(start + 1, end - 1)

        # Initialize pointers and call the recursive function
        return check_palindrome(0, len(s) - 1)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    input_str = "A man, a plan, a canal, Panama!"
    result = solution.isPalindrome(input_str)
    if result:
        print("Palindrome")
    else:
        print("Not Palindrome")


def is_palindrome(s):

    def check_palindrome(start, end):
        # Base case: if the pointers meet or cross, the substring is a palindrome
        if start >= end:
            return True
        # step-1: check if start is non alpha-numeric if it is then skip
        while start < end and not s[start].isalnum():
            start += 1

        # step-2: check if end is non alpha-numeric if it is then skip
        while start < end and not s[end].isalnum():
            end -= 1
        # step-3: compare start lower case to end lower case if they are not same return false
        if s[start].lower() != s[end].lower():
            return False
        # step-4: if they are same move pointer
        return check_palindrome(start + 1, end - 1)

    # Initialize pointers and call the recursive function
    return check_palindrome(0, len(s)-1)


s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))
