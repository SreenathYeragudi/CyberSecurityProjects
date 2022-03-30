import argparse
import pickle
import sys

'''
class CanAccess:
    -> Checks to see if a user can do an operation on a specific object
'''
class CanAccess:
    
    def __init__(self,op,user,obj,setDomain_dict,setType_dict,access):
        self.op=op
        self.user=user
        self.obj=obj
        self.sDd=setDomain_dict
        self.sTd=setType_dict
        self.access_dict=access
    
    def CanAccess(self):
        flag=0
        if self.op=="" and self.user=="" and self.obj=="":
            print("Error: access denied")
        elif self.op=="" or self.user=="" or self.obj=="":
            print("Error: access denied")
        else:
            if self.user in self.sDd:
                user_domain=self.sDd[self.user]
                if self.obj in self.sTd:
                    obj_type=self.sTd[self.obj]
                    if type(user_domain)!=list:
                        for o in obj_type:
                                if (user_domain,o) in self.access_dict:
                                    if self.op in self.access_dict[(user_domain,o)]:
                                            print("Success")
                                            flag=1
                                            break
                                    elif  self.op not in self.access_dict[(user_domain,o)]:
                                        continue
                        if flag!=1:
                            print("Error: access denied")
                    else:
                        for u in user_domain:
                            for o in obj_type:
                                if (u,o) in self.access_dict:
                                    if self.op in self.access_dict[(u,o)]:
                                            print("Success")
                                            flag=1
                                            break
                                    elif  self.op not in self.access_dict[(u,o)]:
                                        continue
                        if flag!=1:
                            print("Error: access denied")
                else:
                    print("Error: access denied")
            else:
                print("Error: access denied")
            
                        
'''
class AddAccess
    ->Adds access to the given users
'''
class AddAccess:
    
    def __init__(self,op,domain,type_name,dict):
        self.op=op
        self.domain=domain
        self.type=type_name
        self.dict=dict

    def AddAcc(self):
        v=0
        if self.op=="" and self.domain=="" and self.type=="":
            print("Error: missing operation,domain,type")
        elif self.op=="":
            print("Error: missing operation")
        elif self.domain=="":
            print("Error: missing domain")
        elif self.type=="":
            print("Error: missing type")
        else:
            if (self.domain,self.type) not in self.dict:
                print("Sucess")
                self.dict[(self.domain,self.type)]=self.op
           
            elif isinstance(self.dict[(self.domain,self.type)], list):
                if self.op in self.dict[(self.domain,self.type)]:
                    v=1
                else:
                    print("Sucess")
                    self.dict[(self.domain,self.type)].append(self.op)
            else:
                if self.op in self.dict[(self.domain,self.type)]:
                    v=1
                else:
                    print("Sucess")
                    self.dict[(self.domain,self.type)] = [self.dict[(self.domain,self.type)], self.op]
        return self.dict

'''
class TypeInfo
'''

class TypeInfo:

    def __init__(self,type_name,dict):
        self.type_name=type_name
        self.dict=dict
    
    def getTypeName(self):
        for key,value in self.dict.items():
            if self.type_name=="":
                print("Error")
                break
            elif self.type_name in value:
                print(key)
                
            

'''
class SetType
    ->Sets the type to given objects
'''
class SetType:

    def __init__(self,obj,type_name,d,dict):
        self.object=obj
        self.type_name=type_name
        self.d=d
        self.dict=dict
    
    def SetType(self):
        if self.object=="" and self.type_name=="":
            print("Error")
        elif self.object=="" or self.type_name=="":
            print("Error")
        else:
            print("Success")
            if self.object not in self.dict:
                self.dict[self.object]=self.type_name
            elif isinstance(self.dict[self.object], list):
                if self.type_name in self.dict[self.object]:
                    v=1
                else:
                    self.dict[self.object].append(self.type_name)
            else:
                if self.type_name in self.dict[self.object]:
                    v=1
                else:
                    self.dict[self.object] = [self.dict[self.object], self.type_name]
        return self.dict


'''
class DomainInfo
    ->prints all the users to a specific domain
'''
class DomainInfo:

    def __init__(self,domain,d):
        self.domain=domain
        self.d=d
    def getInfo(self):
        for key,value in self.d.items():
            if self.domain=="":
                print("Error: missing domain")
                break
            elif self.domain in value:
                print(key)

'''
class SetDomain
    ->sets the domain for the users
'''

class SetDomain:
    def __init__(self,username,domain,d,user_to_domain):
        self.username=username
        self.domain=domain
        self.d=d
        self.user_to_domain=user_to_domain
        
    
    def set_domain_mapped(self):
        domain_list=[]
        v=0
        
        if self.domain =="":
            print("Error: missing domain")
        elif self.username not in self.d:
            print("Error: no such user")
        else:
            
            if self.username not in self.user_to_domain:
                print("Success")
                self.user_to_domain[self.username]=self.domain
            elif isinstance(self.user_to_domain[self.username], list):
                if self.domain in self.user_to_domain[self.username]:
                    v=1
                else:
                    print("Success")
                    self.user_to_domain[self.username].append(self.domain)
            else:
                if self.domain in self.user_to_domain[self.username]:
                    v=1
                else:
                   print("Success")
                   self.user_to_domain[self.username] = [self.user_to_domain[self.username], self.domain]
        return self.user_to_domain

'''
class Authenticate
    ->does authentication handeling
'''

class Authenticate:

    def __init__(self,username,password,dict):
        self.username=username
        self.password=password
        self.d=dict
    
    def auth_user(self):
        if self.username not in self.d:
            print("Error: no such username")
        elif self.password != self.d[self.username]:
            print("Error: bad password")
        else:
            print("Success")
       

'''
class AddUser
    ->Handler for all AddUser capabilities
'''
class AddUser:
    def __init__(self,username,password,dict):
        self.username=username
        self.password=password
        self.d=dict
    
    def AddUser_dict(self):
        if self.username=="" or self.password=="":
            if self.password=="" and self.username!="":
                print("Error: password missing")
            elif self.username=="" and self.password!="":
                print("Error: username missing")
            elif self.password=="" and self.username=="":
                print("Error: username and password missing")
        elif self.username in self.d:
            print("Error: user exists")
        else:
            self.d[self.username]=self.password
            print("Success")
        return self.d

    
'''
class auth
    ->main class of the program
'''
class auth:

    def toFile(f,d1):
        filename=f
        file=open(filename,"wb")
        pickle.dump(d1,file)

    def readFile(filename):
        file=open(filename,'rb')
        try:
            d={}
            d=pickle.load(file)
        except EOFError:
            d={}
        return d

   

    if __name__ == "__main__":
        parser=argparse.ArgumentParser()
        for i in range(len(sys.argv)-1):
            parser.add_argument("part"+str(i))
        
        args=parser.parse_args()
        open('user.txt','a')
        open('setDomain.txt','a')
        open('DomainInfo.txt','a')
        open('setType.txt','a')
        open('access.txt','a')
        
        if args.part0== "AddUser":
            if len(sys.argv)>4:
                print("Error: too many arguements for AddUser")
            elif len(sys.argv)<4:
                print("Error: too little arguements for AddUser")
            else:
                d=readFile("user.txt")
                addUser=AddUser(args.part1,args.part2,d)
                d1=addUser.AddUser_dict()
                tofile=toFile("user.txt",d1)
        elif args.part0== "Authenticate":
            if len(sys.argv)>4:
                print("Error: too many arguements for Authenticate")
            elif len(sys.argv)<4:
                print("Error: too little arguements for Authenticate")
            else:
                d=readFile('user.txt')
                auth=Authenticate(args.part1,args.part2,d)
                auth.auth_user()
        elif args.part0== "SetDomain":
            if len(sys.argv)>4:
                print("Error: too many arguements for SetDomain")
            elif len(sys.argv)<4:
                if len(sys.argv)==2:
                    print("Error: too little arguements for SetDomain")
                elif len(sys.argv)==3:
                    print("Error: domain missing")
            else:
                d=readFile('user.txt')
                d2=readFile('setDomain.txt')
                set_domain=SetDomain(args.part1,args.part2,d,d2)
                d1=set_domain.set_domain_mapped()
                toFile=toFile("setDomain.txt",d1)
        elif args.part0== "DomainInfo":
            if len(sys.argv)>3:
                print("Error: too many arguements for DomainInfo")
            elif len(sys.argv)<3:
                print("Error: too little arguements for DomainInfo")
            else:
                d=readFile('setDomain.txt')
                domain_info=DomainInfo(args.part1,d)
                d1=domain_info.getInfo()
        elif args.part0=="SetType":
            if len(sys.argv)>4:
                print("Error: too many arguements for SetType")
            elif len(sys.argv)<4:
                if len(sys.argv)==2:
                    print("Error: too little arguements for SetType")
                if len(sys.argv)==3:
                    print("Error")
            else:
                d=readFile('user.txt')
                d2=readFile('setType.txt')
                setType=SetType(args.part1,args.part2,d,d2)
                d1=setType.SetType()
                toFile=toFile("setType.txt",d1)
        elif args.part0=="TypeInfo":
            if len(sys.argv)>3:
                print("Error: too many arguements for TypeInfo")
            elif len(sys.argv)<3:
                print("Error: too little arguements for TypeInfo")
            else:
                d=readFile('setType.txt')
                TypeInfo=TypeInfo(args.part1,d)
                TypeInfo.getTypeName()
        elif args.part0=="AddAccess":
            if len(sys.argv)>5:
                print("Error: too many arguements for AddAccess")
            elif len(sys.argv)<5:
                print("Error: too little arguements for AddAccess")
            else:
                d=readFile("access.txt")
                addAccess=AddAccess(args.part1,args.part2,args.part3,d)
                d2=addAccess.AddAcc()
                toFile=toFile("access.txt",d2)
        elif args.part0=="CanAccess":
            if len(sys.argv)>5:
                print("Error: too many arguements for CanAccess")
            elif len(sys.argv)<5:
                print("Error: too little arguements for CanAccess")
            else:
                d=readFile('setDomain.txt')
                d1=readFile('setType.txt')
                d3=readFile('access.txt')
                canAccess=CanAccess(args.part1,args.part2,args.part3,d,d1,d3)
                canAccess.CanAccess()
        elif args.part0:
            print("Error: invalid command "+args.part0)
