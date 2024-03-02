print('Hola')

class Hola():
  def crear_saludo(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def mostrar_saludo(self):
    print(f'''Saludo:
    Hola {self.nombre}
    ''')


