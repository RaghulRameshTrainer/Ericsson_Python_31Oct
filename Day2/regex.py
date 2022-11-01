import re
'''
match
search
findall
sub
split
compile-finditer
'''

line="pet:cat i love cat pet:dog i love dog"
#matches=re.match("pet:cat",line)
#matches=re.match("pet:...",line)
#matches=re.match("pet:.{3}",line)
#matches=re.match("PET:...",line,re.I)
#print(matches.group())

#matches=re.search("pet:dog",line)
#matches=re.search("pet:...",line)
#print(matches.group())

#matches=re.findall("pet:...",line)
# matches=re.findall("Pet:...",line,re.I)
# print(matches)

#print(re.sub("love","like",line))
#print(re.split(" ",line))

mystring="""
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWZYZ
1234567890


~!@#$%^&*()_+

https://www.google.com
http://www.google.com
https://google.com
https://www.google.co.in

Ha HaHa

raghulramesh@gamil.com
ramesh_ramesh@yahoo.com
raghul.ramesh@outlook.com
ramesh@hotmail.com

456-665-3345
344 535 4345
454.432.2434
324_335_5353
"""
pattern=re.compile(r"\d{3}[\-\.\s]\d{3}[\-\.\s]\d{4}")
matches=pattern.finditer(mystring)
#pattern=re.compile('.')
#pattern=re.compile("https?://(www\.)?google\.com?(\.in)?")
#pattern=re.compile(r"\bHa\b")
#pattern=re.compile(r"(\w+\.)?\w+@\w+\.com")


for i in matches:
    print(i.group())