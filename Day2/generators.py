# def tv_channel():
#     yield "Star tv"
#     yield "Tensports"
#     yield "Sun Tv"
#     yield "News24-7"
#
# for chnl in tv_channel():
#     print(chnl)
# # program=tv_channel()
# # print(next(program))
# # print(next(program))
# # print(next(program))
# # print(next(program))
#

def fibonacci_series():
    x,y=1,1
    while True:
        yield x
        x,y=y,x+y

for f in fibonacci_series():
    if f>100000:
        break
    print(f,end=',')