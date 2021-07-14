# -*- coding: utf-8 -*-
"""

William Duong
Mon July 12, 2021
wpduong@gmail.com

"""

class Patient:
	def __init__ (self, cwid, status, patientType = ''):
		"""Initialize class data members"""
		self.cwid = cwid
		self.status = status
		self.patientType = patientType


def readInCompliance(listOfPatients):
	"""Read in PNC Data"""
	with open("compliance.txt", "r") as myFile:
		first_line = myFile.readline()
		del first_line

		for line in myFile:
			myLine = line.split(',')
			campusId = myLine[1].strip('"')
			currstatus = myLine[5]

			myPatient = Patient(campusId, currstatus)
			listOfPatients.append(myPatient)


def readInEmployees(listOfPatients):
	"""Read in employee extract"""
	with open("employee.txt", "r") as myFile:
		first_line = myFile.readline()
		del first_line

		for line in myFile:
			myLine = line.split('|')
			
			for patient in listOfPatients:
				if myLine[0] == patient.cwid:
					patient.patientType = myLine[21]


def readInStudents(listOfPatients):
	"""Read in student extract"""
	with open("student.txt", "r") as myFile:
		first_line = myFile.readline()
		del first_line

		for line in myFile:
			myLine = line.split('|')
			
			for patient in listOfPatients:
				if (myLine[0] == patient.cwid) and (patient.patientType == ""):
					patient.patientType = myLine[45]


def readInNonState(listOfPatients):
	"""Read in non-state extract"""
	with open("nonstate.txt", "r") as myFile:
		first_line = myFile.readline()
		del first_line

		for line in myFile:
			myLine = line.split('|')
			
			for patient in listOfPatients:
				if (myLine[0] == patient.cwid) and (patient.patientType == ""):
					patient.patientType = myLine[9]


def countCompliance(listOfPatients, complianceDictionary):
	"""Count number for each category"""
	for patient in listOfPatients:
		if patient.status == '"Compliant with Standard Requirements"':
			if patient.patientType == "Faculty":
				complianceDictionary["cFaculty"] += 1
			elif patient.patientType == "Staff":
				complianceDictionary["cStaff"] += 1
			elif patient.patientType == "Student":
				complianceDictionary["cStudents"] += 1
			elif patient.patientType == "ASC":
				complianceDictionary["cASC"] += 1
			elif patient.patientType == "ASI":
				complianceDictionary["cASI"] += 1
			else:
				complianceDictionary["cUnknown"] += 1
		if patient.status == '"Awaiting Review"':
			if patient.patientType == "Faculty":
				complianceDictionary["arFaculty"] += 1
			elif patient.patientType == "Staff":
				complianceDictionary["arStaff"] += 1
			elif patient.patientType == "Student":
				complianceDictionary["arStudents"] += 1
			elif patient.patientType == "ASC":
				complianceDictionary["arASC"] += 1
			elif patient.patientType == "ASI":
				complianceDictionary["arASI"] += 1
			else:
				complianceDictionary["arUnknown"] += 1
		if not (patient.status == '"Compliant with Standard Requirements"' or patient.status == '"Awaiting Review"'):
			if patient.patientType == "Faculty":
				complianceDictionary["ncFaculty"] += 1
			elif patient.patientType == "Staff":
				complianceDictionary["ncStaff"] += 1
			elif patient.patientType == "Student":
				complianceDictionary["ncStudents"] += 1
			elif patient.patientType == "ASC":
				complianceDictionary["ncASC"] += 1
			elif patient.patientType == "ASI":
				complianceDictionary["ncASI"] += 1
			else:
				complianceDictionary["ncUnknown"] += 1


def printCompliance(listOfPatients, complianceDictionary):
	"""Output compliance numbers"""
	print("Compliant Faculty: {}".format(complianceDictionary["cFaculty"]))
	print("Compliant Staff: {}".format(complianceDictionary["cStaff"]))
	print("Compliant Students: {}".format(complianceDictionary["cStudents"]))
	print("Compliant ASC: {}".format(complianceDictionary["cASC"]))
	print("Compliant ASI: {}".format(complianceDictionary["cASI"]))
	print("Compliant Unknown: {}\n".format(complianceDictionary["cUnknown"]))
	print("Awaiting Review Faculty: {}".format(complianceDictionary["arFaculty"]))
	print("Awaiting Review Staff: {}".format(complianceDictionary["arStaff"]))
	print("Awaiting Review Students: {}".format(complianceDictionary["arStudents"]))
	print("Awaiting Review ASC: {}".format(complianceDictionary["arASC"]))
	print("Awaiting Review ASI: {}".format(complianceDictionary["arASI"]))
	print("Awaiting Review Unknown: {}\n".format(complianceDictionary["arUnknown"]))
	print("Non-Compliant Faculty: {}".format(complianceDictionary["ncFaculty"]))
	print("Non-Compliant Staff: {}".format(complianceDictionary["ncStaff"]))
	print("Non-Compliant Students: {}".format(complianceDictionary["ncStudents"]))
	print("Non-Compliant ASC: {}".format(complianceDictionary["ncASC"]))
	print("Non-Compliant ASI: {}".format(complianceDictionary["ncASI"]))
	print("Non-Compliant Unknown: {}".format(complianceDictionary["ncUnknown"]))


def main():
	"""Main Function"""

	# Initialize variables
	listOfPatients = []

	complianceDictionary = {
		"cFaculty" : 0,
		"cStaff" : 0,
		"cStudents" : 0,
		"cASC" : 0,
		"cASI" : 0,
		"cUnknown" : 0,

		"arFaculty" : 0,
		"arStaff" : 0,
		"arStudents" : 0,
		"arASC" : 0,
		"arASI" : 0,
		"arUnknown" : 0,

		"ncFaculty" : 0,
		"ncStaff" : 0,
		"ncStudents" : 0,
		"ncASC" : 0,
		"ncASI" : 0,
		"ncUnknown" : 0
	}



	# Begin read-in processes
	print("Reading compliance from PNC ................... ", end='')
	readInCompliance(listOfPatients)
	print("SUCCESS\n")
	print("Reading employee extract ...................... ", end='')
	readInEmployees(listOfPatients)
	print("SUCCESS\n")
	print("Reading student extract ....................... ", end='')
	readInStudents(listOfPatients)
	print("SUCCESS\n")
	print("Reading non-state extract ..................... ", end='')
	readInNonState(listOfPatients)
	print("SUCCESS\n")



	# For debugging:
	# for patient in listOfPatients:
	# 	print("{}: {}, {}".format(patient.cwid, patient.patientType, patient.status))

	# Count compliance
	print("Counting compliance ........................... ", end='')
	countCompliance(listOfPatients, complianceDictionary)
	print("SUCCESS\n")

	# Output compliance
	printCompliance(listOfPatients, complianceDictionary)

main()