import markdown, glob,os,shutil,pathlib
import xml.etree.ElementTree as ET

def useTemplate(passedParams):
	global top
	global end
	try:
		with open("templates/" + passedParams[0] + "/topmatter.html", "r", encoding="utf-8") as template:
			top = template.read() + top
		with open("templates/" + passedParams[0] + "/bottommatter.html", "r", encoding="utf-8") as template2:
			end = end + template2.read()			
	except FileNotFoundError:
		print("|--- [WARNING] Directive useTemplate failed - template " + passedParams[0] + " invalid or not found.")
	try:
		with open("templates/" + passedParams[0] + "/template.jcnf", "r", encoding="utf-8") as template3:
			for line in template3.readlines():
				doCmd(line)
	except:
		pass
		
		
def style(passedParams):
	global head
	try:
		with open("styles/" + passedParams[0] + ".css", "r", encoding="utf-8") as template:
			head = "<style>" + template.read() + "</style>" + head
	except FileNotFoundError:
		print("|--- [WARNING] Directive linkStyle failed - stylesheet " + passedParams[0] + " not found.")

	
def script(passedParams):
	global head
	try:
		with open("scripts/" + passedParams[0] + ".js", "r", encoding="utf-8") as template:
			head = "<script>" + template.read() + "</script>" + head
	except FileNotFoundError:
		print("|--- [WARNING] Directive linkScript failed - scriptfile " + passedParams[0] + " not found.")

		
def comment(passedParams):
	pass
		
commands = {"useTemplate": useTemplate, "linkStyle": style, "linkScript": script, "#": comment}


def doCmd(cmd):
	global commands
	if cmd != "":
		fn = commands[cmd.split()[0]]
		try:
			fn(cmd.split()[1:])
		except:
			print("|--- [WARNING] Ignored directive '" + cmd + "' due to unknown error, maybe command is not in valid scope?")
		
	


	
print("START BUILD")

print("|-Checking if buildout directory exists...", end="")
try:
	shutil.rmtree("buildout")
	print("yes \n|-Removing the buildout directory")
except FileNotFoundError:
	try:
		os.rmdir("buildout")
		print("yes \n|-Removing the buildout directory")
	except FileNotFoundError:
		print("no")


print("|-Checking if global.jcnf exists...", end="")
try:
	with open("global.jcnf", "r", encoding="utf-8") as gblconf:
		lines = gblconf.readlines()
		scope = 1
		for line in lines:
			doCmd(line.lstrip())
	print("yes \n|-Following directives in global.jcnf")
except FileNotFoundError:
	print("no")


print("|-Checking if all.jcnf exists...", end="")
try:
	allconf = open("all.jcnf", "r", encoding="utf-8")
	allconftext = allconf.read()
	allconf.close()
	print("yes")
except FileNotFoundError:
	allconftext = str()
	print("no")


done = 0
skipped = 0

for filename in glob.iglob('content/**/*.jcpd', recursive=True):
     text = ""
     top  = ""
     head = ""
     end = ""
     strippedname = filename[:-5].replace("content","")
     for line in allconftext.split("\n"):
        doCmd(line.lstrip())
     with open(filename, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
        for line in lines:
            scope = 3
            if line.lstrip()[:2] == "@@":
                doCmd(line.lstrip()[2:])
            else:
               text = text + line    
			
        
        content = "<html> <head>" + head + "</head> <body>" + top + markdown.markdown(text) + end + "</body> </html>"
        
        directory_structure = strippedname.rsplit("/",1)[1:]
        slash_delimited_dir = "buildout/"
        for i in directory_structure:
            slash_delimited_dir  = slash_delimited_dir + "/" + "i"
        pathlib.Path(slash_delimited_dir).mkdir(parents=True, exist_ok=True)
        f = open(("buildout/"+strippedname+".html"), "w+")
        f.write(content)
        f.close()
        print("|- Built page '" + strippedname + "'")
        done=done+1

try:
	shutil.copytree("verbatim", "buildout/verbatim")
except:
	pass

print("BUILD DONE (built " + str(done) + ", skipped " +str(skipped) + ")")
