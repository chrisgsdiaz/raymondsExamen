import signal
import sys
import os


ans=True
while ans:
    try:
        os.system('clear')
        print ("""
    1.Suma
    2.Resta
    3.Multilicacion
    4.Division
    5.Exponente
    6.Log
    7.Seno
    8.Coseno
    9.Tangente
    10.Seno Inverso
    11.Coseno Inverso
    12.Tangente Inverso
    13.Salir
    """)
        ans=input("Que operacion deseas hacer? ")
        if ans=="1":
          print("\n Suma")
        elif ans=="2":
          print("\n Resta")
        elif ans=="3":
          print("\n Multilicacion")
        elif ans=="4":
          print("\n Division")
        elif ans=="5":
          print("\n Exponente")
        elif ans=="6":
          print("\n Log")
        elif ans=="7":
          print("\n Seno")
        elif ans=="8":
          print("\n Coseno")
        elif ans=="9":
          print("\n Tangente")
        elif ans=="10":
          print("\n Seno Inverso")
        elif ans=="11":
          print("\n Coseno Inverso")
        elif ans=="12":
          print("\n Tangente Inverso")
        elif ans=="13":
          print("\n Adios")
          ans=False
        elif ans !="":
          print("\n Opcion no valida, intenta de nuevo")
    except KeyboardInterrupt:
        print("A donde vas conejo blaz")