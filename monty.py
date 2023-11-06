import pandas as pd
import numpy as np
import random
from enum import Enum
import random

def main():

    door_amount_in_game = 7
    loop_amount = 1
    #monty_logic(door_amount_in_game)
    m = montyLogic(door_amount_in_game, loop_amount)
    m.monty_logic_loop()
    
    return


class montyLogic:

    def __init__(self, door_amount, loop_amount):
        self.door_amount  = door_amount 
        #self.amount_of_winning_by_staying = np.zeros([self.door_amount])
        self.loop_amount = loop_amount
        self.doors_total_switches_amount = 1 + (self.door_amount - 2)*2
        self.doors_status_index = 0
    #class DoorStatus(Enum):
    #    unchosenDoor = 0
    #    unchosenWinningDoor = 1
    #    currentChosenWinningDoorByTheUser = 2
    #    chosenWinningDoorByTheUser = 3
    #    chosenDoorByTheUser = 4
    #    currentChosenDoorByTheUser = 5
    #    removedUnchosenDoor = 6
    #    removedChosenDoor = 7

    DoorStatus = Enum('DoorStatus', [('unchosenDoor', 0), ('unchosenWinningDoor', 1), ('currentChosenWinningDoorByTheUser', 2), 
                    ('chosenWinningDoorByTheUser', 3), ('chosenDoorByTheUser', 4),('currentChosenDoorByTheUser', 5),
                    ('removedUnchosenDoor', 6), ('removedChosenDoorr', 7)])

    def monty_logic_loop(self):
        for _ in range(0, self.loop_amount):
            
            #START of initial setup (setting up a winning door and choosing a door by the user)

            self.doors_state = np.zeros((self.doors_total_switches_amount, self.door_amount))
            self.doors_status_index = 0
            user_choise_index = random.randint(1, self.door_amount) - 1
            winning_door_index = random.randint(1, self.door_amount) - 1 
            
            if winning_door_index != user_choise_index:
            
                self.doors_state[self.doors_status_index][winning_door_index] = self.DoorStatus.unchosenWinningDoor.value
                self.doors_state[self.doors_status_index][user_choise_index] = self.DoorStatus.currentChosenDoorByTheUser.value
            else:
                self.doors_state[self.doors_status_index][winning_door_index] = self.DoorStatus.currentChosenWinningDoorByTheUser.value
            #END of initial setup (Winning door and user chosen door is set up and check if it's the same door)
            
            
            print(unchosen_doors_indices)
            print(self.doors_state)

            
            unchosen_doors_indices = np.where(self.doors_state[self.doors_status_index] == self.DoorStatus.unchosenDoor.value)
            


            if unchosen_doors_indices[0].any():
            
        



            
            
            unchosen_doors_indices = np.where(doors[doors_status_index] == DoorStatus.unchosenDoor.value)[0] 
            unchosen_winning_door_index = np.where(doors[doors_status_index] == DoorStatus.unchosenWinningDoor.value)[0]
            all_unchosen_doors_indices = np.concatenate((unchosen_doors_indices, unchosen_winning_door_index))

            all_unchosen_doors_amount = all_unchosen_doors_indices.size

            while all_unchosen_doors_amount:

                subsequent_door_choise_step = doors[doors_status_index].copy()
                next_doors_status_index = doors_status_index + 1
                doors[next_doors_status_index] = subsequent_door_choise_step

                #bb cia kazkoks 
                door_to_remove_index_index = random.randint(0, all_unchosen_doors_amount-1)
                #print("why does it delete winning door ")
                #print(doors[next_doors_status_index][all_unchosen_doors_indices[door_to_remove_index_index]])
                while doors[doors_status_index][all_unchosen_doors_indices[door_to_remove_index_index]] == DoorStatus.unchosenWinningDoor.value:
                    #print("one of the errors")
                    #print(all_unchosen_doors_amount)
                    door_to_remove_index_index = random.randint(0, all_unchosen_doors_amount-1)
                
                door_to_remove_index = all_unchosen_doors_indices[door_to_remove_index_index]

                all_unchosen_doors_indices = np.delete(all_unchosen_doors_indices, door_to_remove_index_index)
                #print(doors[next_doors_status_index][door_to_remove_index])
                doors[next_doors_status_index][door_to_remove_index] = DoorStatus.removedUnchosenDoor.value

                all_unchosen_doors_amount -= 1

                if all_unchosen_doors_amount != 0:
                    
                    #unchosen_winning_doors_index = np.where(doors[doors_status_index] == DoorStatus.unchosenWinningDoor.value)
                    #print(all_unchosen_doors_amount)
                    user_new_door_choise_indeces_index = random.randint(0, all_unchosen_doors_amount-1)
                    user_new_door_choise_index = all_unchosen_doors_indices[user_new_door_choise_indeces_index]
                    #user_new_door_choise_index = np.random.choice(all_unchosen_doors_indices)
                    #unchosen_doors_indices = np.delete(unchosen_doors_indices, user_new_door_choise_index)

                    current_chosen_door_index = np.where(doors[doors_status_index] == DoorStatus.currentChosenDoorByTheUser.value)
                    current_chosen_winning_door_by_user_index = np.where(doors[doors_status_index] == DoorStatus.currentChosenWinningDoorByTheUser.value)
                    
                    if current_chosen_winning_door_by_user_index[0].size:

                        doors[next_doors_status_index][user_new_door_choise_index] = DoorStatus.currentChosenDoorByTheUser.value
                        doors[next_doors_status_index][current_chosen_winning_door_by_user_index[0][0]] = DoorStatus.chosenWinningDoorByTheUser.value
                        all_unchosen_doors_indices = np.delete(all_unchosen_doors_indices, user_new_door_choise_indeces_index)

                        all_unchosen_doors_amount -= 1

                        #continue
                    elif doors[doors_status_index][user_new_door_choise_index] == DoorStatus.unchosenWinningDoor.value:
                        
                        doors[next_doors_status_index][user_new_door_choise_index] = DoorStatus.chosenWinningDoorByTheUser.value
                        all_unchosen_doors_indices = np.delete(all_unchosen_doors_indices, user_new_door_choise_indeces_index)
                        all_unchosen_doors_amount -= 1 
                    else:
                        
                        doors[next_doors_status_index][user_new_door_choise_index] = DoorStatus.currentChosenDoorByTheUser.value
                        doors[next_doors_status_index][current_chosen_door_index[0][0]] = DoorStatus.chosenDoorByTheUser.value
                        all_unchosen_doors_indices = np.delete(all_unchosen_doors_indices, user_new_door_choise_indeces_index)

                        all_unchosen_doors_amount -= 1

                        #continue

                doors_status_index += 1

            #now the confusing part I guess
            
            doors_status_index = next_doors_status_index
            next_doors_status_index += 1





            left_wrong_doors_indices = np.where((doors[doors_status_index] != DoorStatus.removedUnchosenDoor.value)
                                                    & (doors[doors_status_index] != DoorStatus.currentChosenDoorByTheUser.value) 
                                                    & (doors[doors_status_index] != DoorStatus.currentChosenWinningDoorByTheUser.value))[0]
            winning_door_index = np.where(doors[doors_status_index] == DoorStatus.chosenWinningDoorByTheUser.value)[0]
            #ISKYRUS CURRENT CHOSEN WINNING DOOR BY THE USER NEPARINKTAS!!!!!
            left_possible_choises_doors_indices = np.concatenate((left_wrong_doors_indices, winning_door_index))
            left_possible_choises_doors_amount = left_possible_choises_doors_indices[0].size 

            
            print(doors)



            return

    def removing_doors():
        return

    


















def monty_logic(door_amount):

    
    #DoorStatus = Enum('DoorStatus', [('unchosenDoor', 0), ('winningDoor', 1), ('chosenWinningDoorByTheUser', 2), ('chosenDoorByTheUser', 3), ('removedDoor', 4)])
    DoorStatus = Enum('DoorStatus', [('unchosenDoor', 0), ('unchosenWinningDoor', 1), ('currentChosenWinningDoorByTheUser', 2), 
                    ('chosenWinningDoorByTheUser', 3), ('chosenDoorByTheUser', 4),('currentChosenDoorByTheUser', 5),
                    ('removedUnchosenDoor', 6), ('removedChosenDoorr', 7)])
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    
    door_winning_instances = np.array([np.zeros(door_amount)])
    
    
    # Should make range number a variable maybe it issier to control

    amount_of_winning_by_staying = np.zeros([door_amount])
    amount_of_winning_by_switching = 0
    loop_amount = 1
    doors_total_switches_amount = 1 + (door_amount - 2)*2
    
    for _ in range(0, loop_amount):
          
        
        #doors = np.array([np.zeros(door_amount)])
        doors = np.zeros((doors_total_switches_amount, door_amount))
        doors_status_index = 0
        #doors to remove has 0 as a value
        
        

        user_choise_index = random.randint(1, door_amount) - 1
        winning_door_index = random.randint(1, door_amount) - 1 
        #user_choise_sequence = np.array([user_choise_index])
        
        if winning_door_index != user_choise_index:
        
            doors[doors_status_index][winning_door_index] = DoorStatus.unchosenWinningDoor.value
            doors[doors_status_index][user_choise_index] = DoorStatus.currentChosenDoorByTheUser.value
        else:
            doors[doors_status_index][winning_door_index] = DoorStatus.currentChosenWinningDoorByTheUser.value


        #This instance doenst need because there is no chosenWinningDoorByTheUser value 
        #but if i will extract function i should look at DoorStatus.chosenWinningDoorByTheUser.value 


        #GRAZINA NE INDEXUS BET BOOL VERTES !!!!!!!!
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
    
        

        if unchosen_doors_indices[0].any():
            
        



            
            
            unchosen_doors_indices = np.where(doors[doors_status_index] == DoorStatus.unchosenDoor.value)[0] 
            unchosen_winning_door_index = np.where(doors[doors_status_index] == DoorStatus.unchosenWinningDoor.value)[0]
            all_unchosen_doors_indices = np.concatenate((unchosen_doors_indices, unchosen_winning_door_index))

            all_unchosen_doors_amount = all_unchosen_doors_indices.size

            while all_unchosen_doors_amount:

                subsequent_door_choise_step = doors[doors_status_index].copy()
                next_doors_status_index = doors_status_index + 1
                doors[next_doors_status_index] = subsequent_door_choise_step

                #bb cia kazkoks 
                door_to_remove_index_index = random.randint(0, all_unchosen_doors_amount-1)
                #print("why does it delete winning door ")
                #print(doors[next_doors_status_index][all_unchosen_doors_indices[door_to_remove_index_index]])
                while doors[doors_status_index][all_unchosen_doors_indices[door_to_remove_index_index]] == DoorStatus.unchosenWinningDoor.value:
                    #print("one of the errors")
                    #print(all_unchosen_doors_amount)
                    door_to_remove_index_index = random.randint(0, all_unchosen_doors_amount-1)
                
                door_to_remove_index = all_unchosen_doors_indices[door_to_remove_index_index]

                all_unchosen_doors_indices = np.delete(all_unchosen_doors_indices, door_to_remove_index_index)
                #print(doors[next_doors_status_index][door_to_remove_index])
                doors[next_doors_status_index][door_to_remove_index] = DoorStatus.removedUnchosenDoor.value

                all_unchosen_doors_amount -= 1

                if all_unchosen_doors_amount != 0:
                    
                    #unchosen_winning_doors_index = np.where(doors[doors_status_index] == DoorStatus.unchosenWinningDoor.value)
                    #print(all_unchosen_doors_amount)
                    user_new_door_choise_indeces_index = random.randint(0, all_unchosen_doors_amount-1)
                    user_new_door_choise_index = all_unchosen_doors_indices[user_new_door_choise_indeces_index]
                    #user_new_door_choise_index = np.random.choice(all_unchosen_doors_indices)
                    #unchosen_doors_indices = np.delete(unchosen_doors_indices, user_new_door_choise_index)

                    current_chosen_door_index = np.where(doors[doors_status_index] == DoorStatus.currentChosenDoorByTheUser.value)
                    current_chosen_winning_door_by_user_index = np.where(doors[doors_status_index] == DoorStatus.currentChosenWinningDoorByTheUser.value)
                    
                    if current_chosen_winning_door_by_user_index[0].size:

                        doors[next_doors_status_index][user_new_door_choise_index] = DoorStatus.currentChosenDoorByTheUser.value
                        doors[next_doors_status_index][current_chosen_winning_door_by_user_index[0][0]] = DoorStatus.chosenWinningDoorByTheUser.value
                        all_unchosen_doors_indices = np.delete(all_unchosen_doors_indices, user_new_door_choise_indeces_index)

                        all_unchosen_doors_amount -= 1

                        #continue
                    elif doors[doors_status_index][user_new_door_choise_index] == DoorStatus.unchosenWinningDoor.value:
                        
                        doors[next_doors_status_index][user_new_door_choise_index] = DoorStatus.chosenWinningDoorByTheUser.value
                        all_unchosen_doors_indices = np.delete(all_unchosen_doors_indices, user_new_door_choise_indeces_index)
                        all_unchosen_doors_amount -= 1 
                    else:
                        
                        doors[next_doors_status_index][user_new_door_choise_index] = DoorStatus.currentChosenDoorByTheUser.value
                        doors[next_doors_status_index][current_chosen_door_index[0][0]] = DoorStatus.chosenDoorByTheUser.value
                        all_unchosen_doors_indices = np.delete(all_unchosen_doors_indices, user_new_door_choise_indeces_index)

                        all_unchosen_doors_amount -= 1

                        #continue

                doors_status_index += 1

            #now the confusing part I guess
            
            doors_status_index = next_doors_status_index
            next_doors_status_index += 1





            left_wrong_doors_indices = np.where((doors[doors_status_index] != DoorStatus.removedUnchosenDoor.value)
                                                    & (doors[doors_status_index] != DoorStatus.currentChosenDoorByTheUser.value) 
                                                    & (doors[doors_status_index] != DoorStatus.currentChosenWinningDoorByTheUser.value))[0]
            winning_door_index = np.where(doors[doors_status_index] == DoorStatus.chosenWinningDoorByTheUser.value)[0]
            #ISKYRUS CURRENT CHOSEN WINNING DOOR BY THE USER NEPARINKTAS!!!!!
            left_possible_choises_doors_indices = np.concatenate((left_wrong_doors_indices, winning_door_index))
            left_possible_choises_doors_amount = left_possible_choises_doors_indices[0].size 

            
            print(doors)
           
            while all_unchosen_doors_amount:

                subsequent_door_choise_step = doors[doors_status_index].copy()
                next_doors_status_index = doors_status_index + 1
                    

                #bb cia kazkoks 
                door_to_remove_index_index = random.randint(0, all_unchosen_doors_amount-1)
                #print("why does it delete winning door ")
                #print(doors[next_doors_status_index][all_unchosen_doors_indices[door_to_remove_index_index]])
                #iskelt sita i funkcija gal
                #pakeist while teigini
                while doors[doors_status_index][all_unchosen_doors_indices[door_to_remove_index_index]] == DoorStatus.unchosenWinningDoor.value:


                    #SITAS KEICIAS
                    door_to_remove_index_index = random.randint(0, left_possible_choises_doors_amount - 1)
                    #user_new_door_choise_indeces_index = random.randint(0, left_possible_choises_doors_amount - 1)

                    door_to_remove_index = left_possible_choises_doors_indices[door_to_remove_index_index]

                    all_unchosen_doors_indices = np.delete(all_unchosen_doors_indices, door_to_remove_index_index)
                    #print(doors[next_doors_status_index][door_to_remove_index])
                    doors[next_doors_status_index][door_to_remove_index] = DoorStatus.removedUnchosenDoor.value

                    all_unchosen_doors_amount -= 1

                    if all_unchosen_doors_amount != 0:
                        
                        #unchosen_winning_doors_index = np.where(doors[doors_status_index] == DoorStatus.unchosenWinningDoor.value)
                        #print(all_unchosen_doors_amount)
                        user_new_door_choise_indeces_index = random.randint(0, all_unchosen_doors_amount-1)
                        user_new_door_choise_index = all_unchosen_doors_indices[user_new_door_choise_indeces_index]
                        #user_new_door_choise_index = np.random.choice(all_unchosen_doors_indices)
                        #unchosen_doors_indices = np.delete(unchosen_doors_indices, user_new_door_choise_index)

                        current_chosen_door_index = np.where(doors[doors_status_index] == DoorStatus.currentChosenDoorByTheUser.value)
                        current_chosen_winning_door_by_user_index = np.where(doors[doors_status_index] == DoorStatus.currentChosenWinningDoorByTheUser.value)
                        
                        if current_chosen_winning_door_by_user_index[0].size:

                            doors[next_doors_status_index][user_new_door_choise_index] = DoorStatus.currentChosenDoorByTheUser.value
                            doors[next_doors_status_index][current_chosen_winning_door_by_user_index[0][0]] = DoorStatus.chosenWinningDoorByTheUser.value
                            all_unchosen_doors_indices = np.delete(all_unchosen_doors_indices, user_new_door_choise_indeces_index)

                            all_unchosen_doors_amount -= 1

                            #continue
                        elif doors[doors_status_index][user_new_door_choise_index] == DoorStatus.unchosenWinningDoor.value:
                            
                            doors[next_doors_status_index][user_new_door_choise_index] = DoorStatus.chosenWinningDoorByTheUser.value
                            all_unchosen_doors_indices = np.delete(all_unchosen_doors_indices, user_new_door_choise_indeces_index)
                            all_unchosen_doors_amount -= 1 
                        else:
                            
                            doors[next_doors_status_index][user_new_door_choise_index] = DoorStatus.currentChosenDoorByTheUser.value
                            doors[next_doors_status_index][current_chosen_door_index[0][0]] = DoorStatus.chosenDoorByTheUser.value
                            all_unchosen_doors_indices = np.delete(all_unchosen_doors_indices, user_new_door_choise_indeces_index)

                            all_unchosen_doors_amount -= 1

                            #continue

                    doors_status_index += 1



            return
                
            #skaiciavimus atlieku po if(skaiciavimai - 1u 2u v c c sutvarkau masyva kuris seka instances ir kiek kartu o po funkcijos naudoju ji kad suskaiciuociu tikrus procentus)
            #????????
            
            #for now, only dopercentege calculationd as long as there is U

         
            
            unchosen_doors_indices = np.where(doors_to_remove_status == DoorStatus.unchosenDoor.value)

            #Check with removed door without the switch
            #steps amount to take = 1 + (door_amount - 2)*2 except if there i s2 door because ou dont remove anything

           
 


            #Check the with the switched door
            # line below chooses random door from the unchosen door list
            #I should check if it is not empty first


            

            #Check logic percentege somehow


            if doors_to_remove_status[user_new_door_choise] == DoorStatus.winningDoor.value:
                doors_to_remove_status[user_new_door_choise] = DoorStatus.chosenWinningDoorByTheUser.value

                #Check logic percentege somehow after switch
        return 
                   


        #CHECK WITHOUT SWITCHING
        #END IF IT WOULD BE IT

    return

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
