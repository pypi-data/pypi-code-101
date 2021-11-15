import math
from pprint import pprint


def functionOne(initialVelocity: float, finalVelocity: float, acceleration: float, time: float):
    if initialVelocity is None:
        return round(finalVelocity - acceleration * time, 2)
    elif finalVelocity is None:
        return round(initialVelocity + acceleration * time, 2)
    elif acceleration is None:
        return round((finalVelocity - initialVelocity) / time, 2)
    elif time is None:
        return round((finalVelocity - initialVelocity) / acceleration, 2)


def functionTwo(distance: float, initialVelocity: float, finalVelocity: float, acceleration: float):
    if distance is None:
        return ((finalVelocity ** 2) - (initialVelocity ** 2)) / (2 * acceleration)
    elif initialVelocity is None:
        return math.sqrt((finalVelocity ** 2) - (2 * acceleration * distance))
    elif finalVelocity is None:
        return math.sqrt((initialVelocity ** 2) + (2 * acceleration * distance))
    elif acceleration is None:
        return ((finalVelocity ** 2) - (initialVelocity ** 2)) / (2 * distance)


def functionThree(distance: float, initialVelocity: float, acceleration: float, time: float):
    if distance is None:
        return (initialVelocity * time) + (.5 * acceleration * (time ** 2))
    elif initialVelocity is None:
        return (distance - .5 * acceleration * time ** 2) / time
    elif acceleration is None:
        return 2 * (distance - initialVelocity * time) / (time ** 2)
    elif time is None:
        temp = math.sqrt(initialVelocity ** 2 + 2 * acceleration * distance)
        valueOne = (-initialVelocity + temp) / acceleration
        valueTwo = (-initialVelocity - temp) / acceleration
        if abs(valueOne) != valueOne:
            return valueTwo
        elif abs(valueTwo) != valueTwo:
            return valueOne
        else:
            return [
                (-initialVelocity + temp) / acceleration,
                (-initialVelocity - temp) / acceleration
            ]


def findMissingValues(distance: float, initialVelocity: float, finalVelocity: float, acceleration: float, time: float):
    valuesDict = {
        "distance": distance,
        "initialVelocity": initialVelocity,
        "finalVelocity": finalVelocity,
        "acceleration": acceleration,
        "time": time
    }
    totalNone = 0
    for value in valuesDict:
        if value is None:
            totalNone += 1
        else:
            pass
    if totalNone > 2:
        raise TypeError
    else:
        # Instances for formula one
        if distance is None:
            if initialVelocity is None:
                tempVar = functionOne(None, finalVelocity, acceleration, time)
                return {
                    "initialVelocity": float(tempVar),
                    "distance": float(functionTwo(None, float(tempVar), finalVelocity, acceleration))
                }
            elif finalVelocity is None:
                tempVar = functionOne(initialVelocity=initialVelocity, finalVelocity=None, acceleration=acceleration,
                                      time=time)
                return {
                    "finalVelocity": float(tempVar),
                    "distance": float(
                        functionThree(distance=None, initialVelocity=initialVelocity, acceleration=acceleration,
                                      time=time))
                }
            elif acceleration is None:
                tempVar = functionOne(initialVelocity=initialVelocity, finalVelocity=finalVelocity, acceleration=None,
                                      time=time)
                return {
                    "acceleration": float(tempVar),
                    "distance": float(
                        functionTwo(distance=None, initialVelocity=initialVelocity, finalVelocity=finalVelocity,
                                    acceleration=tempVar))
                }
            elif time is None:
                tempVar = functionOne(initialVelocity=initialVelocity, finalVelocity=finalVelocity,
                                      acceleration=acceleration, time=None)
                return {
                    "time": float(tempVar),
                    "distance": float(
                        functionTwo(distance=None, initialVelocity=initialVelocity, finalVelocity=finalVelocity,
                                    acceleration=acceleration))
                }
            else:
                return {
                    "distance": float(
                        functionTwo(distance=None, initialVelocity=initialVelocity, finalVelocity=finalVelocity,
                                    acceleration=acceleration))
                }
        elif time is None:
            if initialVelocity is None:
                tempVar = functionTwo(distance=distance, initialVelocity=None, finalVelocity=finalVelocity,
                                      acceleration=acceleration)
                return {
                    "initialVelocity": float(tempVar),
                    "time": functionOne(initialVelocity=float(tempVar), finalVelocity=finalVelocity,
                                        acceleration=acceleration, time=None)
                }
            elif finalVelocity is None:
                tempVar = functionTwo(distance=distance, initialVelocity=initialVelocity, finalVelocity=None,
                                      acceleration=acceleration)
                return {
                    "finalVelocity": float(tempVar),
                    "time": functionOne(initialVelocity=initialVelocity, finalVelocity=float(tempVar),
                                        acceleration=acceleration, time=None)
                }
            elif acceleration is None:
                tempVar = functionTwo(distance, initialVelocity, finalVelocity, acceleration=None)
                return {
                    "acceleration": float(tempVar),
                    "time": functionOne(initialVelocity, finalVelocity, float(tempVar), None)
                }
            else:
                return {
                    "time": functionOne(initialVelocity, finalVelocity, acceleration, None)
                }
        elif finalVelocity is None:
            if initialVelocity is None:
                tempVar = functionThree(distance, None, acceleration, time)
                return {
                    "initialVelocity": float(tempVar),
                    "finalVelocity": functionOne(float(tempVar), None, acceleration, time)
                }
            elif acceleration is None:
                tempVar = functionThree(distance, initialVelocity, None, time)
                return {
                    "acceleration": float(tempVar),
                    "finalVelocity": functionOne(initialVelocity, None, float(tempVar), time)
                }
            else:
                return {
                    "finalVelocity": functionOne(initialVelocity, None, acceleration, time)
                }


def findSecondLaw(acceleration: float, mass: float, forces: float):
    noneDict = {
        acceleration: acceleration,
        mass: mass,
        forces: forces
    }
    noneVarsTotal = 0
    for x in noneDict:
        if x is None:
            noneVarsTotal += 1
        else:
            pass
    if noneVarsTotal > 1:
        raise TypeError
    else:
        if acceleration is None:
            return float(forces / mass)
        elif mass is None:
            return float(forces / acceleration)
        elif forces is None:
            return float(mass * acceleration)
        else:
            return "Unknown Error"


def compCalc(hyp: float, theta: float):
    # theta is a measure of angle in relation to the x axis
    thetaRad = math.pi * theta / 180  # converting from deg to rad
    returningDict = {
        "xComp": hyp * math.cos(thetaRad),
        "yComp": hyp * math.sin(thetaRad)
    }
    return returningDict["xComp"], returningDict["yComp"]


def sumForces(xCompf1: float, yCompf1: float, xCompf2: float, yCompf2: float):
    return {
        "xCompTotal": (xCompf1 + xCompf2),
        "yCompTotal": (yCompf1 + yCompf2)
    }


def magSolver(x: float, y: float):
    magnitude = math.sqrt((x ** 2) + (y ** 2))
    thetaRad = math.acos(x / magnitude)
    return {
        "magnitude": magnitude,
        "theta": float(thetaRad * 180 / math.pi)
    }


fpx, fpy = compCalc(20, 45)
fgx, fgy = compCalc(49, 270)
fx, fy = sumForces(fpx, fpy, fgx, fgy)["xCompTotal"], sumForces(fpx, fpy, fgx, fgy)["yCompTotal"]
ax, ay = findSecondLaw(acceleration=None, mass=5, forces=fx), findSecondLaw(acceleration=None, mass=5, forces=fy)
print(magSolver(fx, fy))
