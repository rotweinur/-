silver_amount=96
golden_amount=silver_amount/16
silver_cost=48
all_cost=int(input())
golden_TR=all_cost-(silver_cost*silver_amount)
golden_cost=golden_TR//golden_amount
print(golden_cost)
