## Introduction
Access control mechanisms in operating systems have evolved over the years to include access control lists as well as a variety of mandatory access control (MAC) mechanisms, including multi-level security, integrity levels, type enforcement, and limited forms of role-based access control.

An operating system, however, can only deal with the users and resources it knows about. It manages access between subjects (users) and objects (resources provided by the system, such as files and devices). There’s an underlying assumption that these subjects (users) have accounts on the system and the objects are known to and managed by the system (e.g., files in the file system).

For many applications, however, this is not the case. Applications may run as services that are launched by a specific user. These services, in turn, interact with users who may not have accounts on the system. For instance, you can log onto eBay and interact with it but you don’t have an account on any of the systems that provide the eBay’s service. Similarly, objects may be entities that are also unknown to the operating system, such as fields or tables in a database or media streams.

This is a problem that affects many services.

## Purpose:
design and implement an authentication and access control (authorization) library that can be used by services that need to rely on their own set of users rather than those who have accounts on the computer and manage their own sets of objects and operations on those objects.

## Feautres:
### AddUser(“user”, “password”)
  Define a new user for the system along with the user’s password, both strings.

  The username cannot be an empty string. The password may be an empty string.

#### Test program:
 python3 auth.py AddUser myname mypassword
  
  ---------------------------------
 ### Authenticate(“user”, “password”) 
    Validate a user’s password by passing the username and password, both strings.
#### Test program: 

  python3 auth.py Authenticate myname mypassword
  
  ------------------------------------
### SetDomain(“user”, “domain”)
  Assign a user to a domain. Think of it as adding a user to a group.

  If the domain name does not exist, it is created. If a user does not exist, the function should return an error. If the user already exists in the domain, the command will succeed but take no action. You should never have duplicate users in a domain.

  A user may belong to multiple domains.

  The domain name must be a non-empty string.

#### Test program:

  python3 auth.py SetDomain user domain_name
  
 ------------------------------------------
### DomainInfo(“domain”)
  List all the users in a domain.

  The group name must be a non-empty string.

#### Test program:

  python3 auth.py DomainInfo domain_name
  
-------------------------------------------
### SetType(“objectname”, “type”)
  Assign a type to an object. You can think of this as adding an object to a group of objects of the same type.

  If the type name does not exist, it is created.

  The object can be any non-null string.

#### Test program:

  python3 auth.py SetType object type_name
  
 ----------------------------------------
### TypeInfo(“type”)
  List all the objects that have a specific type, one per line.

  The type name must be a non-empty string.

#### Test program:

  python3 auth.py TypeInfo type_name
  
-----------------------------------------
### AddAccess(“operation”, “domain_name”, “type_name”)
  Define an access right: a string that defines an access permission of a domain to an object. The access permission can be any arbitrary string that makes sense to the service.

  The domain name and type name must be non-empty strings.

  If the domain name or type names do not exist then they will be created. If the operation already exists for that domain and type, it will not be added a second time but it will not be treated as an error.

  This is the key function that builds the access control matrix of domains and types.

#### Test program:

  python3 auth.py AddAccess operation domain_name type_name
  
---------------------------------------------------
### CanAccess(“operation”, “user”, “object”)
  Test whether a user can perform a specified operation on an object.

  The logic in this function in pseudocode is:

  for d in domains(user)
    for t in types(object)
      if access[d][t] contains operation
        return true
  return false
  That is, find all domains for the user and find all types for the object. Then see if any of those domain-type combinations have the desired operation set.

#### Test program:

  python3 auth.py CanAccess operation user object
  
  The program will check whether the user is allowed to perform the specified operation on the object. That means that there exists a valid access right for an operation in some (domain, type) where the user is in domain and the object is in the corresponding type.
  
