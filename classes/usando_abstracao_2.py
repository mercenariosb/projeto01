from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name) :
        self._name = None
        self.name = name

    @property
    @abstractmethod
    def name(self): ...
        #return self._name

    # @name.setter
    # def name(self, name): 
    #     self._name = name

class Foo(AbstractFoo):

    name = ''

    def __init__(self, name):
        super().__init__(name)
        # print('Não serve pra nada isso')

    # @property    
    # def name(self): 
    #     return self._name
       
                        # Tambem posso implementar o metodo direto na classe para chamar o "name"
                         # como fiz ali em cima apos deixar os codigos comentados
                          # mas assim voce perde o setter para criar logica


    # @name.setter
    # def name(self, name): 
    #     self._name = name

foo = Foo('Bar')
print(foo.name)