# GOAL
There are various ways of hiding content. It could be placed in obscure parts of the file system that might not be searched regularly. A file might be set to be hidden, but this attribute can be changed easily. On Linux systems, files whose names begin with a dot are not listed by default unless you use a -a option to the ls command. Clearly, this isn’t a good way of hiding files. The ideal way of hiding files is to modify the kernel to never report of their existence but this requires getting privileges to modify the kernel.
A way of hiding files in user space is to modify library functions that read directory contents. This way, programs that show directory contents will not see the file but someone who knows about it can open it.
In this project, I use function interposition to hide the presence of files from commands such as ls and find.

# LS Function
  ## GOAL OF FUNCTION:
    The standard library function for reading directories on Linux is readdir (Links to an external site.), which is built on top of the getdents (Links to an external site.) system call. Programs such as ls, find, sh, zsh, and others use readdir to read contents of directories.
    The program will interpose readdir so that it will hide a secret file whose name is set by an environment variable. You do this by setting the LD_PRELOAD environment variable:
                                        export LD_PRELOAD=$PWD/hidefile.so
    This tells the system to load the functions in the specified shared library before loading any others and to give these functions precedence.
    
 ## WHAT IT WILL DO:
    Call the real version of readdir
    Check if the returned file name matches the name in the environment variable HIDDEN
    If it does, call readdir again to skip over this file entry.
    Return the file data to the calling program.
## COMPLING TESTING
    If you run
	                      make
    the make program will compile the file hidefile.c into a shared library hidefile.so. 
    
    If you run
                        make test
    the make program will compile the files (if necessary), create two sample files named secret-1.txt and secret-2.txt and test the program by setting the environment variable HIDDEN to secret-1.txt, then secret-2.txt, and then deleting it – running the lscommand each time with the shared library preloaded. 

# FIND FUNCTION
  # WHAT I WILL DO:
      This program uses the standard C library (glibc) time (Links to an external site.) function to get the system time. The time function returns the number of seconds since the Linux Epoch (the start of January 1, 1970 UTC).
      The program will create an alternate version of the time() C library function that will return a value within a time window that will pass the program’s validation check.
      I will use Linux’s LD_PRELOAD mechanism to take control and replace the standard time library function with your own version.

  # HOW TO RUN IT
    You will then compile this file into a shared library called newtime.so. 
    You can run:
                                  make
    to compile the library. 
    You can then preload this shared library by setting the environment variable:
                        export LD_PRELOAD=$PWD/newtime.so
    and then run the program normally:

                        ./unexpire
    If  correct, you will see a message stating:

              PASSED! You reset the time successfully!
    You can also test the program by running

              make test
    If you set LD_PRELOAD globally, don’t forget to
            unset LD_PRELOAD
