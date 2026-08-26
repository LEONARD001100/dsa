class solution():
    def majorityElement(self,arr):

        count_dict={}
        for i in range(len(arr)):

            if arr[i] not in count_dict:
                count_dict[arr[i]]=1
            else:
                count_dict[arr[i]]+=1

            if count_dict[arr[i]] > (len(arr)/2):
                return arr[i]
    def boyer_moore(self,arr):
        n=len(arr)
        candidate=arr[0]
        count=1
        for i in range(1,n):
            if candidate==arr[i]:
                count+=1
            else :
                count-=1
            if count==0:
                candidate=arr[i]
                count=1
        return candidate

def main():
    arr=list(map(int,input().split()))
    so=solution()
    print(so.boyer_moore(arr))

if __name__ == "__main__":
    main()

