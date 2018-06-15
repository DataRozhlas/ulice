streetnames = []
streetnames_annotated = []
with open("ova_ulice.csv") as file:
    for line in file:
        name = line.split(";")[10]
        if name[-3:] not in ["ská", "cká", "ová"] and name[:2] not in ["U ", "K ", "V "] and name[:3] not in ["Na ", "Za ", "Ke ", "Ve "] and name[:4] not in ["Pod ", "Nad "] and name != "":
            streetnames.append(name)

streetnames = set(streetnames)

unan = 0
for name in streetnames:    
    if name[-3:] == "ova":
        streetnames_annotated.append((name,"M"))
    elif name[-3:] == "ého":
        streetnames_annotated.append((name,"M"))
    elif name[-3:] == "ové":
        streetnames_annotated.append((name,"F"))
    else:
        unan+=1
        streetnames_annotated.append((name," "))
print(streetnames_annotated)
with open("ova_ulice_filtered.csv", "w", encoding="utf8") as file:
    for entry, gender in streetnames_annotated:
        file.write(entry + ";" + gender + "\n")