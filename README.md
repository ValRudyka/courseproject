# About the project

This is my courseproject GUI application which predicts the bitcoin price for several intervals. User load the data from an API, then choose the interval and press "Predict" button.
After completing prediction another window opens and show you the results in different charts.

Main menu window:  
![image](https://github.com/user-attachments/assets/d59ef5a3-5e16-4a5b-b171-31c786b94aa8)

# Fetching data
Before forecasting, you need to get the data first. Click on Fetch, and a loading indicator appears, indicating that the data is being retrieved from the API. The completion of the work is indicated by replacing the indicator with a success message (Figure 2.8). 
In the event of an error, a pop-up message describing the specific error appears. The product supports caching, so the next time the process is launched, users will instantly  will receive the data instantly. Cache updates and its availability in the corresponding directory are automatically monitored. Users are able to delete  cached information using the ‘Clear cache’ button.
Main winfow after successfull fetching:
![image](https://github.com/user-attachments/assets/cb4c2ea7-3150-4fdc-a5ab-f231a641da6b)

# Forecasting prices
Then we begin forecasting our prices over a fixed period of time. In the ‘Choose the interval’ section, you can select the number of days/months/years, with a minimum value of 2 depending on the category. 
hen you click on the ‘Predict’ button, the corresponding number of days is converted, and the forecasting stage begins, which takes a long time, about 5-10 minutes. Compared to other models, this is not much, because there is also not much data from the API, and the time period is up to a year. 

![image](https://github.com/user-attachments/assets/1a0db824-6efe-4f8c-b6e4-7b679fa6f39b)

# Getting the results

After forecasting, an additional window opens that displays the results in a graphical format. The user is provided with 3 graph options: linear, dynamic, and scatter plot.

![image](https://github.com/user-attachments/assets/b4472c10-d890-444e-809a-28223499f625)

![image](https://github.com/user-attachments/assets/b8d56ca6-9ab8-4ef8-9378-09e0c48b8a28)

![image](https://github.com/user-attachments/assets/2677a6bc-cf15-46fb-990b-0efde446fd77)

# Additional features

The program provides special methods for working with the loaded data and forecasting results. The ‘Optional’ section describes the functionality of saving the downloaded data set from the API in Excel format. 
It also includes the generation of a report on the forecasting results in pdf format. 

