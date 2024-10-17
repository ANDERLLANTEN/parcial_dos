from functools import total_ordering

salario_base_mensual = int(input("digite el salario mensual:"))
cargo= input("digite su cargo:")
nivel_desempeño = input("digite el nivel de desempeño:")



if cargo.lower() == "directivo":
    if nivel_desempeño == "alto":
        bonificacion = salario_base_mensual*0.2
    elif nivel_desempeño == "medio":
        bonificacion = salario_base_mensual*0.1
    elif nivel_desempeño == "bajo":
        bonificacion = print("no se otorga ninguna bonificacion")

    else:
        bonificacion = 0


if cargo.lower() == "operativo":
    if nivel_desempeño == "alto":
        bonificacion = salario_base_mensual*0.15
    elif nivel_desempeño == "medio":
        bonificacion= salario_base_mensual*0.05
    elif nivel_desempeño == "bajo":
        bonificacion =  print("no se otorga ninguna bonificacion")

    else:
        bonificacion= 0
else:
    bonificacion=0


    print("-----Resumen deL Pago-----")
    print(f"Cargo: {cargo}")
    print(f"Nivel de Desempeño: {nivel_desempeño}")
    print(f"Salario Base: {salario_base_mensual}")
    print(f"Bonificacion: {bonificacion}")
    print(f"Total a Recibir: {salario_base_mensual+bonificacion}")
    print("-----------------------------")







