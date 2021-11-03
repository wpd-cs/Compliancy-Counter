# -*- coding: utf-8 -*-
"""

William Duong
Mon July 12, 2021
wpduong@gmail.com

Last Updated: 09/15/2021

"""

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
				patient.status == '"Exemption: Medical COVID-19"' or patient.status == '"Exemption: Religious COVID-19"'):

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

	f.write("Compliant Active Students: {:,}\n".format(complianceDictionary["cCurStudents"]))
	f.write("Compliant Future Students: {:,}\n".format(complianceDictionary["cFutStudents"]))
	f.write("Awaiting Review Active Students: {:,}\n".format(complianceDictionary["arCurStudents"]))
	f.write("Awaiting Review Future Students: {:,}\n".format(complianceDictionary["arFutStudents"]))
	f.write("Total Student Uploads: {:,}\n\n".format(studentUploads))

	employeeUploads = complianceDictionary["cFaculty"] + complianceDictionary["cStaff"] \
					  + complianceDictionary["arFaculty"] + complianceDictionary["arStaff"] \
					  + complianceDictionary["cASC"] + complianceDictionary["cASI"] \
					  + complianceDictionary["arASC"] + complianceDictionary["arASI"]

	f.write("Compliant Faculty: {:,}\n".format(complianceDictionary["cFaculty"]))
	f.write("Compliant Staff: {:,}\n".format(complianceDictionary["cStaff"]))
	f.write("Awaiting Review Faculty: {:,}\n".format(complianceDictionary["arFaculty"]))
	f.write("Awaiting Review Staff: {:,}\n".format(complianceDictionary["arStaff"]))
	f.write("Compliant ASC: {:,}\n".format(complianceDictionary["cASC"]))
	f.write("Compliant ASI: {:,}\n".format(complianceDictionary["cASI"]))
	f.write("Awaiting Review ASC: {:,}\n".format(complianceDictionary["arASC"]))
	f.write("Awaiting Review ASI: {:,}\n".format(complianceDictionary["arASI"]))
	f.write("Total Employee Uploads: {:,}\n\n".format(employeeUploads))

	f.write("Not in Current Import Compliant: {:,}\n".format(complianceDictionary["cUnknown"]))
	f.write("Not in Current Import Awaiting Review: {:,}\n\n".format(complianceDictionary["arUnknown"]))

	unknownUploads = complianceDictionary["cUnknown"] + complianceDictionary["arUnknown"]
	totalUploads = studentUploads + employeeUploads + unknownUploads

	f.write("Grand Total Uploads: {:,}\n\n".format(totalUploads))

	f.write("Medical Exemption Active Students: {:,}\n".format(complianceDictionary["meCurStudents"]))
	f.write("Medical Exemption Future Students: {:,}\n".format(complianceDictionary["meFutStudents"]))
	f.write("Medical Exemption Faculty: {:,}\n".format(complianceDictionary["meFaculty"]))
	f.write("Medical Exemption Staff: {:,}\n".format(complianceDictionary["meStaff"]))
	f.write("Medical Exemption ASI: {:,}\n".format(complianceDictionary["meASI"]))
	f.write("Medical Exemption ASC: {:,}\n".format(complianceDictionary["meASC"]))
	f.write("Medical Exemption Unknown: {:,}\n".format(complianceDictionary["meUnknown"]))

	totalMed = complianceDictionary["meCurStudents"] + complianceDictionary["meFutStudents"] \
			   + complianceDictionary["meFaculty"] + complianceDictionary["meStaff"] \
			   + complianceDictionary["meASI"] + complianceDictionary["meASC"] \
			   + complianceDictionary["meUnknown"]

	f.write("Total Medical Exemptions: {:,}\n\n".format(totalMed))

	f.write("Extension Exemption Active Students: {:,}\n".format(complianceDictionary["eeCurStudents"]))
	f.write("Extension Exemption Future Students: {:,}\n".format(complianceDictionary["eeFutStudents"]))
	f.write("Extension Exemption Faculty: {:,}\n".format(complianceDictionary["eeFaculty"]))
	f.write("Extension Exemption Staff: {:,}\n".format(complianceDictionary["eeStaff"]))
	f.write("Extension Exemption ASI: {:,}\n".format(complianceDictionary["eeASI"]))
	f.write("Extension Exemption ASC: {:,}\n".format(complianceDictionary["eeASC"]))
	f.write("Extension Exemption Unknown: {:,}\n".format(complianceDictionary["eeUnknown"]))

	totalRel = complianceDictionary["eeCurStudents"] + complianceDictionary["eeFutStudents"] \
			   + complianceDictionary["eeFaculty"] + complianceDictionary["eeStaff"] \
			   + complianceDictionary["eeASI"] + complianceDictionary["eeASC"] \
			   + complianceDictionary["eeUnknown"]

	f.write("Total Extension Exemptions: {:,}\n\n".format(totalRel))

	f.write("Religious Exemption Active Students: {:,}\n".format(complianceDictionary["reCurStudents"]))
	f.write("Religious Exemption Future Students: {:,}\n".format(complianceDictionary["reFutStudents"]))
	f.write("Religious Exemption Faculty: {:,}\n".format(complianceDictionary["reFaculty"]))
	f.write("Religious Exemption Staff: {:,}\n".format(complianceDictionary["reStaff"]))
	f.write("Religious Exemption ASI: {:,}\n".format(complianceDictionary["reASI"]))
	f.write("Religious Exemption ASC: {:,}\n".format(complianceDictionary["reASC"]))
	f.write("Religious Exemption Unknown: {:,}\n".format(complianceDictionary["reUnknown"]))

	totalRel = complianceDictionary["reCurStudents"] + complianceDictionary["reFutStudents"] \
			   + complianceDictionary["reFaculty"] + complianceDictionary["reStaff"] \
			   + complianceDictionary["reASI"] + complianceDictionary["reASC"] \
			   + complianceDictionary["reUnknown"]

	f.write("Total Religious Exemptions: {:,}\n\n".format(totalRel))

	totalExemp = totalMed + totalRel

	f.write("Grand Total Exemptions: {:,}\n\n".format(totalExemp))

	f.write("-------------------------------------\n\n")

	f.write("Non-Compliant Active Students: {:,}\n".format(complianceDictionary["ncCurStudents"]))
	f.write("Non-Compliant Future Students: {:,}\n".format(complianceDictionary["ncFutStudents"]))
	f.write("Non-Compliant Faculty: {:,}\n".format(complianceDictionary["ncFaculty"]))
	f.write("Non-Compliant Staff: {:,}\n".format(complianceDictionary["ncStaff"]))
	f.write("Non-Compliant ASC: {:,}\n".format(complianceDictionary["ncASC"]))
	f.write("Non-Compliant ASI: {:,}\n".format(complianceDictionary["ncASI"]))
	f.write("Not in Current Import Non-Compliant: {:,}\n".format(complianceDictionary["ncUnknown"]))


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