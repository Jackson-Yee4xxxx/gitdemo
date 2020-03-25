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

#2、定义函数，检查所求得的解是否为可行解                  
def checkOk(change_res,oChange):               
#change_res为存放结果的字典，键为某种硬币面值，对应的值为该种硬币的个数；oChange为需要找零的钱数
    csum = 0                               # change_res中所有硬币钱数的和 
    for key in change_res:                 #遍历字典change_res
        csum = csum + key*change_res[key]  #将各种硬币面值与对应个数相乘，再相加
    if csum == oChange:                    #若change_res中所有硬币钱数的和等于需要找零的钱数
        return True
    
#3、定义函数，获得找零的硬币总个数
def coinNum(change_res):                   #change_res为存放结果的字典             
    num = 0                                #找零的硬币个数
    for key in change_res:                 #遍历字典change_res
        if change_res[key] != 0:
            num = num + change_res[key]    #将所有的值相加，即得到找零的硬币总个数
    return num

#4、主函数
if __name__ == '__main__':
    clist = []                         #存放硬币种类列表
    change_dict = {}                   #全局变量，存放结果的字典，键为某种硬币面值，对应的值为该种硬币的个数
    #（1）输入找零数和硬币种类
    cvalue = int(input('请输入找零数(单位：元)：'))
    ctemp = int(input('请输入硬币种类，以非正数结束：'))
    while ctemp > 0:                   #采用while语句，可以多次输入硬币种类
        clist.append(ctemp)                #将输入的硬币种类添加到clist列表中
        ctemp = int(input('请输入硬币种类，以非正数结束：'))        

    #（2）调用change函数，采用贪心算法求得和为11的最优硬币组合，得到字典change_dict
    change(clist,cvalue)                        

   #（3）调用checkOk函数，检查所求得的解是否为可行解
    if checkOk(change_dict, cvalue) == True:    
        print ("找零结果：", change_dict)
        print ("找零个数：", coinNum(change_dict))#（4）调用coinNum函数，获得找零的硬币个数
    else:
        print ("无解")