# -*- coding: utf-8 -*-
"""

William Duong
Project started: July 12, 2021
wpduong@gmail.com

Last Updated: 11/15/2021

"""

from sys import exit
import datetime
import csv
import os

class Patient:
	def __init__ (self, cwid, status, acadStatus = '', patientType = ''):
		"""Initialize class data members"""
		self.cwid = cwid
		self.status = status
		self.acadStatus = acadStatus
		self.patientType = patientType


def checkFiles():
	"""Check to make sure all input files are present"""
	listOfFiles = ["compliance.txt", "employee.txt", "student.txt", \
				   "nonstate.txt"]

	filesNeeded = []

	for file in listOfFiles:
		if not os.path.exists(file):
			filesNeeded.append(file)

	if filesNeeded:
		exit("ERROR\nMissing files: {}".format(filesNeeded))


def readInCompliance(listOfPatients):
	"""Read in PNC Data"""
	with open("compliance.txt", "r") as myFile:
		first_line = myFile.readline()
		del first_line

		for line in myFile:
			myLine = line.split(',')
			campusId = myLine[3].strip('"')
			currstatus = myLine[7]

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
					patient.acadStatus = myLine[52]


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


def countCompliance(listOfPatients, complianceDictionary, compliantId, exemptId, \
					participantId, activeNCId):
	"""Count number for each category"""
	for patient in listOfPatients:
		if (patient.status == '"Compliant with Standard Requirements"'):
			if patient.patientType == "Faculty":
				complianceDictionary["cFaculty"] += 1
			elif patient.patientType == "Staff":
				complianceDictionary["cStaff"] += 1
			elif patient.patientType == "Student":
				if patient.acadStatus == "ACTIVE":
					complianceDictionary["cCurStudents"] += 1
				else:
					complianceDictionary["cFutStudents"] += 1
			elif patient.patientType == "ASC":
				complianceDictionary["cASC"] += 1
			elif patient.patientType == "ASI":
				complianceDictionary["cASI"] += 1
			else:
				complianceDictionary["cUnknown"] += 1
			temp = [patient.cwid]
			compliantId.append(temp)
			participantId.append(temp)
		if patient.status == '"Awaiting Review"':
			if patient.patientType == "Faculty":
				complianceDictionary["arFaculty"] += 1
			elif patient.patientType == "Staff":
				complianceDictionary["arStaff"] += 1
			elif patient.patientType == "Student":
				if patient.acadStatus == "ACTIVE":
					complianceDictionary["arCurStudents"] += 1
				else:
					complianceDictionary["arFutStudents"] += 1
			elif patient.patientType == "ASC":
				complianceDictionary["arASC"] += 1
			elif patient.patientType == "ASI":
				complianceDictionary["arASI"] += 1
			else:
				complianceDictionary["arUnknown"] += 1
			temp = [patient.cwid]
			participantId.append(temp)
		if patient.status == '"Exemption: Medical COVID-19"':
			if patient.patientType == "Faculty":
				complianceDictionary["meFaculty"] += 1
			elif patient.patientType == "Staff":
				complianceDictionary["meStaff"] += 1
			elif patient.patientType == "Student":
				if patient.acadStatus == "ACTIVE":
					complianceDictionary["meCurStudents"] += 1
				else:
					complianceDictionary["meFutStudents"] += 1
			elif patient.patientType == "ASC":
				complianceDictionary["meASC"] += 1
			elif patient.patientType == "ASI":
				complianceDictionary["meASI"] += 1
			else:
				complianceDictionary["meUnknown"] += 1
			temp = [patient.cwid, patient.status.strip('"')]
			exemptId.append(temp)
			temp2 = [patient.cwid]
			participantId.append(temp2)
		if patient.status == '"Exemption: Extension COVID-19"':
			if patient.patientType == "Faculty":
				complianceDictionary["eeFaculty"] += 1
			elif patient.patientType == "Staff":
				complianceDictionary["eeStaff"] += 1
			elif patient.patientType == "Student":
				if patient.acadStatus == "ACTIVE":
					complianceDictionary["eeCurStudents"] += 1
				else:
					complianceDictionary["eeFutStudents"] += 1
			elif patient.patientType == "ASC":
				complianceDictionary["eeASC"] += 1
			elif patient.patientType == "ASI":
				complianceDictionary["eeASI"] += 1
			else:
				complianceDictionary["eeUnknown"] += 1
			temp = [patient.cwid]
			compliantId.append(temp)
			participantId.append(temp)
		if patient.status == '"Exemption: Breast Feeding COVID"':
			temp = [patient.cwid, patient.status.strip('"')]
			exemptId.append(temp)
			temp2 = [patient.cwid]
			participantId.append(temp2)
		if patient.status == '"Exemption: Pregnant COVID-19"':
			temp = [patient.cwid, patient.status.strip('"')]
			exemptId.append(temp)
			temp2 = [patient.cwid]
			participantId.append(temp2)
		if patient.status == '"Exemption: Religious COVID-19"':
			if patient.patientType == "Faculty":
				complianceDictionary["reFaculty"] += 1
			elif patient.patientType == "Staff":
				complianceDictionary["reStaff"] += 1
			elif patient.patientType == "Student":
				if patient.acadStatus == "ACTIVE":
					complianceDictionary["reCurStudents"] += 1
				else:
					complianceDictionary["arFutStudents"] += 1
			elif patient.patientType == "ASC":
				complianceDictionary["reASC"] += 1
			elif patient.patientType == "ASI":
				complianceDictionary["reASI"] += 1
			else:
				complianceDictionary["reUnknown"] += 1
			temp = [patient.cwid, patient.status.strip('"')]
			exemptId.append(temp)
			temp2 = [patient.cwid]
			participantId.append(temp2)
		if patient.status == '"Exemption: Pos COVID-19 90 Days"':
			temp = [patient.cwid]
			participantId.append(temp)
		if not (patient.status == '"Compliant with Standard Requirements"' or patient.status == '"Awaiting Review"' or\
				patient.status == '"Exemption: Medical COVID-19"' or patient.status == '"Exemption: Religious COVID-19"' or\
				patient.status == '"Exemption: Extension COVID-19"' or patient.status == '"Exemption: Breast Feeding COVID"'):

			if (patient.status == '"Non-Compliant- No Data"' or patient.status == '"Non-Compliant (Unmet Requirement)"') \
			    and patient.patientType != "":
				temp = [patient.cwid, patient.patientType, patient.status]
				activeNCId.append(temp)

			if patient.patientType == "Faculty":
				complianceDictionary["ncFaculty"] += 1
			elif patient.patientType == "Staff":
				complianceDictionary["ncStaff"] += 1
			elif patient.patientType == "Student":
				if patient.acadStatus == "ACTIVE":
					complianceDictionary["ncCurStudents"] += 1
				else:
					complianceDictionary["ncFutStudents"] += 1
			elif patient.patientType == "ASC":
				complianceDictionary["ncASC"] += 1
			elif patient.patientType == "ASI":
				complianceDictionary["ncASI"] += 1
			else:
				complianceDictionary["ncUnknown"] += 1


def printCompliance(listOfPatients, complianceDictionary, path):
	"""Output compliance numbers"""
	today = datetime.date.today()
	d = today.strftime("%b-%d-%Y")

	completeName = os.path.join(path, "Compliance_NUMBERS({}).txt".format(d))
	f = open(completeName, "w")


	studentUploads = complianceDictionary["cCurStudents"] + complianceDictionary["arCurStudents"] \
					 + complianceDictionary["cFutStudents"] + complianceDictionary["arFutStudents"]

	f.write("Compliant Active Students: {:,}	Awaiting Review Active Students: {:,}\n"\
			.format(complianceDictionary["cCurStudents"], complianceDictionary["arCurStudents"]))
	f.write("Compliant Future Students: {:,}	Awaiting Review Future Students: {:,}\n"\
			.format(complianceDictionary["cFutStudents"], complianceDictionary["arFutStudents"]))
	f.write("Total Student Uploads: {:,}\n\n".format(studentUploads))

	employeeUploads = complianceDictionary["cFaculty"] + complianceDictionary["cStaff"] \
					  + complianceDictionary["arFaculty"] + complianceDictionary["arStaff"] \
					  + complianceDictionary["cASC"] + complianceDictionary["cASI"] \
					  + complianceDictionary["arASC"] + complianceDictionary["arASI"]

	f.write("Compliant Faculty: {:,}		Awaiting Review Faculty: {:,}\n"\
			.format(complianceDictionary["cFaculty"], complianceDictionary["arFaculty"]))
	f.write("Compliant Staff: {:,}			Awaiting Review Staff: {:,}\n"\
			.format(complianceDictionary["cStaff"], complianceDictionary["arStaff"]))
	f.write("Compliant ASC: {:,}			Awaiting Review ASC: {:,}\n"\
			.format(complianceDictionary["cASC"], complianceDictionary["arASC"]))
	f.write("Compliant ASI: {:,}			Awaiting Review ASI: {:,}\n"\
			.format(complianceDictionary["cASI"], complianceDictionary["arASI"]))
	f.write("Total Employee Uploads: {:,}\n\n".format(employeeUploads))

	f.write("Unspecified Compliant: {:,}		Unspecified Awaiting Review: {:,}\n\n"\
			.format(complianceDictionary["cUnknown"], complianceDictionary["arUnknown"]))

	unknownUploads = complianceDictionary["cUnknown"] + complianceDictionary["arUnknown"]
	totalUploads = studentUploads + employeeUploads + unknownUploads

	f.write("Grand Total Uploads: {:,}\n\n".format(totalUploads))

	f.write("M.E. - Medical Exemption\n")
	f.write("M.E. Active Students: {:,}		M.E. Future Students: {:,}\n"\
			.format(complianceDictionary["meCurStudents"], complianceDictionary["meFutStudents"]))
	f.write("M.E. Faculty: {:,}			M.E. Staff: {:,}\n"\
			.format(complianceDictionary["meFaculty"], complianceDictionary["meStaff"]))
	f.write("M.E. ASI: {:,}				M.E. ASC: {:,}\n"\
			.format(complianceDictionary["meASI"], complianceDictionary["meASC"]))
	f.write("M.E. Unknown: {:,}\n".format(complianceDictionary["meUnknown"]))

	totalMed = complianceDictionary["meCurStudents"] + complianceDictionary["meFutStudents"] \
			   + complianceDictionary["meFaculty"] + complianceDictionary["meStaff"] \
			   + complianceDictionary["meASI"] + complianceDictionary["meASC"] \
			   + complianceDictionary["meUnknown"]

	f.write("Total Medical Exemptions: {:,}\n\n".format(totalMed))

	f.write("E.E. - Extension Exemption\n")
	f.write("E.E. Active Students: {:,}		E.E. Future Students: {:,}\n"\
			.format(complianceDictionary["eeCurStudents"], complianceDictionary["eeFutStudents"]))
	f.write("E.E. Faculty: {:,}				E.E. Staff: {:,}\n"\
			.format(complianceDictionary["eeFaculty"], complianceDictionary["eeStaff"]))
	f.write("E.E. ASI: {:,}				E.E. ASC: {:,}\n"\
			.format(complianceDictionary["eeASI"], complianceDictionary["eeASC"]))
	f.write("E.E. Unknown: {:,}\n".format(complianceDictionary["eeUnknown"]))

	totalRel = complianceDictionary["eeCurStudents"] + complianceDictionary["eeFutStudents"] \
			   + complianceDictionary["eeFaculty"] + complianceDictionary["eeStaff"] \
			   + complianceDictionary["eeASI"] + complianceDictionary["eeASC"] \
			   + complianceDictionary["eeUnknown"]

	f.write("Total Extension Exemptions: {:,}\n\n".format(totalRel))

	f.write("R.E. - Religious Exemption\n")
	f.write("R.E. Active Students: {:,}		R.E. Future Students: {:,}\n"\
			.format(complianceDictionary["reCurStudents"], complianceDictionary["reFutStudents"]))
	f.write("R.E. Faculty: {:,}			R.E. Staff: {:,}\n"\
			.format(complianceDictionary["reFaculty"], complianceDictionary["reStaff"]))
	f.write("R.E. ASI: {:,}				R.E. ASC: {:,}\n"\
			.format(complianceDictionary["reASI"], complianceDictionary["reASC"]))
	f.write("R.E. Unknown: {:,}\n".format(complianceDictionary["reUnknown"]))

	totalRel = complianceDictionary["reCurStudents"] + complianceDictionary["reFutStudents"] \
			   + complianceDictionary["reFaculty"] + complianceDictionary["reStaff"] \
			   + complianceDictionary["reASI"] + complianceDictionary["reASC"] \
			   + complianceDictionary["reUnknown"]

	f.write("Total Religious Exemptions: {:,}\n\n".format(totalRel))

	totalExemp = totalMed + totalRel

	f.write("Grand Total Exemptions: {:,}\n\n".format(totalExemp))

	f.write("--------------------------------------------------------------------\n\n")

	f.write("N.C. - Not Compliant\n")
	f.write("N.C. Active Students: {:,}		N.C. Future Students: {:,}\n"\
			.format(complianceDictionary["ncCurStudents"], complianceDictionary["ncFutStudents"]))
	f.write("N.C. Faculty: {:,}			N.C. Staff: {:,}\n"\
			.format(complianceDictionary["ncFaculty"], complianceDictionary["ncStaff"]))
	f.write("N.C. ASC: {:,}				N.C. ASI: {:,}\n"\
			.format(complianceDictionary["ncASC"], complianceDictionary["ncASI"]))
	f.write("Unspecified N.C.: {:,}\n\n".format(complianceDictionary["ncUnknown"]))

	totalNC = complianceDictionary["ncCurStudents"] + complianceDictionary["ncFutStudents"] \
			  + complianceDictionary["ncFaculty"] + complianceDictionary["ncStaff"] \
			  + complianceDictionary["ncASC"] + complianceDictionary["ncASI"] \
			  + complianceDictionary["ncUnknown"]

	f.write("Grand Total Not Compliant: {:,}".format(totalNC))


	f.close()


def getCompliantId(compliantId, path):
	"""Output compliant CWIDs"""
	today = datetime.date.today()
	d = today.strftime("%b-%d-%Y")

	completeName = os.path.join(path, "Compliance CWID({}).csv".format(d))
	f = open(completeName, "w", newline='')


	with f:
		write = csv.writer(f)
		write.writerows(compliantId)


	f.close()


def getExemptId(exemptId, path):
	"""Output exemption CWIDs for Central IT"""

	writeList = []

	for x in exemptId:
		temp = [x[0]]
		writeList.append(temp)

	today = datetime.date.today()
	d = today.strftime("%b-%d-%Y")

	completeName = os.path.join(path, "Exemption List({}).csv".format(d))
	f = open(completeName, "w", newline='')


	with f:
		write = csv.writer(f)
		write.writerows(writeList)


	f.close()


def getPSexemptions(exemptId, path):
	"""Output exempt CWIDs for PeopleSoft"""
	today = datetime.date.today()
	d = today.strftime("%b-%d-%Y")

	completeName = os.path.join(path, "Exempt List({}).csv".format(d))
	f = open(completeName, "w", newline='')


	with f:
		write = csv.writer(f)
		write.writerows(exemptId)


	f.close()


def getParticipantId(participantId, path):
	"""Output participant CWIDs"""
	today = datetime.date.today()
	d = today.strftime("%b-%d-%Y")

	completeName = os.path.join(path, "PNC Compliant List({}).csv".format(d))
	f = open(completeName, "w", newline='')


	with f:
		write = csv.writer(f)
		write.writerows(participantId)


	f.close()

def getActiveNCId(activeNCId, path):
	"""Output active non-compliant CWIDS"""
	today = datetime.date.today()
	d = today.strftime("%b-%d-%Y")

	completeName = os.path.join(path, "Active Non-Compliant({}).csv".format(d))
	f = open(completeName, "w", newline='')


	with f:
		write = csv.writer(f)
		write.writerows(activeNCId)


	f.close()


def main():
	"""Main Function"""

	# Initialize variables

	# List of patients
	listOfPatients = []

	# Compliant CWIDs
	compliantId = []

	# Exempt CWIDS
	exemptId = []

	# Participant CWIDS
	participantId = []

	# Active non-compliant CWIDS
	activeNCId = []

	complianceDictionary = {
		"cFaculty" : 0,
		"cStaff" : 0,
		"cCurStudents" : 0,
		"cFutStudents" : 0,
		"cASC" : 0,
		"cASI" : 0,
		"cUnknown" : 0,

		"arFaculty" : 0,
		"arStaff" : 0,
		"arCurStudents" : 0,
		"arFutStudents" : 0,
		"arASC" : 0,
		"arASI" : 0,
		"arUnknown" : 0,

		"ncFaculty" : 0,
		"ncStaff" : 0,
		"ncCurStudents" : 0,
		"ncFutStudents" : 0,
		"ncASC" : 0,
		"ncASI" : 0,
		"ncUnknown" : 0,

		"meFaculty" : 0,
		"meStaff" : 0,
		"meCurStudents" : 0,
		"meFutStudents" : 0,
		"meASC" : 0,
		"meASI" : 0,
		"meUnknown" : 0,

		"reFaculty" : 0,
		"reStaff" : 0,
		"reCurStudents" : 0,
		"reFutStudents" : 0,
		"reASC" : 0,
		"reASI" : 0,
		"reUnknown" : 0,

		"eeFaculty" : 0,
		"eeStaff" : 0,
		"eeCurStudents" : 0,
		"eeFutStudents" : 0,
		"eeASC" : 0,
		"eeASI" : 0,
		"eeUnknown" : 0,
	}


	# Begin read-in processes
	print("Checking for all input files .................. ", end='')
	checkFiles()
	print("SUCCESS\n")
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
	countCompliance(listOfPatients, complianceDictionary, compliantId, exemptId, \
					participantId, activeNCId)
	print("SUCCESS\n")


	print("Creating output files ......................... ", end='')

	# Creating folder
	d = datetime.datetime.now()
	d = d.strftime("%m-%d-%y %H%M%S %p")

	parent_dir = os.getcwd()
	path = os.path.join(parent_dir, d)
	os.mkdir(path)

	print("SUCCESS\n")


	# Output compliance
	printCompliance(listOfPatients, complianceDictionary, path)

	# Output compliant CWIDs
	getCompliantId(compliantId, path)

	# Output exemption CWIDs for Central IT
	getExemptId(exemptId, path)

	# Output exempt CWIDs for PeopleSoft
	getPSexemptions(exemptId, path)

	# Output participant CWIDs
	getParticipantId(participantId, path)

	# Output active non-compliant people
	getActiveNCId(activeNCId, path)


main()