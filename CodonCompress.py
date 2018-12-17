import time
start=time.time()

a='00'
g='01'
c='10'
t='11'
count=0
def display(char):
    if char=='a':
        d=a
    elif char=='g':
        d=g
    elif char=='c':
        d=c
    else:
        d=t
    return d

def revers(s):
    return s[::-1]

file1=open('e:\\gmn\\dna\\vaccg.txt','r')
file2=open('e:\\gmn\\dna\\encodseq.txt','w')
file3=open('e:\\gmn\\dna\\threechar.txt','w')
word1=''
icount=0
pcount=0
scount=0
ftcount=0
ltcount=0
flcount=0
dcount=0
ocount=0
tcount=0
ncount=0

while 1:
    word=file1.read(1)	#read 3 character at a time
    count+=1
    if word=='\n':
        word=file1.read(1)
        ncount+=1
    words=file1.read(1)
    if words!='\n':
        word=word+words
        count+=1
    words=file1.read(1)
    if words!='\n':
        word=word+words
        count+=1
    
    if not word:break	#check for end of file
    wordr=revers(word)
    file3.write(word),
    file3.write(' '),
    l=len(word)
    if l==1:
        if word=='\n':
            break            
        code=display(word[0])
        ocount=ocount+1
    elif l==2:
        code=display(word[0])+display(word[1])
        tcount=tcount+1
    else:
        if word1==word:     #check for identical codons
            code='0'+' '
            icount+=1
        elif word1==wordr:  #check for palindrome codons
            code='1'+' '
            pcount+=1
        elif word[0]==word[1] and word[1]==word[2]:	#checking for all the three character
            code=display(word[0])+' '
            scount=scount+1            
        elif word[0]==word[2]:	#check for first and last character
            code=display(word[0])+display(word[1])+' '
            flcount+=1
        elif word[0]==word[1]:	#check for first two character
            code='0'+display(word[0])+display(word[2])+' '
            ftcount+=1
        elif word[1]==word[2]:	#check for last two character
            code='1'+display(word[0])+display(word[1])+' '
            ltcount+=1
        else:	#check for distinct
            code=display(word[0])+display(word[1])+display(word[2])+' '
            dcount+=1
    file2.write(code)
    word1=word

print 'icount=', icount
print 'pcount=', pcount
print 'scount=', scount
print 'ftcount=', ftcount
print 'ltcount=', ltcount
print 'flcount=', flcount
print 'dcount=', dcount
print 'ocount=', ocount
print 'tcount=', tcount
print 'count=', count
print 'ncount=',ncount
file1.close()
file2.close()
end=time.time()
print end-start
