class bottle:
    def __init__(bottle, material, volume, insulation):
        bottle.material = material
        bottle.volume = volume
        bottle.insulation = insulation

        def IsInsulated(bottle):
            if bottle.insulation == 1:
                print("The bottle is insulated.")
            else:
                print("The bottle is not insulated")


mybottle = bottle("metal", 500, 1)
bottle.IsInsulated(mybottle)
