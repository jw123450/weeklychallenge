def removevirus(files: str) -> str:
    filelist = files.removeprefix('PC Files: ').split(", ")
    cleanfiles = []
    for f in filelist:
    	if not ("virus" in f or "malware" in f) or ("antivirus" in f or "notvirus" in f):
    		cleanfiles.append(f)
    return 'PC Files: ' + (", ".join(cleanfiles) if cleanfiles else "Empty")

print(removevirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"))
print(removevirus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe "))
print(removevirus("PC Files: notvirus.exe, funnycat.gif"))
