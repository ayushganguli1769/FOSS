import sys
class profitLoss:
    def __init__(self):
        self.array = []
        self.length = 0
    def add(self,index):# first,last,profit
        self.array.append([index,index,0])
        self.length += 1
    def update(self,last_index,profit):
        self.array[self.length-1][1] = last_index
        self.array[self.length-1][2] = profit
t = int(input())
for _ in range(t):
    listP = profitLoss()
    n = int(input())
    P  = list(map(int,input().rstrip().split()))[:n]
    start_profit = P[0]#value at index where profit streak starts
    streak_profit = -sys.maxsize
    profit_list = profitLoss()
    profit_list.add(0)
    initialized = False
    condition = False
    for i in range(len(P)):
        profit_at_that_point = P[i] - start_profit
        if profit_at_that_point >= streak_profit:
            if initialized:
                condition = True
            initialized = True
            streak_profit = profit_at_that_point
            profit_list.update(i,streak_profit)
        else: # profit is decreasing. time to sell
            start_profit = P[i]
            streak_profit = 0 
            profit_list.add(i)
    if condition:
        for streak in profit_list.array:
            if streak[2] >0:
                condition = True
                print_string = "("+ str(streak[0]) + " " + str(streak[1])+ ")"
                print(print_string,end=" ")
    else:
        print("No Profit")

    print()