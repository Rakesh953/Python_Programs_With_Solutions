# def numbers(num):
#     print(num)
#     if num==10:
#         return
#     numbers (num+1)
# numbers(1)


def numbers(svn,evn):
    print(svn)
    if svn==evn:
        return
    numbers(svn+1,evn)
svn=int(input('First number: '))
evn=int(input('Second number: '))
numbers(svn,evn)

