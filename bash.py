import subprocess 

command = "ls ~/" 

Out = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]) 

#out is byte-like object 
#to string 
Out_str =  out.decode('utf-8') 
Out_str_list = Out_str.split() 
