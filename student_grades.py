# A small interactive routine to illustrate loops and dictionaries

# Prompt for the number of students to evaluate
nStudents = int( input( "Enter the number of students: ") )

# Setup an empty dictionary to store all of the data
studentData = {}

# Setup the courses as a 'tuple'
courses = ( 'Physics', 'Algebra', 'Chemistry' )

# Loop to acquire the student names
for i in range( 0, nStudents ):  
    name = input( "Enter the name of student %d: " % (i+1) )

    # Define an empty list to hold the grades for the current student
    grades = []

    # Loop over the courses and acquires this student's grades
    for j in courses:
        grades.append( int( input("Enter the grade for %s: " % j ) ) )

    # Save the grades with the students name in the dictionary
    studentData[name] = grades

# Data input is now complete
print( " " )
print( "The student details input are: " )
print( studentData )

# Evaluate the pass/fail status of each student
for x, y, in studentData.items():
    status = "passed"

    # Evaluate each grade for this student, and if failing a subject, put it on the badList
    badList = []        
    for i, grade in enumerate(y):  # Need the index (i) here to access the course names
        if grade < 70 :
            status = "failed"
            badList.append( courses[i] )
    
    # Display the result of the evaluation.
    if status == 'failed' :
        print( x, status, badList )
    elif status == 'passed':
        print( x, status )

