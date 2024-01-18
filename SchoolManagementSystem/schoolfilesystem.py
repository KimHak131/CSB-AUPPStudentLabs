
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

    def analyze_content(self):
        try:
            # Separate Scholarship and Full-paid students
            scholarship_data = self.df[self.df['Position'] == 'Scholarship']
            full_paid_data = self.df[self.df['Position'] == 'Full-paid']

            # Calculate average scores for Scholarship and Full-paid students
            scholarship_avg = scholarship_data[['COSC_221', 'COSC_241', 'INFO_652', 'LEGL_101', 'MATH_234A']].mean(axis=1).mean()
            full_paid_avg = full_paid_data[['COSC_221', 'COSC_241', 'INFO_652', 'LEGL_101', 'MATH_234A']].mean(axis=1).mean()

            # Identify top scorer in Scholarship and Full-paid categories
            top_scorer_scholarship = scholarship_data.nlargest(1, 'Total_score')[["Student_Name", "Total_score"]].to_dict(orient='records')
            top_scorer_full_paid = full_paid_data.nlargest(1, 'Total_score')[["Student_Name", "Total_score"]].to_dict(orient='records')

            # Provide the statements
            if scholarship_avg > full_paid_avg:
                self.statement = f"Average Score for Scholarship students is higher than Full-paid students."
            elif scholarship_avg < full_paid_avg:
                self.statement = f"Average Score for Full-paid students is higher than Scholarship students."
            else:
                self.statement = "Average Scores for Scholarship and Full-paid students are equal."

            print(f"Average Score for Scholarship students: {round(scholarship_avg, 4)}")
            print(f"Average Score for Full-paid students: {round(full_paid_avg, 4)}")
            print(f"Top Scorer in Scholarship category: {top_scorer_scholarship}")
            print(f"Top Scorer in Full-paid category: {top_scorer_full_paid}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def generate_summary(self):
        try:
            print("School Assessment Summary Report:")
            print("\n1. Average Scores:")
            print(f"   - Average Score for Scholarship students: {round(scholarship_avg, 4)}")
            print(f"   - Average Score for Full-paid students: {round(full_paid_avg, 4)}")
            
            print("\n2. Top Scorers:")
            print(f"   - Top Scorer in Scholarship category: {top_scorer_scholarship}")
            print(f"   - Top Scorer in Full-paid category: {top_scorer_full_paid}")

            print("\n3. Comparison:")
            print(f"   - {self.statement}")

            print("\nReport generated on:", date.today())

        except Exception as e:
            print(f"An unexpected error occurred while generating the summary: {e}")

sss = SchoolAssessmentSystem()
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
