#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <dlfcn.h>
#include <string.h>
// Name: Sreenath Yeragudi
// netID: sry20
// RUID: 192001131

//METHOD FOR EC
int numFile(char* file_Names){
    int number_Files = 1;
    int count = 0;
    while( file_Names[count] != '\0' ){
        if( file_Names[count] == ':' )
            number_Files += 1;
        count += 1;
    }
    return number_Files;
}

char** getFile(char* env_var, int number_Files){
    
    char** file_Names = (char**) malloc(number_Files * sizeof(char*));

    int fC = 0;
    int index = 0;
    int length = 0;
 
    while( env_var[index] != '\0' ){
        if( env_var[index] == ':' ){
            file_Names[fC] = (char*) malloc(sizeof(char) * (length+1));
            file_Names[fC][length] = '\0';
            length = 0;
            index += 1;
            fC += 1;
        }else{
            length += 1;
            index += 1;
        }
    }
    file_Names[fC] = (char*) malloc(sizeof(char) * (length+1));
    file_Names[fC][length] = '\0';
    fC = 0;
    index = 0;
    int str_index = 0;
    while( env_var[index] != '\0' ){
        if( env_var[index] == ':' ){
            fC += 1;
            str_index = 0;
            index += 1;
        }else{
            file_Names[fC][str_index] = env_var[index];
            index += 1;
            str_index += 1;
        }
    }    

    return file_Names;
}

int strComp(char** file_Names,int number_Files,char* file){
    int count = 0;
    for(count = 0; count < number_Files; count++){
        if( strcmp(file, file_Names[count]) == 0 )
            return 0;
    }
    return 1;
}

// your code for readdir goes here
struct dirent* readdir(DIR* dirp){
    char* env_var = getenv("HIDDEN");
    int number_Files = numFile(env_var);
    char** file_Names = getFile(env_var, number_Files);
    struct dirent* (*newReaddir) (DIR* dirp);
    newReaddir = dlsym(RTLD_NEXT, "readdir");
    int Exists = 0;
    struct dirent* curr = newReaddir(dirp);
    while( curr != NULL ){
        if( strComp(file_Names, number_Files, curr->d_name ) != 0 ){
            printf("%s\n",curr->d_name);
        }
        curr = newReaddir(dirp);
    }
    
}