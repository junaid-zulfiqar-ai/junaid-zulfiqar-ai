"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    rounded_scores = []

    for score in student_scores:
        rounded_scores.append(round(score))

    return rounded_scores  
  
def count_failed_students(student_scores):
    # 1. Start our tally at zero 
    failed_count = 0

    # 2. Loop through every score
    for score in student_scores:
        # 3. Check if the score is a failing grade 
        if score <= 40:
            # 4. If it is, add 1 to our tally
            failed_count +=1

    # 5. Return the final tally after the loop finishes
    return failed_count        


def above_threshold(student_scores, threshold):
    # 1. Create an empty list for the best scores
    top_scores = []

    # 2. Loop through all the scores
    for score in student_scores:
        # 3. Check if the score hits or beats the threshold
        if score >= threshold:
            # 4. If it does, add it to our new list
            top_scores.append(score)

    # 5. Return the newly built list
    return top_scores      

  
def letter_grades(highest):
    #1 . Calculate the size of each grad tier
    step = (highest - 40) // 4

    # 2. Create an empty list for the thresholds
    thresholds = []

    # 3. Loop exactly 4 times (i will be 0, then 1, then 2, then3)
    for i in range(4):
        # 4. Calculate the threshold and add it to the list 
        thresholds.append(41 + (i * step))

    # 5. Return the lst of 4 lower bounds 
    return thresholds    
   

def student_ranking(student_scores, student_names):
    #1 .Create an empty list for the final formatted strings
    rankings = []

    # 2. Loop through the names, grabbing both the index and the name
    for index, name in enumerate(student_names):

       # 3. Calculate the rank (index + 1)
       rank = index + 1

       # 4. Use the index to pull the matching score from the other list 
       score = student_scores[index]

       # 5. Build the string and append it to our list
       rankings.append(f"{rank}. {name}: {score}")

    # 6. Return the completed scoreboard
    return rankings       


def perfect_score(student_info):
    # 1. Loop through the main list.
    # 'student' will be a list like ["Tony", 85]
    for student in student_info:

        # 2. Check the score, which is always at index 1 of the inner list
        if student[1] == 100:

            # 3. If it's 100, return the student's list immediately.
            # This instantly stops the loop exits the function!
            return student 

    # 4. If the loop finishes checking everyone and never hits the return 
    # above, it means no one got a 100. So, we return an empty list.
    return []    