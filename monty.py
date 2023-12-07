import pandas as pd
import numpy as np
from attrs import define, field
import random
from enum import Enum
import random

def main():

    door_amount_in_game = 10
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
        self.changeable_doors_indices = np.empty((0,0))
        
    #class DoorStatus(Enum):
    #    unchosenDoor = 0
    #    unchosenWinningDoor = 1
    #    currentChosenWinningDoorByTheUser = 2
    #    chosenWinningDoorByTheUser = 3
    #    chosenDoorByTheUser = 4
    #    currentChosenDoorByTheUser = 5
    #    removedDoor = 6
    #    removedChosenDoor = 7

    DoorStatus = Enum('DoorStatus', [('unchosenDoor', 0), ('unchosenWinningDoor', 1), ('currentChosenWinningDoorByTheUser', 2), 
                    ('chosenWinningDoorByTheUser', 3), ('chosenDoorByTheUser', 4),('currentChosenDoorByTheUser', 5),
                    ('removedDoor', 6)])

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
                    self.changeable_doors_indices = np.concatenate((self.removable_doors_indices, self.selectable_not_removable_winning_door_index))
                    self.changeable_doors_amount = self.changeable_doors_indices.size
                    self.removable_doors_amount = self.changeable_doors_amount - 1  
                else:
                    self.changeable_doors_indices = self.removable_doors_indices
                    self.changeable_doors_amount = self.changeable_doors_indices.size
                    self.removable_doors_amount = self.changeable_doors_amount

                while self.changeable_doors_amount:
                    
                    self.last_door_status_step_copy()
                    if (self.removable_doors_amount == 0 and self.changeable_doors_amount == 1):

                        self.set_remove_unchosen_door_status()
                        self.last_door_status_step_copy()
                        self.set_chosen_for_unchosen_door_status()

                        break

                    elif(self.removable_doors_amount == 1 and self.changeable_doors_amount == 1):
                        self.set_remove_for_unchosen_door_status()
                        self.last_door_status_step_copy()
                        self.set_chosen_door_status()
                       
                        break

                    self.set_remove_for_unchosen_door_status()
                    self.last_door_status_step_copy()
                    self.set_chosen_for_unchosen_door_status()
        print(self.doors_state)
        return 


    def set_remove_for_unchosen_door_status(self):
        door_to_remove_index_index = random.randint(0, self.removable_doors_amount-1)        
        door_to_remove_index = self.removable_doors_indices[door_to_remove_index_index]
        self.removable_doors_indices = np.delete(self.removable_doors_indices, door_to_remove_index_index)
        self.changeable_doors_indices = np.delete(self.changeable_doors_indices, door_to_remove_index_index)
        self.doors_state[self.next_doors_status_index][door_to_remove_index] = self.DoorStatus.removedDoor.value
        self.changeable_doors_amount = self.changeable_doors_amount - 1
        self.removable_doors_amount = self.removable_doors_amount - 1
        
        return 
        


    def set_chosen_for_unchosen_door_status(self):

        user_new_door_choise_indeces_index = random.randint(0, self.changeable_doors_amount-1)
        user_new_door_choise_index = self.changeable_doors_indices[user_new_door_choise_indeces_index]

        if self.winning_door_index == self.user_choise_index:

            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] = self.DoorStatus.currentChosenDoorByTheUser.value
            self.doors_state[self.next_doors_status_index][self.user_choise_index] = self.DoorStatus.chosenWinningDoorByTheUser.value
            
        elif self.winning_door_index == user_new_door_choise_index: 

            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] = self.DoorStatus.currentChosenWinningDoorByTheUser.value
            self.doors_state[self.next_doors_status_index][self.user_choise_index] = self.DoorStatus.chosenDoorByTheUser.value
            self.user_choise_index = user_new_door_choise_index
            self.changeable_doors_amount = self.changeable_doors_amount - 1

            return
        else:
            
            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] = self.DoorStatus.currentChosenDoorByTheUser.value
            self.doors_state[self.next_doors_status_index][self.user_choise_index] = self.DoorStatus.chosenDoorByTheUser.value
        
        self.removable_doors_indices = np.delete(self.removable_doors_indices, user_new_door_choise_indeces_index)
        self.changeable_doors_indices = np.delete(self.changeable_doors_indices, user_new_door_choise_indeces_index)
        self.user_choise_index = user_new_door_choise_index
        self.changeable_doors_amount = self.changeable_doors_amount - 1
        self.removable_doors_amount = self.removable_doors_amount - 1

        return 
    
    def set_remove_unchosen_door_status(self):
        
        self.removable_doors_indices = np.where(self.doors_state[self.doors_status_index] == 
                                                                self.DoorStatus.chosenDoorByTheUser.value)[0]
        door_to_remove_index = np.random.choice(self.removable_doors_indices)
        self.doors_state[self.next_doors_status_index][door_to_remove_index] = self.DoorStatus.removedDoor.value
        
        return

    def set_chosen_door_status(self):
        print("w")
        print(self.doors_state)
        self.changeable_doors_indices = np.where(self.doors_state[self.doors_status_index] != 
                                                self.DoorStatus.removedDoor.value)[0]
        

        
        while True:

            user_new_door_choise_index = np.random.choice(self.changeable_doors_indices)
            print(user_new_door_choise_index )
            if(self.doors_state[self.next_doors_status_index][user_new_door_choise_index] != self.DoorStatus.currentChosenDoorByTheUser.value or 
            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] != self.currentChosenWinningDoorByTheUser.value):

                break
        #Ismeta klaida jei peasirenka index 5 kuris yra esamas dabar
        if self.winning_door_index == self.user_choise_index:

            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] = self.DoorStatus.currentChosenDoorByTheUser.value
            self.doors_state[self.next_doors_status_index][self.user_choise_index] = self.DoorStatus.chosenWinningDoorByTheUser.value
            
        elif self.winning_door_index == user_new_door_choise_index: 

            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] = self.DoorStatus.currentChosenWinningDoorByTheUser.value
            self.doors_state[self.next_doors_status_index][self.user_choise_index] = self.DoorStatus.chosenDoorByTheUser.value
            self.user_choise_index = user_new_door_choise_index

        else:
            
            self.doors_state[self.next_doors_status_index][user_new_door_choise_index] = self.DoorStatus.currentChosenDoorByTheUser.value
            self.doors_state[self.next_doors_status_index][self.user_choise_index] = self.DoorStatus.chosenDoorByTheUser.value

        self.user_choise_index = user_new_door_choise_index

        return

    def last_door_status_step_copy(self):

        subsequent_door_choise_step = self.doors_state[self.doors_status_index].copy()
        #in theory next door status index variable isnt necesary maybe leave it for clarity
        self.next_doors_status_index = self.doors_status_index + 1
        self.doors_state[self.next_doors_status_index] = subsequent_door_choise_step
        self.doors_status_index += 1

        return

main()
