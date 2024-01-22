#! /usr/bin/env python3

### PLEASE DO NOT USE THIS FOR PROJECT 2 SUBMISSION -- THIS IS NOT DONE YET ###

def compare(interv):
    numOfNonOvrLap = 0 #init number of overlap occurances
    intervFinTime = 0 # original finishTime is 0 and updated when we compare fin time to that of start time of the next interv
    # newInterv = interv
    # newInterv = []
    # print(interv.sort(key = lambda x: x[1]))
    interv.sort(key = lambda x: x[1])
    print("Sorted: ", interv)
    for (s, f) in interv: 
        # print(s,f)
        if (int(s) >= int(intervFinTime)): # only checks based off first interval given not based off largest nonOvrLap intervs
            # print(s,f)
            # print("HIT")
            numOfNonOvrLap += 1 # if there is no overlap then add it to the list
            intervFinTime = f
    return numOfNonOvrLap

def solution(intervals):
    # highestOveLap = 0
    # counter = 1
    # # print(len(intervals))
    # initialOverlap = compare(intervals)
    # # print("initial overlap: ", initialOverlap)
    # if (len(intervals) > 3):
    #     for i in range(0, len(intervals)):
    #         # del intervals[1] # delete the interval that we don't want to look at anymore
    #         while (highestOveLap < initialOverlap):
    #             highestOveLap = compare(intervals[counter:])
    #             # print("new highest: ", highestOveLap)
    #             counter+=counter
    #             # if (highestOveLap >= initialOverlap): 
    #             #     break
    #     return highestOveLap
    # else:
    #     return compare(intervals)

    return compare(intervals)

    
def main():
    intervs = []
    for line in range(int(input())): # reading each line of the file into an array (each pair of starting/stopping)
        intervs.append(input().split(" ")) #splits each line into split elems in 2d array/list

    print("Original: ", intervs)
    # print(intervs[1])
    print(solution(intervs))    
    

if __name__ == "__main__":
    main()
