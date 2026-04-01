class pair_elements:
    def Sum2(self, nums, target):
        lookup={}
        
        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target-num],i)
            lookup[num]=i

value=int(input("Enter sum for which you want to make your search: "))
print("Index1 = %d, Index2=%d" %pair_elements().Sum2((5,10,20,30,40,50,60,70,80,90),value))

        