import xml.etree.ElementTree as ET
tree = ET.parse('../data/text/in/01-crText.xml')
root = tree.getroot()


for l in root:
    l_id = l.attrib.get('{http://www.w3.org/XML/1998/namespace}id')
    n = 0
    print(l_id)
    #print(l.attrib)
    for w in l:
        n = n + 1
        w.set('xml:id','' + l_id + '.' + str("{0:0=2d}".format(n)) + '')
        print("s")


tree.write('output.xml')