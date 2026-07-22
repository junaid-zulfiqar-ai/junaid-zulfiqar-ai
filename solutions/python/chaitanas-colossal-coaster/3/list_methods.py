"""Functions to manage and organize queues at Chaitana's roller coaster."""

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    #Check if the person have an express ticket 
    if ticket_type == 1:
      express_queue.append(person_name)
      return express_queue
    #If they dont have a express quese , then go to normal queue
    else:
       normal_queue.append(person_name)
       return normal_queue

def find_my_friend(queue, friend_name):
    #Find the position of the friend in the queue and return it
    return queue.index(friend_name)

def add_me_with_my_friends(queue, index, person_name):
    #Insert the person at the specified index
    queue.insert(index, person_name)
    #Return the updated line
    return queue

def remove_the_mean_person(queue, person_name):
    #Kick the mean person out of the line
    queue.remove(person_name)
    #Return the updated line
    return queue

def how_many_namefellows(queue, person_name):
    #Count how many times the name appears and return that number
    return queue.count(person_name)

def remove_the_last_person(queue):
    #Remove the last person from line and return their name
    return queue.pop()

def sorted_names(queue):
    #Sort the list in alphabetical order
    queue.sort()
    #Return the sorted line
    return queue
    