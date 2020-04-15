task = {
	"Process_No" : 0,
	"Burst_Time" : 0,
	"Arrival_Time" : 0,
	"Priority" : 0,
	"Start_Time" : 0,
	"Waiting_Time" : 0,
	"Turn_Around_Time": 0,
	"Complete_Time": 0
}
listProcess = []
num = int(input("Enter the no. of Process : "))
RQ = int(input("Enter Round Robin Time Qantum : "))
for i in range(num):
	print(f"P{i+1}")
	task["Process_No"] = i+1
	task["Arrival_Time"] = int(input("Enter the arival time : "))
	task["Burst_Time"] = int(input("Enter the burst time : "))
	task["Priority"] = int(input("Enter the priority : "))
	listProcess.append(task.copy())
title = '''
Process   AT    PT    ST    BT    WT    TAT
--------------------------------------------'''
def space(n):
	if(n//10 == 0):
		print("     ",end='')
	else:
		print("    ",end='')
def display(Process):
	# Table
	print(title)
	for i in range(len(Process)):
		print("   ",end='')
		print(Process[i].get("Process_No"), end='')
		print("      ",end='')
		print(Process[i].get("Arrival_Time"), end='')
		space(Process[i].get("Arrival_Time"))
		print(Process[i].get("Priority"), end='')
		space(Process[i].get("Priority"))
		print(Process[i].get("Start_Time"), end='')
		space(Process[i].get("Start_Time"))
		print(Process[i].get("Burst_Time"), end='')
		space(Process[i].get("Burst_Time"))
		print(Process[i].get("Waiting_Time"), end='')
		space(Process[i].get("Waiting_Time"))
		print(Process[i].get("Turn_Around_Time"))
	awt, atat = 0, 0
	for i in range(len(Process)):
		awt += Process[i]["Waiting_Time"]
		atat += Process[i]["Turn_Around_Time"]
	print("--------------------------------------------")
	print(f"Average Waiting Time : {awt/num}")
	print(f"Average Waiting Time : {atat/num}")
def sort(opt, Process):
	i = 1
	while (i < len(Process)):
		j = i
		while (j > 0):
			if(Process[j][opt] < Process[j-1][opt]):
				Process[j], Process[j-1] = Process[j-1], Process[j]
			j -= 1
		i += 1
	return Process
def FCFS():
	Process = listProcess.copy()
	for i in range(len(Process)):
		if (i == 0):
			Process[i]["Start_Time"] = Process[i]["Arrival_Time"]
			Process[i]["Complete_Time"] = Process[i]["Burst_Time"] + Process[i]["Arrival_Time"]
		else:
			Process[i]["Start_Time"] = Process[i-1]["Complete_Time"]
			Process[i]["Complete_Time"] = Process[i-1]["Complete_Time"] + Process[i]["Burst_Time"]
		Process[i]["Waiting_Time"] = Process[i]["Start_Time"] - Process[i]["Arrival_Time"]
		Process[i]["Turn_Around_Time"] = Process[i]["Complete_Time"] - Process[i]["Arrival_Time"]
	print("\nFCFS")
	# Gnart Chart
	for i in range(len(Process)):
		print(Process[i]["Start_Time"], end=" <-P")
		print(Process[i]["Process_No"], end="-> ")
	print(Process[-1]["Complete_Time"])
	display(Process)
def SJF():
	Process = listProcess.copy()
	Process[0]["Start_Time"] = Process[0]["Arrival_Time"]
	Process[0]["Complete_Time"] = Process[0]["Burst_Time"] + Process[0]["Arrival_Time"]
	Process[0]["Waiting_Time"] = Process[0]["Start_Time"] - Process[0]["Arrival_Time"]
	Process[0]["Turn_Around_Time"] = Process[0]["Complete_Time"] - Process[0]["Arrival_Time"]
	temp = Process[0]
	Process.remove(Process[0])
	Process = sort("Burst_Time", Process)
	for i in range(len(Process)):
		if (i == 0):
			Process[i]["Start_Time"] = temp["Complete_Time"]
			Process[i]["Complete_Time"] = Process[i]["Burst_Time"] + temp["Complete_Time"]
		else:
			Process[i]["Start_Time"] = Process[i-1]["Complete_Time"]
			Process[i]["Complete_Time"] = Process[i-1]["Complete_Time"] + Process[i]["Burst_Time"]
		Process[i]["Waiting_Time"] = Process[i]["Start_Time"] - Process[i]["Arrival_Time"]
		Process[i]["Turn_Around_Time"] = Process[i]["Complete_Time"] - Process[i]["Arrival_Time"]
	Process.insert(0, temp)
	print("\nSJF")
	# Gnart Chart
	for i in range(len(Process)):
		print(Process[i]["Start_Time"], end=" <-P")
		print(Process[i]["Process_No"], end="-> ")
	print(Process[-1]["Complete_Time"])
	display(Process)
def PRIORITY():
	Process = listProcess.copy()
	Process[0]["Start_Time"] = Process[0]["Arrival_Time"]
	Process[0]["Complete_Time"] = Process[0]["Burst_Time"] + Process[0]["Arrival_Time"]
	Process[0]["Waiting_Time"] = Process[0]["Start_Time"] - Process[0]["Arrival_Time"]
	Process[0]["Turn_Around_Time"] = Process[0]["Complete_Time"] - Process[0]["Arrival_Time"]
	temp = Process[0]
	Process.remove(Process[0])
	Process = sort("Priority", Process)
	for i in range(len(Process)):
		if (i == 0):
			Process[i]["Start_Time"] = temp["Complete_Time"]
			Process[i]["Complete_Time"] = Process[i]["Burst_Time"] + temp["Complete_Time"]
		else:
			Process[i]["Start_Time"] = Process[i-1]["Complete_Time"]
			Process[i]["Complete_Time"] = Process[i-1]["Complete_Time"] + Process[i]["Burst_Time"]
		Process[i]["Waiting_Time"] = Process[i]["Start_Time"] - Process[i]["Arrival_Time"]
		Process[i]["Turn_Around_Time"] = Process[i]["Complete_Time"] - Process[i]["Arrival_Time"]
	Process.insert(0, temp)
	print("\nPRIORITY")
	# Gnart Chart
	for i in range(len(Process)):
		print(Process[i]["Start_Time"], end=" <-P")
		print(Process[i]["Process_No"], end="-> ")
	print(Process[-1]["Complete_Time"])
	display(Process)
def RR():
	Process = listProcess.copy()
	print("\nRound Robin")
	Gline = 0
	count = [0]*num
	st = [0]*num
	ct = [0]*num
	blk = [0]*num
	brst = []
	for i in range(len(Process)):
		brst.append(Process[i]["Burst_Time"])
	pc = True
	# Gnatt Chart
	while (True):
		done = False
		for i in range(len(Process)):
			if(sum(count) == num-1):
				if (Process[i]["Burst_Time"] > 0):
					done = True
					if(not pc):
						print(Process[i]["Process_No"], end="-> ")
						st[i] += Gline
						pc = True
					if(Process[i]["Burst_Time"] >= RQ):
						Process[i]["Burst_Time"] -= RQ
						Gline += RQ
						blk[i] += 1
					else:
						Gline += Process[i]["Burst_Time"]
						Process[i]["Burst_Time"] = 0
						blk[i] += 1
					if(Process[i]["Burst_Time"] == 0):
						print(Gline)
						Process[i]["Turn_Around_Time"] = Gline
			else:  
				if(Process[i]["Burst_Time"] > 0):
					done = True
					if (pc):
						print(Gline, end=" <-P")
					pc = True
					print(Process[i]["Process_No"], end="-> ")
					if(Process[i]["Burst_Time"] >= RQ):
						st[i] += Gline
						Process[i]["Burst_Time"] -= RQ
						Gline += RQ
						ct[i] +=Gline
						blk[i] += 1
					else:
						st[i] += Gline
						Gline += Process[i]["Burst_Time"]
						Process[i]["Burst_Time"] = 0
						blk[i] += 1
					if(Process[i]["Burst_Time"] == 0):
						print(Gline, end=" <-P")
						Process[i]["Turn_Around_Time"] = Gline
						count[i] = 1
						pc = False
		if (done == False):
			break
	for i in range(len(Process)):
		if(blk[i] == 1):
			ct[i] =  0
		Process[i]["Waiting_Time"] = st[i] - ct[i] - Process[i]["Arrival_Time"]
		Process[i]["Start_Time"] = Process[i]["Waiting_Time"] + Process[i]["Arrival_Time"]
		Process[i]["Burst_Time"] = brst[i]
	display(Process)
if __name__ == "__main__":
	listProcess = sort("Arrival_Time", listProcess)
	FCFS()
	SJF()
	PRIORITY()
	RR()