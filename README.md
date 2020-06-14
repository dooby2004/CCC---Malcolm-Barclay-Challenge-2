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
The robots.txt file seems to stop browsers from reading ints contents some times. I fixed the file, and am now able to read it on Chrome on windows, but through a virtual machine, it still doesn't want me to read it. It may be something to do with the program I'm using to host the site, and may be fixed when hosted by you.

## Walkthrough
The student should recognise the fake PDF file in the list of links - Keyboard.jpg.pdf. Using the 'file' command on a Linux system would reveal it is definitely a JPEG. They should then be probed to explore the site, and end up in the robots.txt file. This has a short list of files, but the only one with any useful information inside is stegpass.txt, which has a clear name realtated to steganography.

The student would then understand that one of the lines would be the password required for getting data out of the image and would have to make a piece of code like src/Solution.py to use each line in the 'steghide' command, eventually extracting the flag.
