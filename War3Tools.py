# -*- coding:utf-8 -*-
import sys
import xlrd
import tkinter as tk
import tkinter.messagebox

def function_read(sheetDaoju):
    print(sheetDaoju.nrows)
    print(sheetDaoju.ncols)
    __ItemInfo = ""
    lists = [[] for i in range(sheetDaoju.ncols)]
    lists2 = []


    # for m in range(1, len(__ItemArray)):
    #     # print(__ItemArray[m])
    #     # __ItemArray[m]
    #     pass

    for i in range(2, sheetDaoju.nrows):
        # print(sheetDaoju.cell_value(2, 0))
        for j in range(sheetDaoju.ncols):
            # print(sheetDaoju.cell_value(0,j))
            lists[j].append(sheetDaoju.cell_value(i,j))
            # pass

    for i in range(1, sheetDaoju.nrows-3):
        # print(sheetDaoju.cell_value(2, 0))
        for j in range(sheetDaoju.ncols):
            # print(sheetDaoju.cell_value(0,j))
            lists2.append(sheetDaoju.cell_value(i,j))
            # pass

    print(lists2)

    return lists2, lists
def function_lua(sheetDaoju):
    _sheetName = sheetName.get(index1=1.0, index2=tk.END)[:-1]
    __Lua_Title, __Lua_Item = function_read(sheetDaoju)
    print(__Lua_Item[0])
    LuaCode = luaCodeStart + luaCodeFunction
    LuaCode1 = luaCodeStart + luaCodeFunction1
    if _sheetName == "":
        tempItem = LuaCode
    else:
        tempItem = LuaCode1
    for i in range(len(__Lua_Item[0])):
        for j in range(len(__Lua_Item)):
            if _sheetName[:-5] == "通魔":
                if j == 0:
                    tempItem = tempItem + luaCodeID2.format(_sheetName[-4:], __Lua_Item[0][i])
                    print(_sheetName[-4:])
                else:
                    if __Lua_Item[j][i] == "":
                        pass
                    else:
                        tempItem = tempItem + luaCodeItem.format(__Lua_Title[j], __Lua_Item[j][i])
            else:
                if j == 0:
                    tempItem = tempItem + luaCodeID.format(__Lua_Item[0][i])
                    print(_sheetName[-4:])
                else:
                    if __Lua_Item[j][i] == "":
                        pass
                    else:
                        tempItem = tempItem + luaCodeItem.format(__Lua_Title[j], __Lua_Item[j][i])
        tempItem = tempItem + "\t?>\n"
    # print(tempItem)

    tempItem = tempItem + luaCodeEnd
    print(tempItem)
    if _sheetName == "":
        f = open(path + "\道具.txt", 'w')
        f.write(tempItem)
        f.close()
    else:
        f = open(path + "\\"+_sheetName[:-5]+"技能.txt", 'w')
        f.write(tempItem)
        f.close()
def T1():
    # 根据表格名称获取表格
    # 打开文件
    # path + '/' +file 是文件的完整路径
    path = FilePath.get(index1=1.0, index2=tk.END)[:-1]
    data = xlrd.open_workbook(path)
    _sheetDaoju = data.sheet_by_name('道具')
    function_lua(_sheetDaoju)
def T2():
    SkillTip.place(x=5, y=35)
    sheetName.place(x=80, y=40)
    Btn1.place(x=30, y=100)
    Btn2.place(x=260, y=100)
    Btn3.place(x=150, y=65)
    Btn4.place(x=340, y=20)

def T3():
    # 根据表格名称获取表格
    # 打开文件
    # path + '/' +file 是文件的完整路径
    path = FilePath.get(index1=1.0, index2=tk.END)[:-1]
    data = xlrd.open_workbook(path)
    _sheetName = sheetName.get(index1=1.0, index2=tk.END)[:-1]
    print(_sheetName)
    print(_sheetName[:-5])
    _sheetDaoju = data.sheet_by_name(_sheetName)
    function_lua(_sheetDaoju)

def T4():
    Btn1.place(x=30, y=60)
    Btn2.place(x=260, y=60)
    Btn3.place(x=150, y=300)
    Btn4.place(x=150, y=300)
    sheetName.place(x=80, y=100)
    SkillTip.place(x=5, y=300)
if __name__ == '__main__':

    # 字符串定义
    luaCodeStart = "<?local slk = require 'slk' ?>\n"
    luaCodeFunction = "function Test1 takes nothing returns nothing\n"
    luaCodeFunction1 = "function Test2 takes nothing returns nothing\n"
    luaCodeID = "\t<? local obj = slk.item.afac:new '{0}'?>\n\t<?\n"
    luaCodeID2 = "\t<? local obj = slk.ability.{0}:new '{1}'?>\n\t<?\n"
    luaCodeItem = "\t\tobj.{0} = {1}\n"
    luaCodeEnd = "endfunction"

    window = tk.Tk()
    window.title('物编生成器 龙吟水上 1243391642')
    window.geometry('400x100')
    window.resizable(width=False, height=False)

    PathTip = tk.Label(window, text='文件路径', font='微软雅黑').place(x=5, y=5)
    FilePath = tk.Text(window, width=35, height=1, )
    FilePath.place(x=80, y=12)
    SkillTip = tk.Label(window, text='技能模板', font='微软雅黑')
    SkillTip.place(x=5, y=300)
    sheetName = tk.Text(window, width=35, height=1, )
    sheetName.place(x=80, y=140)
    # path = sys.path[0]
    path = sys.argv[0]
    path = path[:-12]
    # print(path + "物编表.xls")
    FilePath.insert(index=tk.INSERT, chars=path + "物编表.xlsx")

    Btn1 = tk.Button(window, text='点击生成物编道具', width=15, height=1, command=T1)
    Btn1.place(x=30, y=60)
    Btn2 = tk.Button(window, text='技能', width=15, height=1, command=T2)
    Btn2.place(x=260, y=60)
    Btn3 = tk.Button(window, text='点击生成物编技能', width=15, height=1, command=T3)
    Btn3.place(x=260, y=300)
    Btn4 = tk.Button(window, text='返回', width=5, height=1, command=T4)
    Btn4.place(x=340, y=300)

    window.mainloop()