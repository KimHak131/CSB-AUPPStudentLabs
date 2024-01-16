import pandas as pd

class SchoolAssessmentSystem:
    def __init__(self, files, parent='classes') -> None:
        self.files = files
        self.parent = parent
        self.df = None  # To store the current data frame

    def process_file(self, file_path): 
        file_extension = file_path.split('.')[-1].lower()

        # Process CSV file
        if file_extension == "csv":
            self.df = pd.read_csv(file_path)

        # Process Excel file
        elif file_extension in ['xls', 'xlsx']:
            self.df = pd.read_excel(file_path)

        # Process txt file
        elif file_extension == "txt":
            with open(file_path, "r") as file:
                lines = file.readlines()
        else:
            print(f"Unsupported file format {file_extension}")

    def transfer_data(self):
        data_transfer = pd.DataFrame()
        
        for file in self.files:
            file_path = f"{self.parent}/{file}"
            self.process_file(file_path)

            # Assuming there is a common column 'Student' for merging, update as needed
            data_transfer = pd.concat([data_transfer, self.df], ignore_index=True)

        # Save the concatenated data to a new CSV file
        data_transfer.to_csv("all_classes_concatenated.csv", index=False)    
    
    def fetch_web_data(self):
        pass

    def analyze_content(self):
        # Remove leading space from column names
        self.df.columns = [col.strip() for col in self.df.columns]

        if 'Position' not in self.df.columns:
            print("Error: 'Position' column not found in the DataFrame.")
            return None, None, None, None

        spring_data = self.df[self.df['Position'] == 'Spring']
        fall_data = self.df[self.df['Position'] == 'Fall']

        # Calculate average scores for Spring and Fall
        average_score_spring = spring_data['Score'].mean()
        average_score_fall = fall_data['Score'].mean()

        # Identify students with scholarships and full-paid status
        scholarship_students = self.df[self.df['Position'].isin(['Scholarship', 'FullPaid'])]

        # Calculate average scores for scholarship students
        average_score_scholarship = scholarship_students['Score'].mean()

        # Count the number of students who scored above 90
        n_high_achievers = self.df[self.df['Score'] >= 90].shape[0]

        return average_score_spring, average_score_fall, average_score_scholarship, n_high_achievers



    def generate_summary(self):
        pass

# Example usage
# files = ['Fall.csv', 'Spring.csv']
# assessment_system = SchoolAssessmentSystem(files, 'D:/Spring Y2/Computer Science B/CSB-AUPPStudentLabs')
# assessment_system.transfer_data()

files = ['Fall.csv']
assessment_system = SchoolAssessmentSystem(files=files)

# # # Call the process_file method on the instance as CSV file format
assessment_system.process_file("D:/Spring Y2/Computer Science B/CSB-AUPPStudentLabs/Fall.csv")

# print(assessment_system.df)

print(assessment_system.df.columns)
# Call the analyze_content method on the instance
spring_avg, fall_avg, scholarship_avg, high_achievers_count = assessment_system.analyze_content()

# Print the results
print("Average Score in Spring:", spring_avg)
print("Average Score in Fall:", fall_avg)
print("Average Score for Scholarship and FullPaid Students:", scholarship_avg)
print("Number of High Achievers:", high_achievers_count)





