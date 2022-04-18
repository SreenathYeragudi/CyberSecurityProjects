#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <dlfcn.h>
// Name: Sreenath Yeragudi
// netID: sry20
// RUID: 192001131
// your code for time() goes here
int v = 0;
time_t time(time_t *tlocation){
    if( v == 0 ){
        struct tm tmi;
        memset(&tmi, 0, sizeof(struct tm));
        if( strptime("2021-1-3 12:00:00", "%Y-%m-%d %H:%M:%S", &tmi) == NULL ){
            printf("error setting struct\n");
            return 0;
        }
        if(tlocation == NULL){
            tlocation = (time_t*) malloc(sizeof(time_t));
        }
        *tlocation = mktime(&tmi);
        v = 1;
        return *tlocation;
    }
    time_t (*new_time) (time_t* tlocation);
    new_time = dlsym(RTLD_NEXT, "time");
    return new_time(tlocation);
}