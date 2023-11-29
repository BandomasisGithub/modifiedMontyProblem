import pandas as pd
import numpy as np
import random
from enum import Enum
import random

def main():

    door_amount_in_game = 6
    loop_amount = 1
    m = montyLogic(door_amount_in_game, loop_amount)
    m.monty_logic_loop()
    
    return


class montyLogic:

    def __init__(self, door_amount, loop_amount):
        self.door_amount  = door_amount 
        self.loop_amount = loop_amount
        self.doors_total_switches_amount = 1 + (self.door_amount - 2)*2
        self.doors_status_index = 0
        self.next_doors_status_index = 0
        self.user_choise_index = 0
        self.winning_door_index = 0
        self.changeable_doors_amount = 0
        self.removable_doors_amount = 0
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

            self.removable_doors_indices = np.where(self.doors_state[self.doors_status_index] == self.DoorStatus.unchosenDoor.value)[0]

            if self.removable_doors_indices.any():
                
                if self.winning_door_index != self.user_choise_index:
                    
                    self.selectable_not_removable_winning_door_index = np.where(self.doors_state[self.doors_status_index] == self.DoorStatus.unchosenWinningDoor.value)[0]
                    self.all_unchosen_doors_indices = np.concatenate((self.removable_doors_indices, self.selectable_not_removable_winning_door_index))
                    self.changeable_doors_amount = self.all_unchosen_doors_indices.size
                    self.removable_doors_amount = self.changeable_doors_amount - 1  
                else:
                    self.all_unchosen_doors_indices = self.removable_doors_indices
                    self.changeable_doors_amount = self.all_unchosen_doors_indices.size - 1
                    self.removable_doors_amount = self.changeable_doors_amount
          
                print("Initial amounts")
                print(self.changeable_doors_amount)
                print(self.removable_doors_amount)
                print(self.doors_state)
                print("")

                while self.changeable_doors_amount:
                    
                    self.last_door_status_step_copy()
                    if (self.removable_doors_amount == 0 and self.changeable_doors_amount == 1):
                        #self.last_door_status_step_copy()
                        print("What the duck")
                        self.removable_doors_indices = np.where(self.doors_state[self.doors_status_index] == 
                                                                self.DoorStatus.chosenDoorByTheUser.value)[0]
                    
                    self.set_remove_door_status(self.DoorStatus.removedUnchosenDoor.value)
                    print("AFTER remove")
                    print(self.changeable_doors_amount)
                    print(self.removable_doors_amount)
                    print(self.doors_state)
                    print("")

                    #self.changeable_doors_amount = self.removable_doors_amount + 1
                    self.last_door_status_step_copy()
                    self.set_chosen_door_status()
                    print("AFTER change")
                    print(self.changeable_doors_amount)
                    print(self.removable_doors_amount)
                    print(self.doors_state)
                    print("")

        #print(self.doors_state)
        return 


    # I should give status i am searching to remove 

    def set_remove_door_status(self, removable_door_status):
        door_to_change_index_index = random.randint(0, self.removable_doors_amount-1)        
        door_to_change_index = self.removable_doors_indices[door_to_change_index_index]
        self.removable_doors_indices = np.delete(self.removable_doors_indices, door_to_change_index_index)
        self.all_unchosen_doors_indices = np.delete(self.all_unchosen_doors_indices, door_to_change_index_index)
        self.doors_state[self.next_doors_status_index][door_to_change_index] = removable_door_status
        self.changeable_doors_amount = self.changeable_doors_amount - 1
        self.removable_doors_amount = self.removable_doors_amount - 1
        
        return 
        


    def set_chosen_door_status(self):
        #print(self.changeable_doors_amount)
        #print(self.doors_state)
        user_new_door_choise_indeces_index = random.randint(0, self.changeable_doors_amount-1)
        user_new_door_choise_index = self.all_unchosen_doors_indices[user_new_door_choise_indeces_index]

        if self.winning_door_index == self.user_choise_index:

            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] = self.DoorStatus.currentChosenDoorByTheUser.value
            self.doors_state[self.next_doors_status_index][self.user_choise_index] = self.DoorStatus.chosenWinningDoorByTheUser.value
            #self.removable_doors_indices = np.delete(self.removable_doors_indices, user_new_door_choise_indeces_index)
            
        elif self.winning_door_index == user_new_door_choise_index: 

            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] = self.DoorStatus.currentChosenDoorByTheUser.value
            self.doors_state[self.next_doors_status_index][self.user_choise_index] = self.DoorStatus.chosenDoorByTheUser.value
            self.all_unchosen_doors_indices = np.delete(self.removable_doors_indices, user_new_door_choise_indeces_index)
            self.user_choise_index = user_new_door_choise_index
            self.changeable_doors_amount = self.changeable_doors_amount - 1

            return
        else:
            
            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] = self.DoorStatus.currentChosenDoorByTheUser.value
            self.doors_state[self.next_doors_status_index][self.user_choise_index] = self.DoorStatus.chosenDoorByTheUser.value
            #self.removable_doors_indices = np.delete(self.removable_doors_indices, user_new_door_choise_indeces_index)

        
        self.removable_doors_indices = np.delete(self.removable_doors_indices, user_new_door_choise_indeces_index)
        self.all_unchosen_doors_indices = np.delete(self.all_unchosen_doors_indices, user_new_door_choise_indeces_index)
        self.user_choise_index = user_new_door_choise_index
        self.changeable_doors_amount = self.changeable_doors_amount - 1
        self.removable_doors_amount = self.removable_doors_amount - 1

        return 
    

    def last_door_status_step_copy(self):

        subsequent_door_choise_step = self.doors_state[self.doors_status_index].copy()
        #in theory next door status index variable isnt necesary maybe leave it for clarity
        self.next_doors_status_index = self.doors_status_index + 1
        self.doors_state[self.next_doors_status_index] = subsequent_door_choise_step
        self.doors_status_index += 1

        return

main()
