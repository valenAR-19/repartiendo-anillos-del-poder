def distribute_rings(total_rings: int):
    
    sauron = 1
    total_rings -= sauron
    
    for men in range(2, total_rings, 2):
        for elves in range(1, total_rings, 2):
            dwarves = total_rings - men - elves
            
            return {
                "Hombres": men,
                "Elfos": elves,
                "Enanos": dwarves,
                "Sauron": sauron
            }
    
    return "No es posible distribuir los anillos de poder."

try:
    total_rings = int(
        input("Introduce el numero de anillos que quieres repartir: ")
    )
    distributed_rings = distribute_rings(total_rings)
except ValueError:
    print("Por favor, introduce un numero entero de anillos.")