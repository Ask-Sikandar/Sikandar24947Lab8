toprint = input("Enter your text to convert in Ascii code: ")
with open("DMEM3", "w") as f:
    f.write("v2.0 raw\n")
    for x in range(len(toprint)):
        f.write((str(ord(toprint[x]))).zfill(8)+"\n")
print("Done dana done")