import urllib.request
import re

page = urllib.request.urlopen("http://ogimet.com/display_metars2.php?lugar=SPJC&tipo=ALL&ord=REV&nil=SI&fmt=html&ano=2018&mes=06&day=03&hora=00&anof=2018&mesf=06&dayf=04&horaf=00&minf=59&enviar=Ver")

#variable tipo bytes
respuesta = page.read()

#variable tipo string
respuesta2 = respuesta.decode()

v_i = []
v_f = []
v_d = []

for m in re.finditer('<pre>', respuesta2):
	v_i.append(m.end())
		
for m in re.finditer('</pre>', respuesta2):
	v_f.append(m.start())

print (v_i)
print (v_f)

for i in range(len(v_i)):
	v_d.append(respuesta2[v_i[i]:v_f[i]].replace("\n","").replace("  "," ").replace("  "," ").replace("  "," "))

print (v_d)

