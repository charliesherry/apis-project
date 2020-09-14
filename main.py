import sys
import argparse
import Functions.funciones as fu


def main():   
    args = fu.parse()
    nombre = args.nombre
    plata = args.Plataforma
    juego = args.Juego
    reg = args.Region
    print(args)
    print(f"Hola {nombre} bienvenido al mundo de los videojuegos")
    if plata:
        return fu.platforms(plata)
    elif juego:
        return fu.gamestatistics(juego)
    elif reg:
        return fu.regionsales(reg)

if __name__ == "__main__":
    main()


nas= 0.38856721034870645
eus = 0.23253655793025874
jps= 0.06265185601799775
print(f"The average sales (in millions) for North America is {nas}")
print(f"The average sales (in millions) for Europe is {eus}")
print(f"The average sales (in millions) for Japan is {jps}")