"""
File Mode:
=========

r(read)  -> To read, File must exists to read. If file is not there then we will get
            FileNotFoundError
w(write)  -> To write . If the file exists, the content of the file gets removed and
            new content will be written.If the file does not exists then it will create
            the file and start writing into it
a(append)  -> Append. To write the content along with existing content fo the file.
                if the file is not there, it will create and write into it
r+(read-write) -> read and write. First we should read the existing content and write the
                    new data into it
w+(write-read)   -> write and read whatever been written
rb(read binary)   -> special file (image/video/audio)
wb(write binary)

READ:
    read, readline, readlines
WRITE:
    write, writelines
"""

# with open('days.txt','r') as fo:
#     #print(fo.read())
#     #print(fo.readline())
#     for x in fo.readlines()[1:6]:
#         print(x,end='')

# with open('tech.txt','w') as wf:
#     #wf.write("Machine Learning")
#     wf.writelines(["C\n","CPP\n","Java\n","Python\n","Perl"])

# with open('tech.txt','a') as af:
#     af.writelines(["\nUnix\n",".Net\n","golang"])

# with open("days.txt","r+") as rfo:
#     print(rfo.read())
#     rfo.writelines(["\nJan\n","Feb\n","Mar"])

# with open("days.txt","r+") as rfo:
#     rfo.writelines(["Chennai\n","Bangalore"])
#     print(rfo.read())

# with open("days.txt","w+") as wfo:
#     wfo.writelines(["India\n","China\n","Singapore\n","Australia"])
#     wfo.seek(0,0)
#     print(wfo.read())

# with open(r"C:\Users\DELL\Pictures\bird.jpg",'rb') as ri:
#     with open(r"C:\Users\DELL\Pictures\bird_new.jpg",'wb') as wi:
#         wi.write(ri.read())