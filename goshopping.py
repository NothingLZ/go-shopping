# -*-coding:utf-8-*-
print "-----------welcome--------------"
products = ['Car','Iphone','coffee','Mac','Cloths','Bicycle']
prices = [250000,4999,35,9688,450,500]
shop_list = []
list = ["product"]
number = ["number"] 
salary = int(raw_input('please input your salary:'))
while True :
    print "Thing have in the  shop"
    for index,i in enumerate(products):
        print index,i,'\t',prices[products.index(i)]
    choice =raw_input("please input one itme to buy : ")
    if choice.isdigit():
        choice = int (choice)
        if choice <= len(products)-1:
            shop_list.append(products[choice])
            p_prices = prices[choice]
            if p_prices <= salary:
                salary -= p_prices
                print "******shoplist******"
                for v in shop_list:
                    print '\t', v
                print "********************"
                print 'shoplist add %s, salary is %s' % (products[choice],salary)
            else:
                print ''' salaey is enough ,salary is %s. try to buy sth:
                   ***********leave please input "quit"************ ''' % salary
        else:
            print "\033[41;1m sorry! your input, shoplist is not have \033[0m"
    elif choice == "quit":
        for k,v in enumerate(products):
            if products[k] in shop_list:
                list.append(v)
                number.append(shop_list.count(v))
        print "********your shop list******** "
        for index, i in enumerate(list):
            print index, i, '\t', number[list.index(i)]
        print "your salary is %s" % salary
        print "********thank  you ********"
        break