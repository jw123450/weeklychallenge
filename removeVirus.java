import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;


public class removeVirus {
	public static String rv(String PCfiles) {
		PCfiles = PCfiles.replaceFirst("^PC Files: ", "");
		String cleanerFiles = "";
		String separator = ", ";
		List<String> cleanFiles = new ArrayList<>();
		List<String> PCfileslist = new ArrayList<>(Arrays.asList(PCfiles.split(separator)));
		for (String s : PCfileslist){
			if (!((s.contains("virus") || s.contains("malware"))) || ((s.contains("antivirus") || s.contains("notvirus")))){
				cleanFiles.add(s);
			}
		}
		if (!(cleanFiles.isEmpty())) {
			cleanerFiles = "PC Files: " + String.join(", ", cleanFiles);
			return cleanerFiles;
		}
		else {
			return "PC Files: Empty";
		}
	}
	public static void main(String[] args) {
		removeVirus testing = new removeVirus();
		System.out.println(removeVirus.rv("PC Files: spotifysetup.exe, virus.exe, dog.jpg"));
		System.out.println(removeVirus.rv("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe"));
		System.out.println(removeVirus.rv("PC Files: notvirus.exe, funnycat.gif"));
	}
}