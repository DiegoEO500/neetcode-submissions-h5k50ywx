class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:
            if op == "+":
                # Add the sum of the last two elements
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # Double the last element
                stack.append(stack[-1] * 2)
            elif op == "C":
                # Remove the last element
                stack.pop()
            else:
                # It's an integer (handles negative numbers correctly)
                stack.append(int(op))
        
        return sum(stack)