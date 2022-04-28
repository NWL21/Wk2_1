class bottle:
    def __init__(bottle, material, volume, insulation, name):
        bottle.material = material
        bottle.volume = volume
        bottle.insulation = insulation
        bottle.name = name

    def IsInsulated(bot):
        if bot.insulation:
            print(bot.name + " is insulated.")
        else:
            print(bot.name + " is not insulated")


mybottle = bottle("metal", 500, True, "mybottle")
bottle.IsInsulated(mybottle)
