malcolm.barclay2004@gmail.com

# Imposter PDFs

## Flag
Flag: H1dD3n_S1gN4lz

## Briefing
Go to [url] and find the flag hidden within one of the files.

By dooby2004.

## Infrastructure
- Host the web files within the ZIP file.
- PHP is required on the hosting service.

## Risks
The UserID header is used to access a user file, so file inclusion can be exploited to access files outside of the main directory, however, I've made the PHP check whether the input is alphanumeric and exit the script if not, to prevent the use of '.' and '/' to traverse the file system.

## Walkthrough
The student should recognize that the UserID header is a 4-digit hexadecimal value and should create a piece of code similar to src/Solution.py to attempt each header up to the value of the given page or the value of FFFF and check for the page with 'Keri Benton' in it. This should give the header as 56C8.

When on the page, the Student should explore the source code to realise that one of the links is hidden from them and follow it to reach a file with the flag - ./Files/Establishment.txt.
