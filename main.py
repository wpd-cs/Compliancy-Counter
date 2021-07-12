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
		self.patientType = patientType
		self.status = status


def main():
	"""Main Function"""

	listOfPatients = []
	first_line1 = ""
	first_line2 = ""

	with open("compliance.txt", "r") as myFile:
		first_line1 = myFile.readline().strip().split(', ')
		del first_line1[0]

		for line in myFile:
			myLine = line.split(',')
			campusId = myLine[1]
			currstatus = myLine[5]

			myPatient = Patient(campusId, currstatus)
			
			listOfPatients.append(myPatient)

	for patient in listOfPatients:
		print("{}: {}".format(patient.cwid, patient.status))

	print(len(listOfPatients))





main()