# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 07:55:44 2020

@author: clccclcc
"""

class KNode():
    def __init__(self,data,etc=[]):
        self.data=data
        self.etc=etc
        self.parent=[]
        self.child=[]
        
    def addchild_v0(self,cnode):
        self.child.append(cnode)
        
    def addchild(self,cnode,append=True):
        # 2021.1.9 
        if append :
            self.child.append(cnode)
        else:
            self.child.insert(0,cnode)
        
    def addparent(self,pnode):
        self.parent.append(pnode)
        
    def show(self):
        print(self.data,self.etc)
            
        
class KTree():
    def __init__(self):
        pass
    def setroot(self,root):
        self.root=root
    def getroot(self):
        return self.root
    def getpath(self,end_node):
        path=[]
        path.append(end_node)
        
        try:
            while len(end_node.parent) > 0:
                # end_node=end_node.parent.pop(0)
                end_node=end_node.parent[0]
                path.insert(0,end_node)
        except:
            print('------>')
            
        return path
    
    def makelink_v0(self,parent,child):       
        parent.addchild(child)
        child.addparent(parent)
    
    def makelink(self,parent,child,append=True):
        # 2021.1.9         
        parent.addchild(child,append)        
        child.addparent(parent)

        
