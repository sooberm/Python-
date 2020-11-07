def kole(arr,w):
    A={}
    s=len(arr)
    for i in range(s):
        tmp=arr[i]
       
        temp=tmp[1]/tmp[0]

        
        A[i]=temp

    sorted (A.items())
    listofTuples = sorted(A.items() ,  key=lambda x: x[1])   
    print(listofTuples)
    size=len(A)
    res=0

    i=size-1 
    weight=0         
    while i>=0 :
        z=listofTuples[i][0]
        tmp=arr[z]
        print(arr[z])
        weight=weight+tmp[0]
        if weight<= w:
            res=res+tmp[1]                  
        i=i-1    

    print(res)













arr=[(5,10),(3,20),(8,25),(4,8)]
#arr={5:10,3:20,8:25,4:8}
w=13
kole(arr,w)