while True:
    tuumat = float(input("tuumat:"))
    if tuumat<0:
        print("ohjelma lopetetaan")
        break
    senttimetrit = tuumat*2.54
    print(f"{tuumat} on {senttimetrit} senttimetriä")
