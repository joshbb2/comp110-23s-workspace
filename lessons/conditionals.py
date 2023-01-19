"""Checks light, if green, says go."""

light: str = input("What color is the light? ")

if(light == "green"):
    print("Go!")
    print("Drive safe! Love, mom.")
else:
    if (light != "red"):
        if (light == "yellow"): 
            print("Slow down!")
        else:
            print("Go report this to the authorities.")
    else:
        print("Stop!")
print("Don't look at your phone!")