import java.util.*;
import java.io.*;

public class Zimmer {
  
  private ArrayList<String> Zimmergenossen = new ArrayList<String>();
  private ArrayList<String> ungewollteZimmergenossen = new ArrayList<String>();
  
  public Zimmer(String ersteZimmerperson) {
    Zimmergenossen.add(ersteZimmerperson);
  }
  
  public void addZimmergenossen(String name) {
    Zimmergenossen.add(name);
  }
  
  public void addUngewolltenZimmergenossen(String name) {
    ungewollteZimmergenossen.add(name);
  }
  
  public ArrayList<String> getZimmergenossen() {
    return Zimmergenossen;
  }  
  
  public void writeZimmergenossen(BufferedWriter pWriter) {
    try {
      for (int i = 0; i < Zimmergenossen.size(); i++) {
        System.out.println(Zimmergenossen.get(i));
        pWriter.write(Zimmergenossen.get(i) + System.getProperty("line.separator"));
      }  
    } catch(Exception e) {
      System.out.println("Datei konnte nicht geschrieben werden!");
    }
  }
  
  public void writeZimmergenossen() {
    try {
      for (int i = 0; i < Zimmergenossen.size(); i++) {
        System.out.println(Zimmergenossen.get(i));
      }  
    } catch(Exception e) {
      System.out.println("Datei konnte nicht geschrieben werden!");
    }
  }
  
  public void delete() {
    this.Zimmergenossen.clear();
    this.ungewollteZimmergenossen.clear(); 
  }
  
  /**
  * 
  * @param name
  *            Die zu ueberpruefende Person
  * @return Gibt es die Person name schon in diesem Zimmer?
  */
  public boolean existsZimmergenosse(String name) {
    boolean exists = false;
    for (int i = 0; i < Zimmergenossen.size(); i++) {
      if (Zimmergenossen.get(i).equals(name)) {
        exists = true;
        break;
      }
    }
    return exists;
  }
  
  public boolean istPersonUngewollt(String name) {
    boolean ungewollt = false;
    for (int i = 0; i < ungewollteZimmergenossen.size(); i++) {
      if (ungewollteZimmergenossen.get(i).equals(name)) {
        ungewollt = true;
        break;
      }
    }
    return ungewollt;
  }
  
  /**
  * Testet, ob zwei Zimmer sich verbinden koennen
  * 
  * @param zimmer
  *            das zweite Zimmer der Verbindung
  * @return koennen sich beide Zimmer verbinden?
  */
  public boolean kannVerbinden(Zimmer zimmer) {
    for (int i = 0; i < this.getZimmergenossen().size(); i++) {
      if (zimmer.istPersonUngewollt(this.getZimmergenossen().get(i))) {
        return false;
      }
    }
    for (int i = 0; i < zimmer.getZimmergenossen().size(); i++) {
      if (this.istPersonUngewollt(zimmer.getZimmergenossen().get(i))) {
        return false;
      }
    }
    return true;
  }
  
  /**
  * fügt das Parameter-Zimmer dem Zimmer hinzu und loescht alle Personen
  * 
  * @param zimmer
  *            Das zweite Zimmer der Verbindung
  */
  public void verbindeZimmer(Zimmer zimmer) {
    for (int i = 0; i < zimmer.Zimmergenossen.size(); i++) {
      if (!this.existsZimmergenosse(zimmer.getZimmergenossen().get(i))) {
        this.addZimmergenossen(zimmer.getZimmergenossen().get(i));
        System.out.println(zimmer.getZimmergenossen().get(i) + " wurde dem Zimmer hinzugefügt.");
      }
    }
    for (int i = 0; i < zimmer.ungewollteZimmergenossen.size(); i++) {
      if (!this.istPersonUngewollt(zimmer.ungewollteZimmergenossen.get(i))) {
        
        this.addUngewolltenZimmergenossen(zimmer.ungewollteZimmergenossen.get(i));
        System.out.println(zimmer.ungewollteZimmergenossen.get(i) + " wurde der u-Liste hinzugefügt.");
      }
    }
  }
  
}
