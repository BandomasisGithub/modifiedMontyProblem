import pandas as pd
import numpy as np
import random
from enum import Enum

def main():

    door_amount_in_game = 5

    monty_logic(door_amount_in_game)
    
    return

def monty_logic(door_amount):


    #DoorStatus = Enum('DoorStatus', [('unchosenDoor', 0), ('winningDoor', 1), ('chosenWinningDoorByTheUser', 2), ('chosenDoorByTheUser', 3), ('removedDoor', 4)])
    DoorStatus = Enum('DoorStatus', [('unchosenDoor', 0), ('unchosenWinningDoor', 1), ('currentChosenWinningDoorByTheUser', 2), 
                    ('chosenWinningDoorByTheUser', 3), ('chosenDoorByTheUser', 4),('currentChosenDoorByTheUser', 5),
                    ('removedUnchosenDoor', 6), ('removedChosenDoorr', 7)])

    
    door_winning_instances = np.array([np.zeros(door_amount)])
    print(door_winning_instances)
    # Should make range number a variable maybe it issier to control

    amount_of_winning_by_staying = np.zeros([door_amount])
    amount_of_winning_by_switching = 0
    loop_amount = 1

    for _ in range(0, loop_amount):
          

        doors = np.array([np.zeros(door_amount)])
        doors_status_index = 0
        #doors to remove has 0 as a value
        
        

        user_choise_index = random.randint(1, door_amount) - 1
        winning_door_index = random.randint(1, door_amount) - 1 
        user_choise_sequence = np.array([user_choise_index])
        
        if winning_door_index != user_choise_index:
        
            doors[doors_status_index][winning_door_index] = DoorStatus.unchosenWinningDoor.value
            doors[doors_status_index][user_choise_index] = DoorStatus.currentChosenDoorByTheUser.value
        else:
            doors[doors_status_index][winning_door_index] = DoorStatus.currentChosenWinningDoorByTheUser.value
             
        #This instance doenst need because there is no chosenWinningDoorByTheUser value 
        #but if i will extract function i should look at DoorStatus.chosenWinningDoorByTheUser.value 

        winning_index = np.where(np.logical_or(doors[doors_status_index] ==  DoorStatus.unchosenWinningDoor.value,
                                                doors[doors_status_index] == DoorStatus.currentChosenWinningDoorByTheUser.value,
                                                doors[doors_status_index] == DoorStatus.chosenWinningDoorByTheUser.value,))
        staying_win_index = 0

        
        # I have to print and show percentege of unhosen chosen door percentege
        #this is full door check without removing no doors or changing them
        if np.where(doors[doors_status_index] == DoorStatus.currentChosenWinningDoorByTheUser.value)[0].size != 0:
            amount_of_winning_by_staying[staying_win_index] += 1
        
        staying_win_index += 1

        
        #This takes a wining door and marks in to array that tracks winning instances
        door_winning_instances[0][winning_index] += 1 

    
        #userChoise logic
        #user_choise_index = random.randint(1, door_amount)
        unchosen_doors_indices = np.where(doors[doors_status_index] == DoorStatus.unchosenDoor.value)
        
        
        

        
        #function here probabl

    
                

        #maybe i dont need len() and just plane unchosen_doors_indices is enough
        #maybe i have to have len()

        if unchosen_doors_indices:
            
            unchosen_doors_indices = np.where(doors[doors_status_index] == DoorStatus.unchosenDoor.value)  
            #and unchosen win
            door_to_remove_index = np.random.choice(unchosen_doors_indices)
            doors[doors_status_index][door_to_remove_index] = DoorStatus.removedUnchosenDoor.value

            unchosen_doors_indices = np.where(doors[doors_status_index] == DoorStatus.unchosenDoor.value)
        
            if unchosen_doors_indices:
                unchosen_winning_doors_index = np.where(doors[doors_status_index] == DoorStatus.unchosenWinningDoor.value)
                all
                user_new_door_choise = np.random.choice(unchosen_doors_indices)
                

            #????????

            unchosen_doors_indices = np.where(doors_to_remove_status == DoorStatus.unchosenDoor.value)

            #Check with removed door without the switch
            



            #Check the with the switched door
            # line below chooses random door from the unchosen door list
            #I should check if it is not empty first


            

            #Check logic percentege somehow


            if doors_to_remove_status[user_new_door_choise] == DoorStatus.winningDoor.value:
                doors_to_remove_status[user_new_door_choise] = DoorStatus.chosenWinningDoorByTheUser.value

                #Check logic percentege somehow after switch

                   


        #CHECK WITHOUT SWITCHING
        #END IF IT WOULD BE IT



    wSum = np.sum(door_winning_instances[0])
    door_number = 1
    
    
    print(door_winning_instances[0])

    for winning_instances in door_winning_instances[0]:
        percentege = (winning_instances/wSum) * 100
        door_number_STR = str(door_number)
        percentege_STR = str(percentege)
        print(door_number_STR + "d = " + percentege_STR + " %")
        door_number += 1

    amount_of_winning_by_staying_percentege_STR = str((amount_of_winning_by_staying[0]/loop_amount)* 100)
    print("Players percnetge of winning when switches the door = " +  "" + "%")
    print("Players percnetge of winning when he stays with the door = " + amount_of_winning_by_staying_percentege_STR + " %")
    print(amount_of_winning_by_staying[0])

    return doors





main()
