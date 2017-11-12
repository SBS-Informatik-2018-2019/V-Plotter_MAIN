package de.zimmerbelegung.java;

import java.util.*;

public class Zimmer {
	
	private ArrayList<String> Zimmergenossen = new ArrayList<>();
	private ArrayList<String> ungewollteZimmergenossen = new ArrayList<>();

	public Zimmer(String ersteZimmerperson) {
		Zimmergenossen.add(ersteZimmerperson);
	}
	
	public void addZimmergenossen(String name) {
		Zimmergenossen.add(name);
	}
	
	public void addUngewolltenZimmergenossen(String name) {
		ungewollteZimmergenossen.add(name);
	}
	
	public void writeZimmergenossen() {
		for(int i = 0; i < Zimmergenossen.size(); i++) {
			System.out.println(Zimmergenossen.get(i));
		}
	}
	
	public boolean existsZimmergenosse(String name) {
		boolean exists = false;
		for(int i = 0; i < Zimmergenossen.size(); i++) {
			if(Zimmergenossen.get(i).equals(name)) {
				exists = true;
				break;
			}
		}
		return exists;
	}
	
	public boolean istPersonUngewollt(String name) {
		boolean ungewollt = false;
		for(int i = 0; i < ungewollteZimmergenossen.size(); i++) {
			if(ungewollteZimmergenossen.get(i).equals(name)) {
				ungewollt = true;
				break;
			}
		}
		
		return ungewollt;
	}
	

}
