student_dict = {
    "Student": ["Angela", "James", "Lily"],
    "Score": [56, 76, 98]
}

# for(key, value) in student_dict.items():
#     print(key, value)
#
import pandas

student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.Student)
