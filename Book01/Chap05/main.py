from typing import List

from layer_naive import *

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.s1(cost, 0, {})

    def s1(self, cost, total_cost, memo):
        strCost = [str(c) for c in cost]
        key = "/".join(strCost)

        if key in memo and memo[key] < total_cost: return memo[key]
        if len(cost) <= 1: return total_cost

        c1 = self.s1(cost[1:], total_cost + cost[0], memo)
        c2 = self.s1(cost[2:], total_cost + cost[1], memo)

        memo[key] = min(c1, c2)
        return memo[key]

if __name__ == '__main__':
    apple = 100
    apple_num = 2
    tax = 1.1

    mul_apple_layer = MulLayer()
    mul_tax_layer = MulLayer()

    apple_price = mul_apple_layer.forward(apple,  apple_num)
    price = mul_tax_layer.forward(apple_price, tax)


    dprice = 1
    dapple_price, dtax = mul_tax_layer.backward(1)
    dapple, dapple_num = mul_apple_layer.backward(dapple_price)



    print(dapple, dapple_num, dtax)


