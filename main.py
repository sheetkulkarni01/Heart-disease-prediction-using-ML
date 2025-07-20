import pandas as pd
import numpy as np
import tkinter as tk  
from tkinter import messagebox
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn.metrics import accuracy_score
from plot_utils import styled_histogram

train = pd.read_csv('CSV_files/HeartDisease_Training Data.csv')
test = pd.read_csv('CSV_files/HeartDisease_Testing Data.csv')

win = tk.Tk()  
win.minsize(width = 350, height = 200)
win.maxsize(width = 350, height = 200)
win.title("Heart Diease Prediction") 

bp1 = 0 #Blood Pressure
cholestrol1 = 0
fh1 = 0 #Family History
bmi1 = 0
age1 = 0

target = train['Class']
data = train.drop(['Class'],axis=1)

clf = DecisionTreeClassifier()
clf = clf.fit(data,target)

prediction = clf.predict(test.drop(['Class'],axis = 1))
true = [0 if i == 'Patient doesnt have a heart disease' else 1 for i in np.array(test['Class'])]
print("Model Accuracy : ",accuracy_score(true, prediction))

bp = tk.Label(win, text = "Enter the Blood Pressure:").grid(row = 0)
cholestrol = tk.Label(win, text = "Enter the Cholestrol:\n").grid(row = 1)
fh = tk.Label(win, text = "Enter Family History(0/1):\n").grid(row = 2)
bmi = tk.Label(win, text = "Enter the BMI:\n").grid(row = 3)
age = tk.Label(win, text = "Enter the Age:\n").grid(row = 4)

bp = tk.StringVar()  
cholestrol = tk.StringVar()
fh = tk.StringVar()
bmi = tk.StringVar()
age = tk.StringVar()   

def click(): 
	print("Blood Pressure is:" + bp.get())	
	bp1 = bp.get()
	print("Cholestrol is:" + cholestrol.get())	
	cholestrol1 = cholestrol.get()
	print("Family History is:" + fh.get()) 
	fh1 = fh.get()	    
	print("BMI is:" + bmi.get())	
	bmi1 = bmi.get()
	print("Patient age is:" + age.get())	
	age1 = age.get()
	
	prediction = clf.predict(np.array([bp1,cholestrol1,fh1,bmi1,age1]).reshape(1,-1))
	if prediction[0] == 0:
		messagebox.showinfo("Prediction", "Negative: Does not have a heart disease")
	else:
		messagebox.showinfo("Prediction", "Positive: Probably Has a heart disease")
	print("Negative: Does not have a heart disease" if prediction[0] == 0 else "Positive: Probably Has a heart disease")
	
	export_graphviz(clf,out_file='tree.dot')#exports a Decision tree figure
	pos = train[train['Class'] == 1].drop(['Class'],axis = 1)#people with a heart disease
	neg = train[train['Class'] == 0].drop(['Class'],axis = 1)#people without a heart disease
	
	styled_histogram(pos['Systolic Blood Pressure'], neg['Systolic Blood Pressure'], 
                 "Systolic Blood Pressure", "Blood Pressure (mm Hg)", "BloodPressurePlot.png")
	styled_histogram(pos['Age'], neg['Age'], 
					"Age", "Age (Years)", "AgePlots.png")
	styled_histogram(pos['Cholestrol'], neg['Cholestrol'], 
					"Cholesterol Levels", "Cholesterol (mg/dL)", "CholestrolLevelsPlot.png")
	styled_histogram(pos['BMI'], neg['BMI'], 
					"Body Mass Index (BMI)", "BMI", "BMIPlot.png")
	
e1 = tk.Entry(win,textvariable = bp)
e2 = tk.Entry(win,textvariable = cholestrol)
e3 = tk.Entry(win,textvariable = fh)
e4 = tk.Entry(win,textvariable = bmi)
e5 = tk.Entry(win,textvariable = age)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

button = tk.Button(win, text = "submit", command = click).grid(column = 1, row = 15)	
	
win.mainloop()
	
       	