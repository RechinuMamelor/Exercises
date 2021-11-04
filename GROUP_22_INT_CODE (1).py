import datetime
import csv   
import matplotlib.pyplot as plt
import numpy as np 


def show_Menu():
    print ("""               -MENU-
               Press 1 to parse the csv file
               Press 2 to print average download speed for Fano in August and September.
               Press 3 to plot monthly average download speed for Copenhagen and Ballerup.
               Press 4 to create a bar plot of the upload speed per date for Lolland Commune.
               Press Q to quit.
        """)


def show_Menu_afterparsing():
    print("                -Menu-")
    print("***Press 1 to parse the csv file***")
    print ("""Press 2 to print average download speed for Fano in August and September.
Press 3 to plot monthly average download speed for Copenhagen and Ballerup.
Press 4 to create a bar plot of the upload speed per month for Lolland Commune.
Press Q to quit.""")


# checking the user input so the program knows which function to call
def user_Input():
    check_File1 = 0
    #if the user is not typing a valid option this is going to repeat until he is quiting or choosing something possible
    while check_File1 == 0:
        userInput1 = (input("please enter a number "))
        if userInput1 == "1":
            print("File already parsed")
        elif userInput1 == "2":
            average_download_speed()
            show_Menu_afterparsing()
        elif userInput1 == "3":
            plot_monthly_average_download_speed()
            show_Menu_afterparsing()
        elif userInput1 == "4":
            uploas_speed_per_month()
            show_Menu_afterparsing()
        elif userInput1 == "Q" or userInput1 == "q":
            quit
            check_File1 = 1        
        else:    
            print("Please try again using a valid option ")
            show_Menu_afterparsing()
        userInput1 = "0"
#declaring the variable in which we'll add dates so we can decide in which month a date from the csv file is
month_list = [] 
#the x axis for the graph and for the bar plot
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]  
#creating the dates to help us decide if a date from csv file is in a specific month         
for i in range(0,12):
    month_list.append(str(i+1)+'-1-2018')
    month_list[i] = datetime.datetime.strptime(month_list[i],'%m-%d-%Y') 
#adding the 31 of december in the list because in the for loop was not possible 
december="12-31-2018"
date_december = datetime.datetime.strptime(december, '%m-%d-%Y')
month_list.append(date_december)
#lists for storing the values from the csv file     
date_list = []
location_list = []
download_list = []
upload_list = []
#numbers of entries values in the file so this program can work wih any file
entry_counter= 0  
#the function below helps use reading the file and storing the values 
def parse_csv_file(file_name):
    with open(file_name,'r', encoding='UTF-8') as csv_data:   #this is opening the file name given or not by the user
        csv_date_reader = csv.reader(csv_data)
        #skipping the first row ( head of the table)
        next(csv_data)  
        #adding the values in the lists
        for line in csv_date_reader:
            date_list.append(line[0])
            location_list.append(line[2]) 
            download_list.append(line[3])
            upload_list.append(line[4])
            global entry_counter
            entry_counter += 1
        #converting the dates from string into date variables   
        for x in range(entry_counter):
            date_list[x] = date_list[x].replace("/", "-", 2 )
            date_list[x] = datetime.datetime.strptime(date_list[x], '%m-%d-%Y')
    csv_data.close()        
def average_download_speed():
    download = 0 #variable for download speed
    download_counter = 0 # variable that is helping me count the number of good variables
    #I created 2 dates so we can compare and select the download speed only from august and september
    # august="7-31-2018"
    # date_august = datetime.datetime.strptime(august, '%m-%d-%Y')
    # september= "10-1-2018"
    # date_september = datetime.datetime.strptime(september, '%m-%d-%Y')
    #going through the list and checking for the searched values
    for x in range(entry_counter):
        if location_list[x] == "FanÃ¸" or location_list[x] == "Fanø" : # checking if the location is Fanø
           
            if date_list[x] >= month_list[7] and date_list[x] < month_list[9] : # checking if the records were in august or september
                
                download = download + float(download_list[x])
                download_counter += 1  
    
    #calculating the average download speed for august and september
    download = download / download_counter
    print("Average download speed is", download) 
  

def plot_monthly_average_download_speed():
    #Lists for calculating average of the each month
    average_download_speed_counter_copenhagen_list = [0,0,0,0,0,0,0,0,0,0,0,0]
    average_download_speed_copenhagen_list = [0,0,0,0,0,0,0,0,0,0,0,0]
    average_download_speed_counter_Ballerup_list = [0,0,0,0,0,0,0,0,0,0,0,0]
    average_download_speed_Ballerup_list = [0,0,0,0,0,0,0,0,0,0,0,0]

    #calculating the total download speed and number of entries
    for i in range(entry_counter):
        if location_list[i] == "Copenhagen":
            for j in range(0,12):
                if date_list[i] >= month_list[j] and date_list[i] < month_list[j+1]:
                    average_download_speed_copenhagen_list[j] = average_download_speed_copenhagen_list[j] + float(download_list[i])
                    average_download_speed_counter_copenhagen_list[j] +=1  
        if location_list[i] == "Ballerup":
            for j in range(0,12):
                if date_list[i] >= month_list[j] and date_list[i] < month_list[j+1]:
                    average_download_speed_Ballerup_list[j] = average_download_speed_Ballerup_list[j] + float(download_list[i])
                    average_download_speed_counter_Ballerup_list[j] +=1 
    #calculating the average speed of each month                
    for t in range(0,12):
        average_download_speed_copenhagen_list[t] = average_download_speed_copenhagen_list[t] / average_download_speed_counter_copenhagen_list[t]
        average_download_speed_Ballerup_list[t] = average_download_speed_Ballerup_list[t] / average_download_speed_counter_Ballerup_list[t]

    #plotting the graphs 
    plt.plot(months,average_download_speed_copenhagen_list, 'r', label= "Average download speed for Copenhagen")
    plt.plot(months,average_download_speed_Ballerup_list, 'b', label="Average download speed for Ballerup" )
    # Set the x axis label
    plt.xlabel('Months of year 2018')
    # Set the y axis label 
    plt.ylabel('average download speed')
    # Set a title of the current axes.
    plt.title('Average download speed for Copenhagen and Baleerup')
    # show a legend on the plot
    plt.legend()
    plt.xticks(rotation=45)
    # Display a figure.
    plt.show()

def uploas_speed_per_month():
    #lists for calculating the total upload speed per month and the number of entries
    average_upload_speed_counter_list = [0,0,0,0,0,0,0,0,0,0,0,0]
    average_upload_speed_list = [0,0,0,0,0,0,0,0,0,0,0,0]
    #calculating total upload speed per moth and the number of entryes
    for i in range(entry_counter):
        if location_list[i] == "Lolland":
            for j in range(0,12):
                if date_list[i] >= month_list[j] and date_list[i] < month_list[j+1]:
                    average_upload_speed_list[j] = average_upload_speed_list[j] + float(upload_list[i]) 
                    average_upload_speed_counter_list[j] += 1
    #calculating the average upload speed of each month
    for t in range(0,12):
        average_upload_speed_list[t] = average_upload_speed_list[t] / average_upload_speed_counter_list[t]
    #showing the bar    
    y_pos = np.arange(len(months))
    plt.bar(y_pos, average_upload_speed_list, align='center', alpha=1) #(alpa=opacity)
    plt.xticks(y_pos, months,rotation=30)
    plt.ylabel('Avg Upload Speed')
    plt.title('Average upload Speed per month in Lolland')
    plt.show() 


#showing the first menu               
show_Menu()


check_File = 0
Input_user = (input("please enter a number "))
while check_File == 0:
    #selecting the file
    if Input_user == "1":
        print('Press 1 again if you csv file is named "data.csv" ')
        print("Press anything else to write the name of the file ")
        userInput2 = input()
        if userInput2 == "1":
           file_name= "data.csv" 
           parse_csv_file(file_name)
        #selecting the file from the folder where the .py file is located    
        else:
            file_name = (input("Write the name of the file "))
            parse_csv_file(file_name)
        check_File = 1
    elif Input_user == "2" or Input_user == "3" or Input_user == "4":
        print("You need to parse the csv file first")
        Input_user = (input("Please try again"))
    elif Input_user == "Q" or Input_user == "q":
        quit        
    else:
        Input_user = (input("Please try again using a valid option "))
#showing the menu after parsing the file        
show_Menu_afterparsing()
user_Input()



