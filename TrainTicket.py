"""
The approach here is to keep a dp array and intialize the first index of dp array to 0. each value in 
the dp array represents the min cost of train ricket till the particular point, the dp array is having len
of total number of travel days, now at every day we calculate 

1. if it is cheap to either buy a daily ticket, then it would be total cost till yesterday + daily ticket cost
2. if it is cheap to buy a weekly pass, so we go back to 7 days back and take that cost + the weekly pass cost
    here we consider that the we bought the weekly pass 7 days ago.
3. if it is cheap to buy a monthly pass.
finally we take the cheapest amoungst all for the particular index.
In this way we have the cheapest cost at the lat day.

"""
def mincostTickets(self, days, costs):
    dp = [0 for i in range(days[-1]+1)]
    for i in range(days[-1]+1):
        if i not in days:
            dp[i] = dp[i-1]
        else:
            day = dp[max(0,i-1)]+costs[0]
            week = dp[max(0,i-7)]+costs[1]
            month = dp[max(0,i-30)]+costs[2]
            dp[i] = min(day,week,month)
    return dp[-1]