class node:
    def __init__(self,val):
        self.data=val  # value of the node
        self.p ,self.r ,self.l ,self.red = None,None,None,True
        # self.p = parent node  / self.r = right child / self.l = left child / self.red = a boolean which shows that if our node is red or not
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
        # boolean variable is_val , checks if the val is a node or it's a value which we want to insert to the tree
        if is_val:
            x , th = self.find(val)  # finds the parent of our new inserted node and the direction
            if th == 'root' :
                self.root = node(val)
                self.root.red = False  # root have to be black
                return
        
            elif th == 'left' :  # we have to insert the new node as the left child of x
                a = node(val)  # our new inserted node
                x.l = a
                a.p = x
                if x.red :
                    # here we have to red nodes as parent and child 
                    pp = x.p  # grandparent of a = parent of x

                    if pp.l ==x :  # x is the left child of its parent
                        if pp.r and pp.r.red :  # it checks the right child of pp and the color of it         
                            pp.r.red , x.red = False , False
                            pp.red = True
                            self.insert(pp,is_val=False) # here we use insert as a recursive function 

                        elif (pp.r and (not pp.r.red)) or not pp.r :  # right child of pp is black or there is no right child for pp
                            pp.red , x.red = True , False
                            self.rotate_right(x)
                    else:    # x is the right child of its parent     
                        if pp.l and pp.l.red :   # it checks the left child of pp and the color of it 
                            pp.r.red , x.red =False , False
                            pp.red=True
                            self.insert(pp,is_val=False) # here we use insert as a recursive function
                        elif (pp.l and (not pp.l.red)) or not pp.l :  # right child of pp is black or there is no right child for pp
                            self.rotate_right(a)
                            self.insert(x,is_val=False)
            
            else:    # the new node which we are going to insert is the right child of x
                a = node(val)  
                x.r = a
                a.p = x
                if x.red :
                    # here we have two red nodes as parent and child
                    pp = x.p
                    # like the above elif
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

        else:  # the recursive part of insert() method
            # it examines the node val to see if its parent is red or not
            a = val  # the node we want to examine
            x = a.p  # parent of node val
            if not x : # the recursion finishing point
                # we have reached the root of our tree
                a.red = False # root have to be black
                return
            if x.r == a:  # val is the right child of its parent
                if x.red : 
                    # here we have two red nodes as parent and child
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
    
    def is_in_tree(self,val): # searchs for a node in tree
        ''' if the node is in tree : returns True
            else : returns False 
        '''
        x= self.root
        while x:
            if x.data==val :
                return('YES')
            elif x.data < val :
                x=x.r
            else:
                x=x.l
        return('NO')
    
    
    def in_order(self,x=1234): # prints in-order traversal of the tree
        ''' prints space seperated in-order traversal of the tree in one line '''
        if x == 1234:
            x=self.root
        if not x:
            return
        self.in_order(x.l)
        print(x.data,end=' ')
        self.in_order(x.r)



if __name__ == '__main__':  # just for a test :)
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
            

            


        