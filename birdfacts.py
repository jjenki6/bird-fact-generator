import random

def ask():
    question = input("Would you like to get a bird fact? (y/n)")
    return (question)
facts=["Owls cannot actually turn their heads 360 they can only turn 270 degrees","Some migratory birds fly over oceans and can go days without eating or drinking or landing at all","The peregrine falcon has the highest recorded speeds of any bird in the sky but the common swift has the fastest flying speed","Chickens constantly lay eggs in the right conditions even without the presence of a rooster","Crows have very good memories and can recognize faces for many years","Homing pigeons can navigate back to a set location via earths magnetic fields rather than any other sense"]

factsgiven=[]

while(ask()!="n"):
    randomindex=random.randrange(len(facts))
    if (factsgiven in facts[randomindex]): #checks for repeats
        break
    else:
        print("\n"+facts[randomindex]+"\n")
        factsgiven=factsgiven.append(randomindex)
