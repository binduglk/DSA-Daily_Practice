# Session 2 - Search Suggestions System
# LeetCode #1268
# Topic - Trie + Sorting
# Day 19

class Solution:
    def suggestedProducts(self,
                          products: list,
                          searchWord: str) -> list:
        products.sort()    # sort alphabetically!
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            suggestions = []

            for product in products:
                if product.startswith(prefix):
                    suggestions.append(product)
                if len(suggestions) == 3:
                    break

            result.append(suggestions)

        return result

# Testing
sol = Solution()
print(sol.suggestedProducts(
    ["mobile","mouse","moneypot","monitor","mousepad"],
    "mouse"))
# [["mobile","moneypot","monitor"],
#  ["mobile","moneypot","monitor"],
#  ["mouse","mousepad"],
#  ["mouse","mousepad"],
#  ["mouse","mousepad"]]

print(sol.suggestedProducts(
    ["bags","baggage","banner","box","cloths"],
    "bags"))