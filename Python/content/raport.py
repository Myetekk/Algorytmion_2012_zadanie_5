plik_in = open("output/output.txt", "r")
plik_out = open("raport.html", "w")
zawartosc = plik_in.readlines()

table = "<table>"
for j in range(4):
    table += "\n  <tr>"
    for i in range(4):
        table += "\n    <td>" + str(zawartosc[i+j]) + "    &nbsp;\n" + "    </td>\n"
    table += "  </tr>\n"
table += "</table>\n\n"
table2 = "<table>" + "\nŻeby rozwiazać tabliczke potrzeba: " + str(zawartosc[16]) + " ruchów \n</table>\n "

plik_out.write(table)
plik_out.write(table2)
plik_in.close()
plik_out.close()
