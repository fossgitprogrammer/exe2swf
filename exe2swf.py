#!/usr/bin/env python
# coding: utf-8

import re,os,struct

def exe2swf(path_list):
    notexeflash=[]
    exe2swf_done=[]
    for path in path_list:
        with open(path,'rb') as f1:
            f1.seek(-8,2)
            if re.match(b'V4\x12\xfa',f1.read(4)):
                swf_l=struct.unpack('<I', f1.read(4))[0]
                f1.seek(-8-swf_l,2)
                with open(path+'.swf','wb') as f2:
                    f2.write(f1.read(swf_l))
                exe2swf_done.append(path)
            else:
                notexeflash.append(path)
    print('转换完成，返回值为不能转换的列表和已转换的列表的两个元素的元组')
    return notexeflash,exe2swf_done

def list_all(path):
    l=[]
    def recursion(path):
        if os.path.isfile(path):
            if path.endswith('exe'):
                l.append(path)
        elif os.path.isdir(path):
            tmp=[path+os.sep+x for x in os.listdir(path)]
            for i in tmp:
                recursion(i)
        return l
    return recursion(path)


if __name__ == "__main__":
    path=os.path.split(os.path.realpath(__file__))
    lexe=list_all(path)
    nots,dones=exe2swf(lexe)
    if input('需要删除已完成转换的exe文件吗？输入“yes”即可删除')=='yes':
        for i in dones:
            os.remove(i)