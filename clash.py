from random import shuffle
import json

###
class data_getter():
    def __init__(self):
        pass
        

    def data_initialization(self):
        with open('C:\\Users\\hp folio 9480m i7\\Documents\\Angular\\timeTable\\_project\\_data.json','r') as f:
            x=f.read()
        _dic=json.loads(x) 

        return _dic


    def data_import(self):
        with open('C:\\Users\\hp folio 9480m i7\\Documents\\Angular\\timeTable\\_project\\_data.json','r') as f:
            x=f.read()
        _dic=json.loads(x) 
        lis=[]
        for i in _dic:
            lis.append(i)
            #print(i)
        return {'course':lis}








#####
class clashResolover:
   
    
    def __init__(self):
        global course_data
        d_get=data_getter()
        course_data=d_get.data_initialization()
        
#    def __init__(self''', student_list, teacher, subject, json_struct'''):
#        pass
#        '''self.student_list=student_list
#        self.teacher=teacher
#        self.subject=subject
#        self.json_struct=json_struct
#    '''
    def clashHandler(self,sub):
        subjectClashes=[] 
        
        for i in course_data:
            if i!=sub:
                if course_data[i]['teacher']==course_data[sub]['teacher']:
                    subjectClashes.append(i)
                else:
                    for j in range(len(course_data[sub]['studentList'])):
                        for k in range(len(course_data[i]['studentList'])):
                            if course_data[i]['studentList'][k]==course_data[sub]['studentList'][j]:
                                subjectClashes.append(i)
                                break
                                #print(course_data[i]['studentList'][j])

        return {'course': list(set(subjectClashes))} 
    
    def clashCheck(self,ls):
        subjectClashes=[]
        for i in ls:
            if i!=ls[-1]:
                if course_data[i]['teacher']==course_data[ls[-1]]['teacher']:
                    subjectClashes.append(i)
                   # print(course_data[ls[-1]]['teacher'])
                else:
                     for j in range(len(course_data[ls[-1]]['studentList'])):
                        for k in range(len(course_data[i]['studentList'])):
                            if course_data[i]['studentList'][k]==course_data[ls[-1]]['studentList'][j]:
                                subjectClashes.append(i+'\n '+str(course_data[i]['courseName']))
                               ## print(course_data[ls[-1]]['studentList'][j])

        return {'course':list(set(subjectClashes))}


c= clashResolover()
#print(c.clashHandler("CL103CS-R"))
#print(c.clashCheck(['CS118BS(SE)-19A', 'EE229CS18-A', 'CS301CS17-A','CS103CS-R']))
#import os
#
#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))

class creatTable():
    def __init__(self):
        pass

    def read_and_return(self):
        with open('C:\\Users\\hp folio 9480m i7\\Documents\\Angular\\timeTable\\_project\\alpha.json','r') as f:
            x=f.read()
        
        _dic=json.loads(x) 

        return _dic
class autogen1():
    def __init__(self):
        pass

    def read_gen1(self):
        with open('C:\\Users\\hp folio 9480m i7\\Documents\\Angular\\timeTable\\_project\\new_day1.json','r') as f:
            x=f.read()
        
        _dic=json.loads(x) 

        return _dic
class autogen():
    def __init__(self):
        pass

    def read_gen(self):
        with open('C:\\Users\\hp folio 9480m i7\\Documents\\Angular\\timeTable\\_project\\new_day.json','r') as f:
            x=f.read()
        
        _dic=json.loads(x) 

        return _dic