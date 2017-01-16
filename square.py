from rectangle import rectangle
    class square(rectangle) :
        def __init__ (self,lenhei):
            super(square,self).__init__(lenhei, 7)

        def set_lenhei(self,new_lenhei) :
            if new_lenhei>=0:
                
                self.length=new_lenhei
                self.height=new_lenhei
                if self.has_been_drawn:
                    self.draw_shape()
                    
                    
