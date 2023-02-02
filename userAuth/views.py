from django.shortcuts import render
from .apps import UserauthConfig
from django.http import HttpResponse
import pickle
import pdb
from sklearn.preprocessing import MinMaxScaler
from django.contrib import messages
from django.contrib.auth import authenticate
import numpy as np
import pandas as pd
import csv
import codecs




# Create your views here.
def login_view(request):
    return render(request,"userLogin.html")
    







def loginCheck(request):
   try:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user and redirect to the appropriate page
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login the user and redirect to the appropriate page
            return render(request,"home.html",{'user':user})
        else:
            # Display an error message
             #messages.error(request, "Invalid username or password")
              raise ValueError("please try again . . . ")
        
   except Exception as e:    
        # Render the error page 
        
         return render(request, 'login_error.html',{'e':e})
      
def process_data(request):
    try:
      if request.method == "POST":
          form_data = request.POST.copy()
          del form_data['csrfmiddlewaretoken']
          lis=[]
          time = float(request.POST['time'])
          v1 = float(request.POST['v1'])
          v2 = float(request.POST['v2'])
          v3 = float(request.POST['v3'])
          v4 = float(request.POST['v4'])
          v5 = float(request.POST['v5'])
          v6 = float(request.POST['v6'])
          v7 = float(request.POST['v7'])
          v8 = float(request.POST['v8'])
          v9 =float(request.POST['v9'])
          v10 = float(request.POST['v10'])
          v11 = float(request.POST['v11'])
          v12 = float(request.POST['v12'])
          v13 = float(request.POST['v13'])
          v14 = float(request.POST['v14'])
          v15  = float(request.POST['v15'])
          v16 = float(request.POST['v16'])
          v17 = float(request.POST['v17'])
          v18 = float(request.POST['v18'])
          v19 = float(request.POST['v19'])
          v20 = float(request.POST['v20'])
          v21 = float(request.POST['v21'])
          v22 = float(request.POST['v22'])
          v23 = float(request.POST['v23'])
          v24 = float(request.POST['v24'])
          v25 = float(request.POST['v25'])
          v26 = float(request.POST['v26'])
          v27 = float(request.POST['v27'])
          v28 = float(request.POST['v28'])
          amount = float(request.POST['amount'])
          csv_file = request.FILES['csv-file']
         
          
         
          with open('SMOTE_stackingEnsembleModel.pkl', 'rb') as f:
            model = pickle.load(f)
          
          
          
          
          lis.append(v1)
          lis.append(v2)
          lis.append(v3)
          lis.append(v4)
          lis.append(v5)
          lis.append(v6)
          lis.append(v7)
          lis.append(v8)
          lis.append(v8)
          lis.append(v9)
          lis.append(v10)
          lis.append(v11)
          lis.append(v12)
          lis.append(v13)
          lis.append(v14)
          lis.append(v15)
          lis.append(v16)
          lis.append(v17)
          lis.append(v18)
          lis.append(v19)
          lis.append(v20)
          lis.append(v21)
          lis.append(v22)
          lis.append(v23)
          lis.append(v24)
          lis.append(v25)
          lis.append(v26)
          lis.append(v27)
          lis.append(v28)
          lis.append(amount)
          
          newTrans = pd.read_csv(csv_file)
          
          data = []
          
          '''file_data = csv_file.read().decode("utf-8")	
          lines = file_data.split("\n")
          pdb.set_trace()
          for line in lines:
                data.append(line)'''
          
          '''with codecs.open(csv_file.name, 'r', encoding='utf-8') as f:
            for line in f:
                data.append(line)'''
          
          with csv_file.open(mode='r') as f:
            pdb.set_trace()
            reader = csv.reader(f)
            #data = list(reader)
            #for row in data:
                #print(row)
            for row in reader:
                data.append(row)
         
         
          table = newTrans.to_html()
          
          #text_file = open('J:/PROJECT/PROJECT WEBSITE/CreditCardValidator/userAuth/templates/home.html', 'w')
          #text_file.write(table)
          #text_file.close()
          
          '''file_path = 'J:/PROJECT/PROJECT WEBSITE/CreditCardValidator/userAuth/templates/home.html'
          with open(file_path, 'w') as f:
            # Write the content to the file
            f.write(table)'''
          
          scaler = MinMaxScaler()
          arr = np.array(lis)
          def minmax(ar):
            ar_new = (ar -ar.min()) /(ar.max() - ar.min())
            return ar_new
          
          #lis = [float(x) for x in lis]
         
          #X_scaled = scaler.fit_transform([lis])
          scaled_lis = minmax(arr)
          
          # Make prediction using model
          #prediction = model.predict(X_scaled)
          prediction = model.predict([scaled_lis])

          predictionStmt = ""
          
         
          # Process the data here
          
          if (prediction ==1):
                #predictionStmt += "Normal transaction"
                predictionStmt += "fraudulent transaction"
          else:
                #predictionStmt += "fraudulent transaction"
                predictionStmt += "Normal transaction"
          finalans = "The system has predicted it to be a",predictionStmt
         
          
<<<<<<< HEAD
          return render(request, 'results.html',{'data':data,'form_data':form_data,'lis':lis,'prediction': finalans, 'trans5':table})
=======
          return render(request, 'results.html',{'lis':arr,'scaled_lis':scaled_lis,'form_data':form_data,'lis':lis,'prediction': finalans})
>>>>>>> be860584ccfddb6e8cf9daa1854b0b604508feaa
          
    except Exception as e:
           
            pdb.set_trace()
            return render(request, 'form_error.html',{'e':e})
            