# def Even(num):
#     if num%2==0:
#         print(num)
#     if num==25:
#         return
#     Even(num+1)
# Even(1)

def Even(sve,eve):
    if sve%2==0:
        print(sve)
    if sve==eve:
        return
    Even(sve+1,eve)
sve=int(input('Start Number: '))
eve=int(input('End Number: '))
Even(sve,eve)