#Grading System

data={
    1:{'name':'praveen','attempt_status':False,'python':0,'sql':0,'powerbi':0},
    2:{'name':'Harshith','attempt_status':True,'python':100,'sql':90,'powerbi':80},#90
    3:{'name':'Varun','attempt_status':True,'python':80,'sql':90,'powerbi':20}, #70.0
    4:{'name':'Tarit','attempt_status':True,'python':30,'sql':100,'powerbi':25}, # 52.0
    5:{'name':'Sheshu','attempt_status':True,'python':60,'sql':40,'powerbi':35}, #45
}

stuid=int(input("Enter the student id: ")) #1,2,3 like that..

if data[stuid]['attempt_status']:  #if true 
    total=(data[stuid]['python']+data[stuid]['sql']+data[stuid]['powerbi'])/3 #2 90.0 #3 75.0 #4 52.0 #5 45
    if total>90:   
        print(f'Congrats!!!\n{data[stuid]["name"]} got "A" grade') #Congrats!!! Harshit
                                                                   #got "A" Grade
    elif total>75:
        print(f'Good!!!\n{data[stuid]["name"]} got "B" grade') #Good!! varun
                                                                #got "B" Grade
    elif total>50:
        print(f'Try it improve!!!\n{data[stuid]["name"]} got "C" grade')  #Try it improve!!! tarit
                                                                          #got "C" grade
    elif total>35:                                                         
        print(f'Just Passed!!!\n{data[stuid]["name"]} got "D" grade')
    else:
        print(f'Better luck next time!!!\n{data[stuid]["name"]} failed')
        
else:                              #first if case is false 
    print(f'{data[stuid]["name"]} is not attempted the exam.') #1 praveen is not attemtes the exam.