"""
Exercise 7:
        Write a program to calculate the BMI by accepting user input from the keyboard and check whether the user 
        comes in underweight ,normal weight or obesity by creating a class. Read the CSV files which contains player 
        data and compare your BMI with a player.Create functions for calculating BMI and check the user category.
       
            i)Get user weight in kg 
            ii)Get user height in meter
            iii) Use this formula to calculate the BMI
                    BMI = weight_of_the_user/(height_of_the_user * height_of_the_user)
            iv)Use this level to check user category
                #)Less than or equal to 18.5 is represents underweight
                #)Between 18.5 -24.9 indicate normal weight
                #)Between 25 -29.9 denotes over weight
                #)Greater than 30 denotes obese
        # Hint
            i)Create a class
            ii)Create one method to get the input 
            iiCreate one method to calculate BMI
            iii)Create one more method for checking user category
            iv)Create one method to read the CSV file using CSV reader and compare the user BMI with players BMI

We will use this script to learn Python to absolute beginners
The script is an example of BMI_Calculator implemented in Python
The BMI_Calculator: 
    # Get the weight(Kg) of the user
    # Get the height(m) of the user
    # Caculate the BMI using the formula
        BMI=weight in kg/height in meters*height in meters
"""
import csv
import os

class bmiCalculator:
    "This class calculates the BMI of the user"
    def __init__(self):
        self.weight_of_the_user = 0
        self.height_of_the_user = 0
        self.matched_player = []

    def get_input_to_calcluate_bmi(self):
        "This function gets the input from the user"
        #Getting input will be repeated until the user enters the proper input
        while True:
            print "Enter the weight of the user in Kg's"
            # Get the input from the user and check it's of correct type
            try:        
                weight_of_the_user = float(raw_input())
                # isintance will check the type of the input and returns true/false
                if isinstance(weight_of_the_user,float):
                    break 
            #If user inputs wrong type then the except will run
            except ValueError:
                print 'The value you have enteed is not a float value.Please enter the input in float value and in kilograms'  
        
        # Get the height of the user through keyboard
        while True:
            print "Enter the height of the user in Kg's"
            try:        
                self.height_of_the_user = float(raw_input())
                if isinstance(self.height_of_the_user,float):
                    break 
            except ValueError:
                print 'The value you have enteed is not a float value.Please enter the input in float value and in meters'  
            
    def calculate_bmi(self):
        "This function calculates the bmi"
        # Calculate the BMI of the user according to height and weight
        self.bmi_of_the_user = round(self.weight_of_the_user/(self.height_of_the_user * self.height_of_the_user),1)

        print 'BMI of the user is : ' , self.bmi_of_the_user

    def check_user_bmi_category(self):
        "This function checks whether the user comes under under weight, normal or obesity"    
        if self.bmi_of_the_user <= 18.5:
            print 'The user is considered as underweight'
        elif self.bmi_of_the_user > 18.5 and self.bmi_of_the_user < 24.9:
            print 'The user is considered as normal weight'
        elif self.bmi_of_the_user > 25 and self.bmi_of_the_user <= 29.9:
            print 'The user is considered as overweight'
        elif self.bmi_of_the_user >=30:
            print 'The user is considered as obese'
        else:
            print 'Check the input units. It should be in kg and meters'   

    def read_csv_file(self):
        "This functions reads the csv file and compare the BMI value with players and returns the players name"   
        filename = os.path.abspath(os.path.join('..','training',"all_players_data.csv")) 
        with open(filename,"r") as fp:
            csv_file = csv.reader(fp)
            next(csv_file)                 
            for i, row in enumerate(csv_file):
                bmi_value_in_row = row[3]            
                player_name = row[0]
                #matched_bmi_value = approx_value(player_name,bmi_value_in_row,bmi_value) 
                if float(bmi_value_in_row) == self.bmi_of_the_user:
                    self.matched_player.append({player_name:bmi_value_in_row})                       
                
            if not self.matched_player:
                print 'No matching data'
            else:
                print 'Your BMI is matching with'
                print self.matched_player 
       
# Program starts here
if __name__ == "__main__":
    # Creating an object for a class
    bmi_calculator_object = bmiCalculator()
    
    # This calling function gets the input from the user
    bmi_calculator_object.get_input_to_calcluate_bmi()     
    
    # This method calculates BMI of the user
    bmi_calculator_object.calculate_bmi()

    # This method is used to calculate the user's category
    bmi_calculator_object.check_user_bmi_category()

    # This method is used to read the text file and compare the BMI value
    bmi_calculator_object.read_csv_file()