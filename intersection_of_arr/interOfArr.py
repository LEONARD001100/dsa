class solution():
    def intersection(self,arr1,arr2):
        #first we need to add all the element and corresponding frequency of ar1
        freqDict={}
        
        for num in arr1:
            if num not in freqDict :
                freqDict[num]=1
            else :
                freqDict[num]+=1
        #now we need to take the second array and decrease the frequency if common element present and append to the final list
        intersection_element=[]

        for num in arr2:
            if num in freqDict and freqDict[num]!=0:
                intersection_element.append(num)
                freqDict[num]-=1
        return intersection_element




def main():
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    so=solution()
    print(so.intersection(arr1,arr2))

if __name__ == "__main__":
    main()
