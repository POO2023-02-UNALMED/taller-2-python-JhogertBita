class Asiento:

  def __init__(self, color, precio, registro):
    self.color = color
    self.precio = precio
    self.registro = registro

  def cambiarColor(self, color):
    listaColores = ["rojo", "verde", "amarillo", "blanco", "negro"]
    if color in listaColores:
      self.color = color


class Auto:
  cantidadCreados = 0

  def __init__(self, modelo, precio, asientos, marca, motor, registro):
    self.modelo = modelo
    self.precio = precio
    self.asientos = asientos
    self.marca = marca
    self.motor = motor
    self.registro = registro

    def cantidadAsientos(self):
      numAsientos = 0
      for asiento in self.asientos:
        if asiento != None:
          numAsientos += 1
      return numAsientos

    def verificarIntegridad(self):
      for asiento in self.asientos:
        if asiento != None and asiento.registro != self.registro:
          return "Las piezas no son originales"
      if self.registro != self.motor.registro:
        return "Las piezas no son originales"
      return "Auto original"


class Motor:

  def __init__(self, numeroCilindros, tipo, registro):
    self.numeroCilindros = numeroCilindros
    self.tipo = tipo
    self.registro = registro

  def cambiarRegistro(self, registro):
    self.registro = registro

  def asignarTipo(self, tipo):
    if tipo == "electrico" or tipo == "gasolina":
      self.tipo = tipo