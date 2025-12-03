# # School Supply Order Tracking – Logic Challenge

# ## Objective
# Students will apply their understanding of lists, nested lists, slicing, sorting, list grouping, and logical decision-making to solve a real-world data organization problem.

# ---

# ## Scenario
# You are helping the main office organize student supply requests for the week. Each request includes:

# - Student name  
# - Item requested  
# - Quantity requested  

# All requests must be stored together in one organized system.

# ---

# ## Student Tasks (No Coding – Logic Only)

# ### 1. Create Student Requests
# Create a collection that stores information for **3 different student requests**.  
# Each student request must include:
# - Student name  
# - Item requested  
# - Quantity requested  
student_requests = [
    ["Tito", "Markers", 4],
    ["Lorenzo", "Glue Sticks", 7],
    ["Jonathan", "Folders", 2]
]

# ---

# ### 2. Identify Key Information
# From your collection:
# - Identify the **first student’s name**
# - Identify the **last student’s requested item only**
first_student_name = student_requests[0][0]
last_student_item = student_requests[-1][1]
print(first_student_name)
print(last_student_item)
# ---

# ### 3. Quantity Extraction
# Create a **separate list that contains only the quantities requested** by the students.
Quantities = [row[2] for row in Students]
print(Quantities)

# ---

# ### 4. Order Size Analysis
# Analyze the quantities:
# - If **any quantity is greater than 5**, label the order:
#   “Large order detected!”
# - Otherwise label the order:
#   “Orders within normal limits.”
if any(Quantities) >= 5:
    print("Large order detected!")
else:
    print("Orders within normal limits.") 
# ---

# ### 5. Quantity Organization
# Re-organize the quantity list from **smallest to largest** and display the final result.
Quantities.sort()
print(Quantities)
# ---

# ## Challenge Extension: Classroom Storage Grid

# You are also given a grid showing classroom supply counts:

# Classroom 1: 8, 12, 5  
# Classroom 2: 7, 3, 9  
# Classroom 3: 10, 6, 4  
classrooms = [
    [8, 12, 5],   # Classroom 1
    [7, 3, 9],    # Classroom 2
    [10, 6, 4]    # Classroom 3
]

# Answer the following:

# 1. What is the **middle number** in the second classroom’s list?

# 2. Create a new list that extracts **only the last number** from each classroom.

# 3. Explain **why this information must be stored as a nested structure instead of a single list.**
#Because each classroom has its own group of numbers. A single list would mix them together and we wouldn’t know which numbers belong to which classroom. A nested list keeps each classroom's data separate and organized.

# ---

# ## What This Assignment Tests
# - Understanding how grouped data is stored
# - Nested structure reasoning
# - Data extraction using position
# - Organizational logic
# - Real-world decision-making with quantities

# ---

# ## Submission Requirements
# - Show clear reasoning for each response.

# ---

# ## Academic Integrity
# This is an individual logic and reasoning task. All work must be your own.

# ---

# Instructor: Marvin Evins  
# Course:  AP Computer Science Principles  
