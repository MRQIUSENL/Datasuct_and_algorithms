import random
def PX(old_arr,new_arr):
    for i in range(len(old_arr)):
        judgement_Key=False

        for j in range (len(new_arr)):
            if old_arr[i] < new_arr[j]:
                new_arr.insert(j,old_arr[i])
                judgement_Key=True
                break
        if not judgement_Key:
            new_arr.append(old_arr[i])

    return new_arr

random_numbers = [random.randint(1, 1000) for _ in range(1000)]
new_arr=[]
R=PX(random_numbers,new_arr)
print(R)