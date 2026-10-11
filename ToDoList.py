import json
import os
# data = {}

# load task 
if os.path.exists("task.json") and os.path.getsize("task.json") > 0: 
    with open("task.json", "r") as f : 
        task = json.load(f);
        
else:
    task = []; #creating list




def addTask() : 
    taskNum = int(input("Enter Task Number : "))
    taskName = input("Enter Task Name : ")
    isTaskDone = int(input("Task Complete Or Not :  Choose 1 For true and 0 For false : "))
    
    data = {
        "taskId" : taskNum,
        "taskName" : taskName,
        "isDone" : isTaskDone == 1 
     }
    
    task.append(data)
    saveTask()
    
  
    
def saveTask() : 
    with open("task.json", "w") as f :
        json.dump(task, f , indent=3);
    
    print("Task Successfully Added!!");


def deletTask() : 
    
    print("Which Task You Want To Delete !!")
    viewTask();
    
    taskIdNum = int(input("Enter Task Id Number : "))
    
    with open("task.json", "r") as f :
        taskDetail = json.load(f)
        
    # print(taskDetail)
    for detail in taskDetail :
        # print(detail)
        if detail.get("taskId") == taskIdNum :
            taskDetail.remove(detail);
            
    # After Delting Update json file   
    with open("task.json", "w") as f: 
        json.dump(taskDetail, f , indent=3)
    print("Task Deleted!!");
        
    
def viewTask() : 
    print("!-------------- Task Detail --------------!")
    
    with open("task.json", "r") as f :
        taskDetail = json.load(f);
    
    for detail in taskDetail :
        print(f"TaskId : {detail["taskId"]} | TaskName : {detail["taskName"]} | taskIsDone : {detail["isDone"]}!!");
        
        
# it runs unitl user put 4.       
while True :         
    print("Hello Welcome!!")
    print("-- My ToDo List --")
    print("1. Add Task!")
    print("2. Remvoe Task!")
    print("3. Show All Task!")
    print("4. Exit")


    taskNum = int(input("Choose Option : "))

    if taskNum == 1 :
        addTask()

    elif taskNum == 2 :
        deletTask()

    elif taskNum == 3 :
        viewTask()

    elif taskNum == 4 :
        print("All date saved")
        break;
    else : 
        print("Invalid Number!!")

