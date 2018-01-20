##flask setup

pip install -r requirements.txt

##Steps in analysis
1: Read given csv file as csvreader = csv.reader("india-districts-census-2011.csv")
2: Define each function in anothor file named usecase.py and send the data their to get the value for all usercase
3: Get the data as a form of dictionary and send them to frontend
4:Display all data in the form of charts in webpages
5:The chart is created by canvasjs which will create the bar and column chart according to your value

##Project - 2011 India Census

##Usecase1:
#A graphical representation of states with low literacy rates

description : Enter a value inside the box,this value will act as a level which is set by the user . If for a particular state the total literacy rate is below that value then that state will be considered as low literacy state

##Usecase2:
#Find out most similar districts in Bihar and Tamil Nadu. Similarity can be based on any of the columns from the data

description: You can choose any parameter from the dropdown and based on that parameter it will give a graphical representation of most similar state of Bihar and Tamilnadu

##Usecase3:
#Mobile penetration vary in regions (districts or states) with high or low agricultural workers

description: You can get the value of households mobile only and agriculture workers according to state or according to district