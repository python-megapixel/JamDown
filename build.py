import markdown, glob,os,shutil
import xml.etree.ElementTree as ET

def useTemplate(passedParams):
	global top
	global end
	with open("templates/" + passedParams[0] + "/topmatter.html", "r", encoding="utf-8") as template:
		top = template.read() + top
	with open("templates/" + passedParams[0] + "/bottommatter.html", "r", encoding="utf-8") as template2:
		end = end + template2.read()
	return 0
		
def style(passedParams):
	with open("styles/" + passedParams[0] + ".css", "r", encoding="utf-8") as template:
		head = "<style>" + template.read() + "</style>" + top
		

commands = {"useTemplate": useTemplate, "linkStyle": style}

def doCmd(cmd):
	global commands
	fn = commands[cmd.split()[0]]
	return fn(cmd.split()[1:])
		
	


	
print("START BUILD")

print("|-Checking if buildout directory exists...", end="")
try:
	shutil.rmtree("buildout")
	print("yes \n|-Removing the buildout directory")
except:
	print("no")


done = 0
skipped = 0

for filename in glob.iglob('content/**/*.jcpd', recursive=True):
     text = ""
     top  = ""
     head = ""
     end = ""
     strippedname = filename[:-5].replace("content","")
     with open(filename, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
        for line in lines:
            if line.lstrip()[:2] == "@@":
               doCmd(line.lstrip()[2:])
            else:
               text = text + line    
			
        
        content = "<html> <head>" + head + "</head> <body>" + top + markdown.markdown(text) + end + "</body> </html>"
        
        directory_structure = strippedname.rsplit("/",1)[1:]
        slash_delimited_dir = "buildout/"
        for i in directory_structure:
            slash_delimited_dir  = slash_delimited_dir + "/" + "i"
        os.makedirs(slash_delimited_dir)
        f = open(("buildout/"+strippedname+".html"), "w+")
        f.write(content)
        f.close()
        print("|- Built page '" + strippedname + "'")
        done=done+1

       

print("BUILD DONE (built " + str(done) + ", skipped " +str(skipped) + ")")


