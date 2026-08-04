class solution():
    #this is a funtion which find the maxsum of subarray also considering the rotation
    def maxSumSubArrLoopAround(self,arr,k):
        start=0
        kPointer=k
        maxSum=0
        currentSum=0
        for i in range(k):
            currentSum+=arr[i]
        maxSum=currentSum
        for i in range(len(arr)):
            kPointer=kPointer%len(arr)
            newSum=currentSum-arr[start]+arr[kPointer]
            if newSum > maxSum :
                maxSum=newSum
            currentSum=newSum
            start+=1
            kPointer+=1
        return maxSum

    #This is a function which find the maxsum of the subarray like continuity that means no loop back to the first element
    def maxSumSubArr(self,arr,k):
        start=0
        kPointer=k
        maxSum=0
        currentSum=0
        for i in range(k):
            currentSum+=arr[i]
        maxSum=currentSum
        for i in range(len(arr)-k):
            newSum=currentSum-arr[start]+arr[kPointer]
            if newSum > maxSum :
                maxSum=newSum
            currentSum=newSum
            start+=1
            kPointer+=1
        return maxSum

def main():
    arr = [9,8,1,2,3]
    k = 2
    so=solution()
    print(so.maxSumSubArrLoopAround(arr,k))

if __name__ == "__main__":
    main()
