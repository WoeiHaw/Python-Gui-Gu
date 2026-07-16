# import trade.order
# import trade.pay
#
# trade.order.create_order()
# trade.pay.wechat_pay()

# import trade.order as dd
# import trade.pay as zf
#
# dd.create_order()
# zf.wechat_pay()

# from trade.order import  max_order_amount,create_order
# from trade.pay import tineout ,wechat_pay
#
# print(max_order_amount)
# print(tineout)
# create_order()
# wechat_pay()

# from trade.order import  max_order_amount as mx_amt,create_order
# from trade.pay import tineout ,wechat_pay as w_pay
#
# print(mx_amt)
# print(tineout)
# create_order()
# w_pay()

# from trade.order import *
# from trade.pay import *
#
# print(max_order_amount)
# create_order()
# cancel_order()
# show_info()
#
# print(tineout)
# wechat_pay()
# ali_pay()
# show_info()

# from trade import order, pay
# order.create_order()
# pay.wechat_pay()

# from trade import order as dd, pay as p
# dd.create_order()
# p.wechat_pay()

# from trade import *
# print(a)
# print(b)
# print(order.max_order_amount)
# order.create_order()
# print(pay.tineout)
# pay.wechat_pay()

# import trade
# print(trade.a)
# print(trade.b)
# trade.order.create_order()
# trade.pay.wechat_pay()


# from trade.hello.h1 import say_hello
# say_hello()

from collections import Counter
name = ["张三","李四","王五","李华","张三","李四","张三","王五"]
result = Counter(name)
print(result)

