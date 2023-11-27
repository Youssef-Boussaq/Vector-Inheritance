class Vecteur_2D :
    _count=0
    def __init__(self , x , y ):
        self.__x=x
        self.__y= y
        Vecteur_2D._count+=1
    def get_x(self):
        return self._x
    def get_y(self):
        return self.__y
    def set_x(self, new_x):
        self.__x= new_x
    def set_y(self, new_y):
        self.__y= new_y
    def Tostring(self):
        return (f"x ={self.get_x} et y = {self.get_y}")
    def Equals(self, vecteur1) :
        if vecteur1.get_x() == self.get_x() and vecteur1.get._y() == self.get_y() :
            return True
        else : 
            return False 
    def norme(self) :
        return ((self.get_x)**2+(self.get_y)**2)**0.5
class Vecteur_3D(Vecteur_2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z
    def get_z(self):
        return self.__z
    def set_z(self ,new_z):
        self.__z = new_z
    def Tostring(self):
        return super().Tostring()+(f"z={self.get_z}")
    def Equals(self, vecteur2) :
        if vecteur2.get_x() == self.get_x() and vecteur2.get._y() == self.get_y()  and self.get_z == vecteur2.get_z:
            return True
        else : 
            return False 
    def norme(self):
        return((self.get_x)**2+(self.get_y)**2 +(self.get_z)**2)**0.5
        