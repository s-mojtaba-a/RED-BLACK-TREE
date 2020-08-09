class node:
    def __init__(self,val):
        self.data=val
        self.p ,self.r ,self.l ,self.red = None,None,None,True

class tree :
    def __init__(self):
        self.root=None

    def rotate_right(self,a):  #             x
                               #       a           y
                               #   b       c

        x = a.p
        # adjusting grand parent
        if x.p and  x.p.l == x :
            x.p.l = a
        elif x.p and x.p.r == x :
            x.p.r = a

        a.p = x.p
        x.p = a
        if a.r :
            a.r.p = x
        x.l , a.r = a.r , x

    def rotate_left(self,a):  #            x
                              #     y             a
                              #              c         b       
        
        x = a.p
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
        x=self.root
        if not x:
            return (x,'root')

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
            a = val
            x = a.p
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



if __name__ == '__main__':
    oh = tree()

    oh.insert(10)
    oh.insert(11)
    oh.insert(12)
    oh.insert(13)

    for i in range(10,15):
        print(oh.is_in_tree(i))

            

            


        