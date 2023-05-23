import theGame
import Map

def heal(creature):
    """Heal the creature"""
    creature._hp += 3
    return True

def teleport(creature, unique)def teleport(creature, unique):
    ori = theGame.theGame()._floor.pos(creature)
    theGame.theGame()._floor._mat[ori.y][ori.x] = theGame.theGame()._floor.ground
    coord = random.choice(
    theGame.theGame()._floor._rooms).randEmptyCoord(theGame.theGame()._floor)
    theGame.theGame()._floor._mat[coord.y][coord.x] = creature
    theGame.theGame()._floor._elem[creature] = coord
    return unique
