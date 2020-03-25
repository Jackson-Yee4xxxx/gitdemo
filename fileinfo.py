# -*- coding: utf-8 -*-
#找零问题
#解法二：贪心算法（通用程序，可以由用户输入找零钱数和硬币种类）
#例4.13-change_Greedy.py

#1、定义函数，利用贪心算法求和为11的最优硬币组合，存入字典change_dict中
def change(coinValueList,change):          
    #coinValueList为存储不同面值硬币的列表，change为所需找给顾客的零钱
    if change == 0:                         #增强程序鲁棒性
        return 0
    elif change < 0:
        print('error')
        return 1
    else:
        list_coin = coinValueList
        list_coin.sort(reverse = True)     #倒序（即按从大到小顺序）排列硬币面值列表
        print('倒排序后的list_coin为：',list_coin)
        #print('coinValueList为：',coinValueList)    #由于sort方法是在原位置对列表进行排序，故coinValueList也变得与list_coin一样
        print ('-------------------------------------------')
        for i in list_coin: 	            #遍历列表，每次从找零硬币种类中找当前可选择的最大值i
            change_dict[i] = int(change/i)  #创建字典change_dict，键i为最大面值；值为change/i（整型），此即是i的个数
            #字典change_dict用于存放贪心算法求得的各种硬币面值的个数，键为硬币面值，值为对应的个数
            print ('最优硬币组合change_dict为：',change_dict)
            newchange = change % i          #新所凑硬币钱数 ← 原所凑硬币钱数 % i（即扣除已凑零钱数后剩下的零钱）
            print ('新所凑硬币钱数newchange为：',newchange)
            print ('-------------------------------------------')
            if newchange == 0:              #若新所凑硬币钱数为0，说明已凑够找零
                break                       #则跳出循环
            else:
                change = newchange