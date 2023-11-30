import csv
import random
 
# Function to read data from the input file
def read_input_file(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return None
    
def read_data(data):
    faculty_data = {}  # (faculty_id, category) map
 
    # Skip the header line
 
    for values in data[1:]:
        faculty_id = values[0]
        category = values[1]
        category_decimal = 0.5 if category == 'x1' else 1.0 if category == 'x2' else 1.5
 
        courses = {values[i]: 1 for i in range(2,13)}
        
        # Construct the faculty data entry
        faculty_data[faculty_id] = {'category': category_decimal, 'courses': courses}
 
    return faculty_data
 
def initialize_allot_data(data):
    allot_data = {}
 
    # header = data[0]
 
    for values in data[1:]:
        faculty_id = values[0]
        allot_data[faculty_id] = []
    
    return allot_data
 
def reduce(faculty_data, faculty_id, course_name, reduction_value,faculty_allot):
    
    if(faculty_data[str(faculty_id)]['category'] != 0):
        faculty_data[str(faculty_id)]['category'] -= reduction_value
 
    for id in faculty_data.keys():
        data = faculty_data[str(id)]['courses']
        if(course_name in data.keys() and data[course_name] != 0):   
            data[course_name] -= reduction_value
            data = dict(sorted(data.items(), key=lambda item: item[1]))
            # data = sorted(data.keys())    
            faculty_data[str(id)]['courses'] = data
            # print(data)
 
    # print(faculty_id, )
    # print(course_name)
    # print(faculty_data)
    # print(faculty_allotment)
    return faculty_data
 
def check(faculty_data):
    i = 0
    for id in range(10):
        if(faculty_data[str(id+1)]['category'] != 0 ):
            i += 1
    if(i == 0):
        return True
    else:
        return False
 
def allotment(faculty_data,faculty_allotment):
    
    # faculty_allotment[faculty_id].append(course)
    if(check(faculty_data)):
        return faculty_allotment
    else:
        faculty = random.choice(list(faculty_data.keys()))
        # print(faculty,":",faculty_data[faculty]['courses'])
        load = faculty_data[faculty]['category']
        reduction_value = 0
        if(load != 0):
            for course in faculty_data[faculty]['courses'].keys():
                
                course_wt = faculty_data[faculty]['courses'][course]
                if(course_wt == 1 or course_wt == 0.5):
                    if(course_wt == 0.5):
                        faculty_allotment[faculty].append(course)
                        reduction_value = 0.5
                    else:
                        if(load == 0.5):
                            faculty_allotment[faculty].append(course)
                            reduction_value = 0.5
                        elif(load == 1 or load == 1.5):
                            faculty_allotment[faculty].append(course)
                            reduction_value = 1
                    faculty_data = reduce(faculty_data,faculty,course,reduction_value,faculty_allotment)
                    result = allotment(faculty_data,faculty_allotment)
                    if(result == None):
                        continue
                    else:
                        return result
            return None
        else:
            result = allotment(faculty_data,faculty_allotment)
            if(result == None):
                return None
            else:
                return result
    
                        
            
 
input_file_path = 'input2.csv'
input_data = read_input_file(input_file_path)
faculty_data = read_data(input_data)
faculty_allotment = initialize_allot_data(input_data)
# print(faculty_data)
final_allotment = allotment(faculty_data,faculty_allotment)
# print(final_allotment)
headers = ['faculty_id','alloted_course']
with open("./output2.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Writing headers
    for key, values in final_allotment.items():
        writer.writerow([key, ', '.join(values)])