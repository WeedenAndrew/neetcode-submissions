class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)

        while b:
            wo_carry = a ^ b
            carry = (a & b) << 1
            a, b = wo_carry, carry

        return bin(a)[2:]