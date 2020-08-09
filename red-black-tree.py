class node:
    def __init__(self,val):
        self.data=val
        self.p ,self.r ,self.l ,self.red = None,None,None,True

class tree :
    def __init__(self):
        self.root=None
                               #          (grandparent)                  (grandparent) 
    def rotate_right(self,a):  #             x                               a
                               #       a           y   ---->          b             x
                               #   b       c                                    c       y

        x = a.p
        if x==self.root :
            self.root = a
        # adjusting grandparent
        if x.p and  x.p.l == x :
            x.p.l = a
        elif x.p and x.p.r == x :
            x.p.r = a

        a.p = x.p
        x.p = a
        if a.r :
            a.r.p = x
        x.l , a.r = a.r , x
                              #          (grandparent)
    def rotate_left(self,a):  #            x                                               a
                              #     y             a            ----->              x              b
                              #              c         b                     y           c  
        
        x = a.p
        if x==self.root :
            self.root = a
        # adjusting grand parent
        if x.p and  x.p.l == x :
            x.p.l = a
        elif x.p and x.p.r == x :
            x.p.r = a

        a.p = x.p
        x.p = a
        if a.l :
            a.l.p = x
        x.r , a.l = a.l , x

    def find(self,val): # finds where to insert the node with data = val
        # returns the parent node of our new inserted node with data = val
        # also returns the direction . for example if the new node is going to be inserted as the left child of its parent
        # the find() method will return the parent node and the word 'left'
        x=self.root
        if not x:
            return (x,'root')
        # it's searching in the tree
        else:
            while True:
                if x.data < val :
                    if x.r :
                        x=x.r
                    else:
                        return(x,'right')
                else:
                    if x.l :
                        x=x.l
                    else:
                        return(x,'left')

    def insert(self,val,is_val=True) :
        if is_val:
            x , th = self.find(val)
            if th == 'root' :
                self.root = node(val)
                self.root.red = False
                return
        
            elif th == 'left' :
                a = node(val)
                x.l = a
                a.p = x
                if x.red :
                    pp = x.p

                    if pp.l ==x :
                        if pp.r and pp.r.red :
                            pp.r.red , x.red = False , False
                            pp.red = True
                            self.insert(pp,is_val=False)

                        elif (pp.r and (not pp.r.red)) or not pp.r :
                            pp.red , x.red = True , False
                            self.rotate_right(x)
                    else:
                        if pp.l and pp.l.red :
                            pp.r.red , x.red =False , False
                            pp.red=True
                            self.insert(pp,is_val=False)
                        elif (pp.l and (not pp.l.red)) or not pp.l :
                            self.rotate_right(a)
                            self.insert(x,is_val=False)
            
            else:
                a = node(val)
                x.r = a
                a.p = x
                if x.red :
                    pp = x.p

                    if pp.r ==x :
                        if pp.l and pp.l.red :
                            pp.l.red , x.red = False , False
                            pp.red = True
                            self.insert(pp,is_val=False)

                        elif (pp.l and (not pp.l.red)) or (not pp.l) :
                            pp.red , x.red = True , False
                            self.rotate_left(x)
                    else:
                        if pp.r and pp.r.red :
                            pp.r.red , x.red =False , False
                            pp.red=True
                            self.insert(pp,is_val=False)

                        elif (pp.r and not(pp.r.red)) or not pp.r :
                            self.rotate_left(a)
                            self.insert(x,is_val=False)

        else:
            a = val
            x = a.p
            if not x :
                a.red = False
                return
            if x.r == a:
                if x.red :
                    pp = x.p

                    if pp.r ==x :
                        if pp.l and pp.l.red :
                            pp.l.red , x.red = False , False
                            pp.red = True
                            if pp == self.root :
                                pp.red=False
                                return
                            self.insert(pp,is_val=False)

                        elif pp.l and (not pp.l.red) :
                            pp.red , x.red = True , False
                            self.rotate_left(x)
                    else:
                        if pp.r and pp.r.red :
                            pp.r.red , x.red =False , False
                            pp.red=True
                            self.insert(pp,is_val=False)

                        elif pp.r and not(pp.r.red) :
                            self.rotate_left(a)
                            self.insert(x,is_val=False)
            else:
                if x.red :
                    pp = x.p

                    if pp.l ==x :
                        if pp.r and pp.r.red :
                            pp.r.red , x.red = False , False
                            pp.red = True
                            if pp == self.root:
                                pp.red=False
                                return
                            self.insert(pp,is_val=False)

                        elif pp.r and (not pp.r.red) :
                            pp.red , x.red = True , False
                            self.rotate_right(x)
                    else:
                        if pp.l and pp.l.red :
                            pp.r.red , x.red =False , False
                            pp.red=True
                            self.insert(pp,is_val=False)
                        elif pp.l and (not pp.l.red) :
                            self.rotate_right(a)
                            self.insert(x,is_val=False)
    
    def is_in_tree(self,val):
        x= self.root
        while x:
            if x.data==val :
                return('YES')
            elif x.data < val :
                x=x.r
            else:
                x=x.l
        return('NO')
    
    
    def in_order(self,x=1234):
        if x == 1234:
            x=self.root
        if not x:
            return
        self.in_order(x.l)
        print(x.data,end=' ')
        self.in_order(x.r)



if __name__ == '__main__':
    oh = tree()

    oh.insert(10)
    oh.in_order()
    print()
    oh.insert(11)
    oh.in_order()
    print()
    oh.insert(12)
    oh.in_order()
    print()
    oh.insert(13)
    oh.in_order()
    print()
    oh.insert(1)
    oh.in_order()
    print()
    oh.insert(4)
    oh.in_order()
    print()
    oh.insert(2)
    oh.in_order()
    print()
    oh.insert(18)
    oh.in_order()
    print()

    oh.in_order(oh.root)
            

            


        