more = [x + 1 for x in [1,2,3,4]]
#[2,2,3,4]
#[2,3,3,4]
#[2,3,4,4]
#[2,3,4,5]
print(more) #[2, 3, 4, 5]

##################################################################################################

def square(n:int) -> int:
    return n * n
#call 1: n = 1, return 1
#call 2: n = 2, return 4
#call 3: n = 3, return 9
#call 4: n = 4, return 16

squares = [square(x) for x in [1,2,3,4]] #squares is [1,4,9,16] and it's the list of the
print(squares) #above return values in order

##################################################################################################

def check(n:int) -> bool:
    return n > 2
#call 1: n = 0, return False
#call 2: n = 1, return False
#call 3: n = 2, return False
#call 4: n = 3, return True
#call 5: n = 4, return True
answer = [x for x in range(5) if check(x)] #answer is [3,4]
print(answer)

##################################################################################################

def inc(m: int) -> int:
    return m + 1
#call 1: m = 0, return 1
#call 2: m = 1, return 2
#call 3: m = 2, return 3
#call 4: m = 3, return 4
#call 5: m = 4, return 5

#def check(n:int) -> bool:
#    return n > 2
#call 1: n = 0, return False
#call 2: n = 1, return False
#call 3: n = 2, return False
#call 4: n = 3, return True
#call 5: n = 4, return True



answer = [inc(x) for x in range(5) if check(x)]
print(answer) #answer is [4,5]

##################################################################################################

