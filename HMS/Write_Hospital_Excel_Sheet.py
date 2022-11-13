def Write_Patients_DataBase (Pateints_DataBase) :
	myfile = open("Patients_DataBase.csv","w")
	for i in Pateints_DataBase :
		myfile.write(str(i)+";"+Pateints_DataBase[i][0]+";"+Pateints_DataBase[i][1]+";"+Pateints_DataBase[i][2]+";"+Pateints_DataBase[i][3]+";"+Pateints_DataBase[i][4]+";"+Pateints_DataBase[i][5]+";"+Pateints_DataBase[i][6]+"\n")
	myfile.close()
	
	
	
def Write_Doctors_DataBase (Doctors_DataBase) :
	myfile = open("Doctors_DataBase.csv","w")	
	for i in Doctors_DataBase :
		myfile.write(str(i)+";")
		for j in Doctors_DataBase[i] :
			myfile.write(str(j[0])+";"+j[1]+";"+j[2]+";")
		myfile.write("\n")
	
	myfile.close()