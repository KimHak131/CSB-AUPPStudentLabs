
#Libraries you may need:
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
# from selenium import webdriver

class SchoolAssessmentSystem:
    def __init__(self):
        self.data = None
        

    def process_file(self, file_path):           
        
        try:
            with open(file_path, 'r') as file:
                if file_path.endswith('.csv'):
                    self.data = pd.read_csv(file_path)
                elif file_path.endswith('.txt'):
                    self.data = file.read()
                else:
                    self.data = None
            if file_path.endswith('.xlsx'):
                self.data = pd.read_excel(file_path)
            
            return self.data
        
        except FileNotFoundError:
            print('File not found')


    def transfer_data(self, old_file_path, new_file_path):
        try:
            with open(new_file_path, 'a') as file:
                file.write(str(self.process_file(old_file_path)))
        except UnicodeDecodeError:
            print('File not found')
    
    def fetch_web_data(self, url):
        # Open the URL and read the HTML content
        response = urllib.request.urlopen(url)
        html_content = response.read()

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

    def analyze_content(self, file_path):
        try:
            self.df = self.process_file(file_path)

            # Separate Scholarship and Full-paid students
            scholarship_data = self.df[self.df['Position'] == 'Scholarship']
            full_paid_data = self.df[self.df['Position'] == 'Full-paid']

            # Calculate average scores for Scholarship and Full-paid students
            scholarship_avg = scholarship_data[['COSC_221', 'COSC_241', 'INFO_652', 'LEGL_101', 'MATH_234A']].mean(axis=1).mean()
            full_paid_avg = full_paid_data[['COSC_221', 'COSC_241', 'INFO_652', 'LEGL_101', 'MATH_234A']].mean(axis=1).mean()

            # Identify top scorer in Scholarship and Full-paid categories
            top_scorer_scholarship = scholarship_data.nlargest(1, 'MATH_234A')[["Student_Name", "MATH_234A", 'Position']].to_dict(orient='records')
            top_scorer_full_paid = full_paid_data.nlargest(1, 'MATH_234A')[["Student_Name", "MATH_234A", 'Position']].to_dict(orient='records')

            return {
                "total_average": (scholarship_avg + full_paid_avg) / 2,
                "subject_averages": self.df[['COSC_221', 'COSC_241', 'INFO_652', 'LEGL_101', 'MATH_234A']].mean(),
                "class_subject_averages": self.df.groupby('Position')[['COSC_221', 'COSC_241', 'INFO_652', 'LEGL_101', 'MATH_234A']].mean(),
                "highest_average_each_position": [top_scorer_scholarship, top_scorer_full_paid]
            }

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def generate_summary(self, analysis_data):
        try:
            if analysis_data is None:
                print("Cannot generate summary. Analysis data is None.")
                return

            print("School Assessment Summary Report:")

            # Overall Analysis
            print("\n1. Overall Analysis:")
            print(f"   - Total Grade Average: {round(analysis_data['total_average'], 4)}")

            # Subject-wise Analysis
            print("\n2. Subject-wise Analysis:")
            for subject, average in analysis_data['subject_averages'].items():
                print(f"   - {subject}: {round(average, 4)}")

            # Class-wise Analysis
            print("\n3. Class-wise Analysis:")
            for position, averages in analysis_data['class_subject_averages'].iterrows():
                print(f"   - {position}: {averages.to_dict()}")

            # Top Scorer in Each Position
            print("\n4. Top Scorer in Each Position:")
            for record in analysis_data['highest_average_each_position']:
                print(f"   - Position: {record[0]['Position']}, Top Scorer: {record[0]['Student_Name']} (Score: {record[0]['MATH_234A']})")


        except Exception as e:
            print(f"An unexpected error occurred while generating the summary: {e}")


sss = SchoolAssessmentSystem()
analysis_data = sss.analyze_content('D:/Spring Y2/Computer Science B/CountEachLetter/CSB-AUPPStudentLabs/SchoolManagementSystem/all_classes_concatenated.csv')

# sss.transfer_data('D:/Spring Y2/Computer Science B/CountEachLetter/CSB-AUPPStudentLabs/SchoolManagementSystem/Spring.csv', 'D:/Spring Y2/Computer Science B/CountEachLetter/CSB-AUPPStudentLabs/SchoolManagementSystem/bothsms.csv')

# print(sss.fetch_web_data('https://www.janison.com/resources/post/a-guide-to-5-school-assessment-types-and-their-key-purposes/'))
# Analyze content & display result area
# Sample of Output:
"""
School Assessment Summary Report:

1. Overall Performance of Student A:
   - Average score: 85.5
   - Top-performing class: Grade 10B

2. Subject-wise Analysis:
   - Mathematics: Improved by 10% compared to the last assessment.
   - Science: Consistent performance across all classes.

3. Notable Observations:
   - Grade 8A shows a significant improvement in English proficiency.

4. Web Data Insights:
   - Online participation: 95% of students accessed assessment resources online.

5. Recommendations:
   - Consider additional support for Grade 9B in Mathematics.

Report generated on: 2024-01-14
"""
