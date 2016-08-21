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
		list.add("张三");
		list.add("李四");
		list.add("王五");

		//使用get方法遍历
		System.out.println("=====get方法遍历=====");
		for (int i = 0; i < list.size(); i++) {
			System.out.println(list.get(i) + ",");
		}
		
		HashSet<String> set = new HashSet<String>();
		set.add("宝强");
		set.add("马蓉");
		set.add("经纪人");

		//使用迭代器遍历
		System.out.println("=====迭代器遍历=====");
		Iterator<String> it = set.iterator();
		while (it.hasNext()) {
			System.out.println(it.next() + ",");			
		}
		
		//增强for循环
		System.out.println("=====增强for循环=====");
		for (String item : set) {
			System.out.println(item + ",");
		}
		
		HashMap<String, String> map = new HashMap<String,String>();
		map.put("乔峰", "001");
		map.put("段誉", "002");
		map.put("虚竹", "003");
		Set<Entry<String, String>> entrys = map.entrySet();
		for (Entry<String, String> entry : entrys) {
			System.out.println("{" + "键：" + entry.getKey() + ", " + "值：" + entry.getValue() + "}");
		}
	}
}
