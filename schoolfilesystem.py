import pandas as pd
#Libraries you may need:
# import csv, collections, dictionary, (pandas as pd), urlopen, etc..

#classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self):
        self.data = None
    def process_file(self, file_path): 
        file_extension = file_path.split('.')[-1].lower()
        
        #Process CSV file
        if file_extension == "csv":
            self.data = pd.read_csv(file_path) 

        # Process Excel file
        elif file_extension == ['xls', 'xlsx']:
            self.data = pd.read_excel(file_path)
            
        # Process txt file
        elif file_extension == "txt":
            with open(file_path, "r") as file:
                lines = file.readlines
        else:
            print(f"Unsupported file formate {file_extension}")

    def transfer_data(self):
        pass
    def fetch_web_data(self):
        pass
    def analyze_content(self):
        pass
    def generate_summary(self):
        pass

# Analyze content & display result area
# Create an instance of the SchoolAssessmentSystem class
assessment_system = SchoolAssessmentSystem()

# Call the process_file method on the instance as CSV file format
assessment_system.process_file(r"D:/Spring Y2/Computer Science B/CSB-AUPPStudentLabs/data_107326465.csv")

print(assessment_system.data)
