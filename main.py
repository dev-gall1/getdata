import time

def dataatual():
  dia = time.strftime("%d")
  mes = time.strftime("%m")
  ano = time.strftime("%Y")
  horas = time.strftime("%H:%M:%S")
  return f"{dia}/{mes}/{ano} {horas}"