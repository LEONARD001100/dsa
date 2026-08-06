class solution():
    def buySellStock(self,arr):
        buy=arr[0]
        sell=0
        profit=0
        for i in range(1,len(arr)):
            if not arr:
                return None
            if arr[i] > buy:
                sell=arr[i]
                currentProfit = sell-buy
                if currentProfit > profit:
                    profit =currentProfit
            else:
                buy=arr[i]
        return profit

def main():
    arr=[6,5,4,3,2,10]
    
    so=solution()
    print(so.buySellStock(arr))

if __name__ == "__main__":
    main()
