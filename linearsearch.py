arr=[8,2,5,9,1]

target=9

found=False

for i in range(len(arr)-1):
    if arr[i]==target:
        index=i
        found=True
        print(f"found at the index : {index}")
        break
    else:
        continue
if not found:
    print("Not found")
