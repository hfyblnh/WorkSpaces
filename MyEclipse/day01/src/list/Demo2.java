package list;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map.Entry;
import java.util.Set;

public class Demo2 {
	public static void main(String[] args) {
		
		ArrayList<String> list = new ArrayList<String>();	
		list.add("����");
		list.add("����");
		list.add("����");

		//ʹ��get��������
		System.out.println("=====get��������=====");
		for (int i = 0; i < list.size(); i++) {
			System.out.println(list.get(i) + ",");
		}
		
		HashSet<String> set = new HashSet<String>();
		set.add("��ǿ");
		set.add("����");
		set.add("������");

		//ʹ�õ���������
		System.out.println("=====����������=====");
		Iterator<String> it = set.iterator();
		while (it.hasNext()) {
			System.out.println(it.next() + ",");			
		}
		
		//��ǿforѭ��
		System.out.println("=====��ǿforѭ��=====");
		for (String item : set) {
			System.out.println(item + ",");
		}
		
		HashMap<String, String> map = new HashMap<String,String>();
		map.put("�Ƿ�", "001");
		map.put("����", "002");
		map.put("����", "003");
		Set<Entry<String, String>> entrys = map.entrySet();
		for (Entry<String, String> entry : entrys) {
			System.out.println("{" + "����" + entry.getKey() + ", " + "ֵ��" + entry.getValue() + "}");
		}
	}
}
