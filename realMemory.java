import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class realMemory {
	public static void memory(String origMem){ 
		List<String> mem = new ArrayList<>();
		mem.add(origMem.substring(0, origMem.length() -2));
		mem.add(origMem.substring(origMem.length() -2, origMem.length()));
		double size = 0.0;
		String result = "";
		if (origMem.contains("GB")) {
			size = Math.round(Double.parseDouble(mem.get(0)) * 0.93 * 1000.0) / 1000.0;
			if (size < 1) {
				size = (int)(1000 * size);
		   		mem.set(1, "MB");
		   		result = String.format("%.0f", size) + mem.get(1);
		   	}else {
				result = String.format("%.2f", size) + mem.get(1);
		   	}

		} else if (origMem.contains("MB")) {
			size = Math.round(Double.parseDouble(mem.get(0)) * 0.93);
			result = String.format("%.0f", size) + mem.get(1);

		}

		System.out.println(result);
	}
	public static void main(String[] args) {
		realMemory.memory("21GB");
		realMemory.memory("32GB");
		realMemory.memory("2GB");
		realMemory.memory("512MB");
		realMemory.memory("1.1GB");
		realMemory.memory("1.01GB");
	}
}