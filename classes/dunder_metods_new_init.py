class A:

    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        return instancia
        
            
    def __init__(self):
        print(self)

    def __repr__(self):
        return 'A()'
    
a  = A()
print(a)