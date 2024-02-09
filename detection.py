#detection

import distance
import password_changer

def attempts(passwrd,typepswd):   
              
        #This function defines if the attempts on the password are wrong and need for detection
        if passwrd != typepswd:
            attempt += 1
        else:
            print("nothing to worry abt it")

        while attempts > 3:
            detection()  


def detection(username, passwrd, typepswd):

    detect += distance(passwrd,typepswd)    
            
    #distance probablity should be more than 60% for suspisous activity 
    percentage =((detect * len(detect)) * 100)
    return percentage
    



    
    