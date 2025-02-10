# Tower Of Hanoi
def towerOfHanoi(n,fromRod,auxRod,toRod):
    if 1 == n:
        print("Move Disk 1 From Rod",fromRod,"To Rod",toRod)
        return

    towerOfHanoi(n-1,fromRod,auxRod,toRod)
    print("Move Disk",n,"From Rod",fromRod,"To Rod",toRod)
    towerOfHanoi(n-1,auxRod,toRod,fromRod)

towerOfHanoi(3,"A","B","C")
