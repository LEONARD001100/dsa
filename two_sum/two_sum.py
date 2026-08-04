class solution():
    def two_sum(self,arr,target):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==target:
                    return [i,j]
        return None
    
    def two_sum_optimized(self,arr,target):
        index_dict={}
        for i in range(len(arr)):
            compliment=target-arr[i]
            if compliment in index_dict:
                return [index_dict[compliment],i]
            index_dict[arr[i]]=i
        return None

def main():
    arr=[3,2,7,4,1]
    target=9
    so=solution()
    print(so.two_sum_optimized(arr,target))

if __name__ == "__main__":
    main()

