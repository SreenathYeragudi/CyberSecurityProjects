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

# Output
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
You can easily test your program’s result against the data produced by the openssl command

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
