# POW_CREATE
The program called pow-create  creates a proof of work string for a given file:

### Command:
pow-create nbits file



The work is the search for a string that, when suffixed to a hash of the given file (file), will result in a SHA-256 hash (256-bit version of the SHA-2 hash) that contains a certain number (nbits) of leading 0s.

For example, suppose we have the following text in a file called walrus.txt:

The time has come, the Walrus said,
To talk of many things:
Of shoes — and ships — and sealing-wax —
Of cabbages — and kings —
And why the sea is boiling hot —
And whether pigs have wings.
We can use the openssl command on a macOS or Linux system to find its SHA-256 hash:

### Command:
$ openssl sha256 < walrus.txt
66efa274991ef4ab1ed1b89c06c2c8270bb73ffdc28a9002a334ec3023039945



The hash starts with 66ef. The hex digit 6 is 0101 in binary, so we currently have one leading zero bit in this message.

To create a proof of work string with a difficulty of 20 (at least 20 leading zero bits), we run the command:

### Command:
$ pow-create 20 walrus.txt 

File: walrus.txt

Initial-hash: 66efa274991ef4ab1ed1b89c06c2c8270bb73ffdc28a9002a334ec3023039945

Proof-of-work: rftE

Hash: 000005ca35310f45d7ef2b28753a74cf410734b4a5930247d15128d23e419ca0

Leading-zero-bits: 21

Iterations: 1467959

Compute-time: 1.0712 



The pow-create command will:

Create a SHA-256 hash of the specified file.

Convert it to a printable hex string (matching the string produced by the openssl command).

Pick a string that’s a potential proof of work value.

Create a hash of the string representation of the hash in (2) concatenated with the potential proof of work string in (3).

If the hash doesn’t start with at least nbits zero bits (the number supplied by the first argument of the command line) then go back to step (3) and try a different suffix.

For this example, it took almost 1.5 million hashes with different variations of suffixes to find a hash that starts with 20 zero bits (in this particular case, the first hash we found that started with at least 20 leading 0 bits actually contained 21).

The string that we came up with is rftE. This is presented as the proof of work in the Proof-of-work header.

# OUTPUT:
The program will print results to the standard output (stdout) in a standard header format as used by mail headers or HTTP. This is one name-value item per line with each line containing the header name, a colon, one or more spaces, and the value. A header item shall not span multiple lines and the output will not contain blank lines.

The headers your program must produce are:

File:
The name of the file.

Initial-hash:
The SHA-256 hash of the file (as a printable hex value)

Proof-of-work:
The printable string that is your proof of work.

Hash:
The SHA-256 hash of the original string concatenated with the proof of work.

Leading-zero-bits:
The actual number of leading 0 bits in the hash you computed. This value should be greater than or equal to the number requested.

Iterations
The number of different proof-of-work values you had to try before you found one that works.

Compute time:
How long this process took, in seconds (including decimal seconds if appropriate).

Testing your proof of work
We can easily test your program’s result against the data produced by the openssl command

Run your pow-create command:

### Command
$ ./pow-create 20 walrus.txt File: testfiles/walrus.txt

File: testfiles/walrus.txt

Initial-hash: 66efa274991ef4ab1ed1b89c06c2c8270bb73ffdc28a9002a334ec3023039945

Proof-of-work: rftE

Hash: 000005ca35310f45d7ef2b28753a74cf410734b4a5930247d15128d23e419ca0

Leading-zero-bits: 21

Iterations: 1467959

Compute-time: 1.0712 



The only header we care about here is the Proof-of-work value, rftE.

We can check our hash with the one openssl produces by running the openssl command with the sha256 argument. This value should match the Initial-hash header:
 ### Command
$ openssl sha256 <walrus.txt

66efa274991ef4ab1ed1b89c06c2c8270bb73ffdc28a9002a334ec3023039945



Then we append the proof of work to that hash string and find the sha-256 hash of this proof of work string concatenated with the hex string output of the original hash:

### Command
$ echo -n '66efa274991ef4ab1ed1b89c06c2c8270bb73ffdc28a9002a334ec3023039945rftE'|openssl sha256

000005ca35310f45d7ef2b28753a74cf410734b4a5930247d15128d23e419ca0 



We can see that the resulting hash starts with five zeros followed by a 5 (which is 0101 in binary). We have a hash that has 21 leading zero bits, which is at least as good as the 20 we wanted, so the proof of work is valid.


# POW_CHECK

### Command

pow-check powheader file



The command is provided a file the headers (generated by the pow-create command and a file with the original message. It validates the headers against the file.

These are the tests it performs:

It checks the value of the Initial-hash in the header. This is the SHA-256 hash of the message.

It computes the hash of the initial hash string concatenated with the Proof-of-work string in the header. This value should match the Hash header

Finally, it checks that the number in the Leading-bits header exactly matches the number of leading 0 bits in that hash header.

The result of pow-check will be a single line with the message pass or fail. If all conditions passed, simply print a pass message. If any tests failed, specify which of these tests failed before printing a line the fail message. The final line of your output contains this single pass/fail result. Previous lines may identify checks that passed and should identify checks that failed.

# OUTPUT:

We can – and should – do your own tests using openssl but I’ve supplied you with sample files  Download sample filesthat contain header output for various input files. We should produce headers similar to these and your pow-check program should successfully validate all these headers.

For example:

 $ ./pow-check headerfiles/abc.pow-20 testfiles/abc 
 
PASSED: initial file hashes match

PASSED: leading bits is correct

PASSED: pow hash matches Hash header
pass



We should then modify some aspects of the header or test against the wrong file to force pow-check to fail.

Example 1: wrong file
If you provide a file that was not used to generate the header, the initial hashes will not match. We need to detect that the initial-hash value does not match the hash of the file.

$ ./pow-check headerfiles/abc.pow-20 testfiles/alice.txt 

ERROR: initial hashes don't match

       hash in header: 1010a7e761610980ac591359c871f724de150f23440ebb5959ac4c0724c91d91
       
       file hash: 4c2824e599717cc70abe29345d326c0ad4c4564b79bab6570eb0766834829d68
       
ERROR: incorrect Leading-bits value: 20, expected 3

ERROR: pow hash does not match Hash header

        expected: 132d96c356f5a5a17adb53b92716b73bb0b7a1581b85251458f32519a9a3a636
        
        header has: 00000cb2fd2996146d9d8f5d7863d2bc3d39d04beebb214112aa270196753afa
fail

Example 2: bad initial hash value
Appended a 9 to the Initial-hash: header. This is a variation of Example 1. We should detect that the Initial-hash value does not match the hash of the message and not make assumptions about the length of the hash.

$ /pow-check headerfiles/abc.pow-20 testfiles/abc 

ERROR: initial hashes don't match

       hash in header: 1010a7e761610980ac591359c871f724de150f23440ebb5959ac4c0724c91d919
       
       file hash: 1010a7e761610980ac591359c871f724de150f23440ebb5959ac4c0724c91d91
       
PASSED: leading bits is correct

PASSED: pow hash matches Hash header

fail

Example 3: bad Proof of Work value
Changing the  Proof-of-work: header value (to Yi! in this example) will most likely result in a hash with a different number of leading bits than indicated in the header.

$ ./pow-check headerfiles/abc.pow-20 testfiles/abc 

PASSED: initial file hashes match

ERROR: Leading-zero-bits value: 20, but hash has 0 leading zero bits

ERROR: pow hash does not match Hash header

        expected: b7c207d21d60e3778d49a8c46c2ee477f1d08153ca0c99c4b6295625c44db338
        
        header has: 00000cb2fd2996146d9d8f5d7863d2bc3d39d04beebb214112aa270196753afa
fail

Example 4: bad count of leading zero bits
The Leading-zero-bits: header value was changed to 23 from 20.

$ ./pow-check headerfiles/abc.pow-20 testfiles/abc 

PASSED: initial file hashes match

ERROR: Leading-zero-bits value: 23, but hash has 20 leading zero bits

PASSED: pow hash matches Hash header

fail

Example 5: missing header
We should check for presence and validity of the following headers:

Initial-hash:

Proof-of-work:

Leading-zero-bits:

Hash:

If any are missing, the program will fail the check. The File, Iterations, and Compute-time headers are just informative and don't need to be checked. Here's an example of a missing Initial-hash: header.

ERROR: missing Initial-hash in header

PASSED: leading bits is correct

PASSED: pow hash matches Hash header

fail