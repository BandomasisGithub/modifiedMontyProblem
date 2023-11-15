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
        self.next_doors_status_index = 0
        self.user_choise_index = 0
        self.winning_door_index = 0
        self.selectable_not_removable_winning_door_index = np.empty((0,0))
        self.removable_doors_indices = np.empty((0,0))
        self.all_unchosen_doors_indices = np.empty((0,0))
        
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
                    ('removedUnchosenDoor', 6), ('removedChosenDoor', 7)])

    def monty_logic_loop(self):

        for _ in range(0, self.loop_amount):
            
            #START of initial setup (setting up a winning door and choosing a door by the user)

            self.doors_state = np.zeros((self.doors_total_switches_amount, self.door_amount))
            self.doors_status_index = 0
            self.user_choise_index = random.randint(1, self.door_amount) - 1
            self.winning_door_index = random.randint(1, self.door_amount) - 1 
            
            if self.winning_door_index != self.user_choise_index:
            
                self.doors_state[self.doors_status_index][self.winning_door_index] = self.DoorStatus.unchosenWinningDoor.value
                self.doors_state[self.doors_status_index][self.user_choise_index] = self.DoorStatus.currentChosenDoorByTheUser.value
            else:
                self.doors_state[self.doors_status_index][self.winning_door_index] = self.DoorStatus.currentChosenWinningDoorByTheUser.value
            #END of initial setup (Winning door and user chosen door is set up and check if it's the same door)
            
            
            
            

            #START of something
            #gal removint iseitu ir kitam zingsni
            #tik paduot kaip state kitoki
            
            #REIKIA PAZIURET SU VSC AR VISI REMOVABLE DOORS INDICES PAKEISTI I SELF.REMO ...
            #removable_doors_indices = np.where(self.doors_state[self.doors_status_index] == self.DoorStatus.unchosenDoor.value)[0]
            self.removable_doors_indices = np.where(self.doors_state[self.doors_status_index] == self.DoorStatus.unchosenDoor.value)[0]
            
            
            
            
            #CIA else parasyt kad kai baigis uchosen door kad galeciau chosen removint
            if self.removable_doors_indices.any():

            
                #unchosen_doors_indices = np.where(self.doors_state[self.doors_status_index] == self.DoorStatus.unchosenDoor.value)[0]
                # CIA TURI BUT IF STATEMENT kad paimtu panaikintu jau pasirinkta statusa jei vieninteles nepasirinktos durys yra
                # jau yra pasirinktos 
                self.selectable_not_removable_winning_door_index = np.where(self.doors_state[self.doors_status_index] == self.DoorStatus.unchosenWinningDoor.value)[0]
                self.all_removable_doors_indices = np.concatenate((self.removable_doors_indices, self.selectable_not_removable_winning_door_index))
                all_removable_doors_amount = self.all_removable_doors_indices.size
                removable_doors_amount = all_removable_doors_amount - 1  

                
                while all_removable_doors_amount:
                    #PAKEIST I CHOSEN
                    if (removable_doors_amount == 0 and all_removable_doors_amount == 1):
                        self.last_door_status_step_copy()
                        self.removable_doors_indices = np.where(self.doors_state[self.doors_status_index] == self.DoorStatus.chosenDoorByTheUser.value)[0]
                        removable_doors_amount = all_removable_doors_amount - 1  
                        removable_doors_amount = self.set_remove_door_status(removable_doors_amount, self.DoorStatus.removedUnchosenDoor.value)
                        
                    else:
                        self.last_door_status_step_copy()
                        
                        removable_doors_amount = self.set_remove_door_status(removable_doors_amount, self.DoorStatus.removedUnchosenDoor.value)
                    
                    all_removable_doors_amount = removable_doors_amount + 1
                    self.last_door_status_step_copy()

                    all_removable_doors_amount = self.set_chosen_door_status(all_removable_doors_amount)
        print(self.doors_state)
        return 


    # I should give status i am searching to remove 

    def set_remove_door_status(self, removable_doors_amount, removable_door_status):
        #TEORISKAI KARTOJAS SITOS DVI EILUTES IR IS PAVADININMU GAN SUNKU SUPRAST PRASME
        #GAL REIKTU ISKELT I FUNCKIJA ATSKIRA IR JOJE PAAISKINT IDEJA KODEL TAIP DAROMA
        #self.removable_doors_indices = np.empty((0,0))
        #self.selectable_not_removable_winning_door_index 
        #self.removable_doors_indices
        #self.all_unchosen_doors_indices
                                
        door_to_change_index_index = random.randint(0, removable_doors_amount-1)        
        door_to_change_index = self.removable_doors_indices[door_to_change_index_index]
        #JEIGU REIKES PADARYT KAD METHODui paduotu variable vietos set self.param galiu pet funkcijas 
        #getattr and setattr
        self.removable_doors_indices = np.delete(self.removable_doors_indices, door_to_change_index_index)[0]
        self.all_unchosen_doors_indices = np.delete(self.all_unchosen_doors_indices, door_to_change_index_index)[0]
        self.doors_state[self.next_doors_status_index][door_to_change_index] = removable_door_status

        return removable_doors_amount - 1
        


    def set_chosen_door_status(self, all_removable_doors_amount):
        #self.removable_doors_indices,
        #self.all_removable_doors_indices
        user_new_door_choise_indeces_index = random.randint(0, all_removable_doors_amount-1)
        user_new_door_choise_index = self.all_unchosen_doors_indices[user_new_door_choise_indeces_index]

        #self.user_choise_index = all_changable_doors_indices[user_new_door_choise_indeces_index]
        #self.self.winning_door_index
        
        #current_chosen_door_index = np.where(self.doors_state[self.doors_status_index] == self.DoorStatus.currentChosenDoorByTheUser.value)
        #current_chosen_winning_door_index = np.where(self.doors_state[self.doors_status_index] == self.DoorStatus.currentChosenWinningDoorByTheUser.value)[0]


        if self.winning_door_index == self.user_choise_index:
        #if current_chosen_winning_door_index.size:

            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] = self.DoorStatus.currentChosenDoorByTheUser.value
            self.doors_state[self.next_doors_status_index][self.user_choise_index] = self.DoorStatus.chosenWinningDoorByTheUser.value

        #elif self.doors_state[self.doors_status_index][user_new_door_choise_index] == self.DoorStatus.unchosenWinningDoor.value:
        elif self.winning_door_index == user_new_door_choise_index: 
            #not_current_winning_door_status == self.DoorStatus.unchosenWinningDoor.value:
            #PAKEIST JI NES GALIU PERNAUDOT FUNKCIJA ANTRAM RINKIMUI
            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] = self.DoorStatus.chosenWinningDoorByTheUser.value

        else:
            
            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] = self.DoorStatus.currentChosenDoorByTheUser.value
            self.doors_state[self.next_doors_status_index][self.user_choise_index] = self.DoorStatus.chosenDoorByTheUser.value
            #pakeist self.DoorStatus.chosenDoorByTheUser.value irgi pakeist nes antaram rinkimui ir treciam gali skirtis

        self.user_choise_index = user_new_door_choise_index
        self.removable_doors_indices = np.delete(all_changable_doors_indices, user_new_door_choise_indeces_index)[0]
        self.all_removable_doors_indices = np.delete(self.all_removable_doors_indices, user_new_door_choise_indeces_index)[0]
        #self.doors_status_index += 1

        return all_removable_doors_amount - 1
    
    def last_door_status_step_copy(self):
        # I Should fix this because there is definetly an error here


        subsequent_door_choise_step = self.doors_state[self.doors_status_index].copy()
        self.next_doors_status_index = self.doors_status_index + 1
        self.doors_state[self.next_doors_status_index] = subsequent_door_choise_step
        self.doors_status_index += 1

        return

main()
