
class Carro:
    def __init__(self, request):
        self.request = request
        self.session=request.session
        carro = self.session.get("carro")
        
        if not carro:
            carro = self.session["carro"]={}

        self.carro = carro
           

    def agregar(self , producto):
        if (str(producto.cod_producto) not in self.carro.keys()):
            self.carro[producto.cod_producto]={
                "id" : producto.cod_producto,
                "nombre": producto.descripcion,
                "cantidad": 1,
                "precio": producto.precio

            }
            
        else:
            
            for key , value in self.carro.items():
              
                if key == str(producto.cod_producto):
                    print('Agrege un producto')
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]= value["precio"] * value["cantidad"]
                    break
            
        self.guardar_carro()


    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto.cod_producto =str(producto.cod_producto)
        if producto.cod_producto in self.carro:
            del self.carro[producto.cod_producto]
            self.guardar_carro()

    def restar_productos(self, producto):
        for key , value in self.carro.items():
            if key == str(producto.cod_producto):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]= value["precio"] - producto.precio
                if value["cantidad"]<1:
                    self.eliminar(producto)
                    
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True