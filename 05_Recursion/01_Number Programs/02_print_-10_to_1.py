# def numbers(num):
#     print(num)
#     if num==1:
#         return
#     numbers(num-1)
# numbers(10)

def numbers(evn,svn):
    print(evn)
    if evn==svn:
        return
    numbers(evn-1,svn)
evn=int(input('Last number: '))
svn=int(input('First number: '))
numbers(evn,svn)