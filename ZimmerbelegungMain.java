import java.io.*;
import java.util.ArrayList;

public class ZimmerbelegungMain{
  
  private static ArrayList<Zimmer> zimmerliste = new ArrayList<Zimmer>();
  private static File fileIn = new File("zimmerbelegung.txt");
  private static FileReader fr;
  private static BufferedReader reader;
  private static File fileOut = new File("zimmerbelegung_loesung.txt");
  private static FileWriter fw;
  private static BufferedWriter writer;
  
  public static void main(String[] args) {
    
    try {
      fr = new FileReader(fileIn);
      reader = new BufferedReader(fr);
      fw = new FileWriter(fileOut);
      writer = new BufferedWriter(fw);
      
      if (checkPersonGrouping()) {
        System.out.println("Es funktioniert!");
        int zaehler = 0;
        for (int i = 0; i < zimmerliste.size(); i++) { 
          if(!zimmerliste.get(i).getZimmergenossen().isEmpty()) {
            zaehler++;
            System.out.println("Das " + zaehler + ". Zimmer: ");  
            writer.write("Zimmer " + (zaehler) + ":" + System.getProperty("line.separator"));
            zimmerliste.get(i).writeZimmergenossen(writer);
            
          }
        }
      } else {
        System.out.println("Diese Schueler koennen sich auf keine Zimmerbelegung einigen!");
        writer.write("Die Kinder können sich auf keine Zimmerbelegung einigen!");
      }
      
      reader.close();
      writer.close();
    } catch (IOException e) {
      System.err.println("Die Datei " + fileIn + " konnte nicht bearbeitet werden!");
    }
    
  }
          
  private static boolean checkPersonGrouping() {
    String line;
    try {
      // Teil 1
      line = reader.readLine();
      if (line == null) {
        System.out.println("Die Datei ist fertig gelesen!");
        return true;
      }
      if (line.equals("")) {
        line = reader.readLine();
      }
      
      String name = line;
      // Die erste Zeile ist immer der Name der Person
      System.out.println("Eine neue Person: " + name);
      
      ArrayList<Integer> zimmertemp = new ArrayList<Integer>();
      for (int i = 0; i < zimmerliste.size(); i++) {
        // Ist die Person schon in einem Zimmer?
        if (zimmerliste.get(i).existsZimmergenosse(name)) {
          System.out.println("Die Person " + name + " gehoert Zimmer " + i + " an.(Meth1)");
          zimmertemp.add(i);
        }
      }
      line = reader.readLine();
      // die Praeferiertenliste der einen Person
      line = line.substring(2);
      if (!line.isEmpty()) {
        String[] temp2 = line.split(" ");
        for (int i = 0; i < zimmerliste.size(); i++) {
          for (int j = 0; j < temp2.length; j++) {                 
            if (zimmerliste.get(i).existsZimmergenosse(temp2[j])) {
              if (zimmerliste.get(i).istPersonUngewollt(name)) {
                System.out.println(
                "Zimmer " + i + " mag nicht, dass " + temp2[j] + " zu ihnen kommt!");
                return false;
              } else {
                System.out.println("Person " + name + " kann in Zimmer  " + i + " dazukommen.(Meth2)");
                boolean zimmerExists = false;
                for (int k = 0; k < zimmertemp.size(); k++) {
                  if (i == zimmertemp.get(k)) {
                    zimmerExists = true;
                  }
                } 
                if (!zimmerExists) { 
                  zimmertemp.add(i);
                }
              } 
            }
          }
        } 
      }
      // Teil 2
      if (zimmertemp.size() == 1) {
        // die Person gehört definitiv in dieses eine Zimmer
        if (!zimmerliste.get(zimmertemp.get(0)).existsZimmergenosse(name)) {
          zimmerliste.get(zimmertemp.get(0)).addZimmergenossen(name);
          System.out.println("Dem Zimmer " + zimmertemp.get(0) + " wird Person " + name + " hinzugefügt.");
        }         
        if (!schreibePräferenzen(line, zimmertemp.get(0))) {
          // Die Präferenzen werden geschrieben: Fehler
          System.out.println("Es funktioniert nicht (Person einfuegen1) !");
          return false;
        }
      } else if (zimmertemp.size() > 1) {
        // kann man diese Zimmer verbinden?
        if (!zimmerverbindenMoeglich(zimmertemp)) {
          System.out.println("Zimmer verbinden nicht möglich.");
          return false;
        } 
        
        // man kann die Zimmer verbinden
        for(int i = 1; i < zimmertemp.size(); i++) {
          // hier werden alle Zimmer dem ersten zugefügt
          zimmerliste.get(zimmertemp.get(0)).verbindeZimmer(zimmerliste.get(zimmertemp.get(i)));
          System.out.println(zimmertemp.get(i) + " wurde dem Zimmer " + zimmertemp.get(0) + " hinzugefügt.");
          //Hier wird die Liste nicht gelöscht!?
          zimmerliste.remove(zimmertemp.get(i));
          zimmerliste.get(zimmertemp.get(i)).delete();
          System.out.println(zimmertemp.get(i) + " wurde gelöscht.");
          zimmertemp.remove(i);
        }
        if (!zimmerliste.get(zimmertemp.get(0)).existsZimmergenosse(name)) {
          zimmerliste.get(zimmertemp.get(0)).addZimmergenossen(name);
          System.out.println("Dem Zimmer " + zimmertemp.get(0) + " wird Person " + name + " hinzugefügt.");
        }   
        if (!schreibePräferenzen(line, zimmertemp.get(0))) {
          // Die Präferenzen werden geschrieben: Fehler
          System.out.println("Es funktioniert nicht (Person einfuegen1) !");
          return false;
        }
      } else {  
        // ein neues Zimmer wird angelegt
        System.out.println("Ein neues Zimmer mit " + name);
        zimmerliste.add(new Zimmer(name));
        if (!schreibePräferenzen(line, zimmerliste.size() - 1)) {
          // Die Präferenzen werden geschrieben: Fehler
          System.out.println("Es funktioniert nicht (Zimmer erstellen) !");
          return false;
        }
      }
      // Teil 3
      if (!checkPersonGrouping()) {
        // falls die nächste Zeile eine Ungereimtheit findet
        System.out.println("Es funktioniert nicht (Neue Person)!");
        return false;
      }
      
    } catch (IOException e) {
      System.err.println("Fehler beim Bearbeiten der Namenszeile!");
      e.printStackTrace();
    }
    return true;
  }
          
  /**
  * Diese Funktion ueberprueft, ob sich mehrere Zimmer verbinden lassen,
  * damit den Wuenschen der Kinder entsprochen wird
  *
  */
  private static boolean zimmerverbindenMoeglich(ArrayList<Integer> zimmerNr) {
    for (int i = 0; i < zimmerNr.size(); i++) {
      for (int j = 0; j < zimmerNr.size(); j++) {
        if (i != j) {
          if (!zimmerliste.get(zimmerNr.get(i))
          .kannVerbinden(zimmerliste.get(zimmerNr.get(j)))) {        
            System.out.println("Es funktioniert nicht (Zimmer verbinden) !");
            return false;
          }
        }
      }
    }
    return true;
  }
          
  /**
  * Diese Funktion überprueft die Uebereinstimmung einer Person mit einem
  * Zimmer und ergänzt die Listen des angegebenen Zimmers mit den Listen der
  * letzten Person
  * 
  * @param lastLine
  *            ist entweder die Präferiertenliste oder null
  * @param zimmerNr
  *            ist die Nummer des zu überprüfenden Zimmers
  * @return returns true, wenn das Hinzufügen in das Zimmer möglich ist
  */
  private static boolean schreibePräferenzen(String lastLine, int zimmerNr) {
    try {
      String prefLine = lastLine;
      System.out.println(prefLine);
      if (prefLine.startsWith("+"))
        prefLine = prefLine.substring(2);
      if (!prefLine.isEmpty()) {
        String[] temp = prefLine.split(" ");
        for (int i = 0; i < temp.length; i++) {
          // hier wird die Wunschliste ruebergeschrieben
          
          if (zimmerliste.get(zimmerNr).istPersonUngewollt(temp[i])) {
            System.out.println("In das Zimmer kann nicht: " + temp[i]);
            return false;
          } else if (!zimmerliste.get(zimmerNr).existsZimmergenosse(temp[i])) {
            zimmerliste.get(zimmerNr).addZimmergenossen(temp[i]);
            System.out.println("Neue Person in dem Zimmer: " + temp[i]);
          }
        }
      }
      System.out.println("Die Preferiertenliste wurde geschrieben!");
      String dislikeLine = reader.readLine();
      System.out.println(dislikeLine);
      dislikeLine = dislikeLine.substring(2);
      if (!dislikeLine.isEmpty()) {
        String[] temp = dislikeLine.split(" ");
        for (int i = 0; i < temp.length; i++) {
          // hier wird die Ungewunschtenliste ruebergeschrieben
          if (zimmerliste.get(zimmerNr).existsZimmergenosse(temp[i])) {
            System.out.println("Person mag nicht: " + temp[i] + " aus dem Zimmer");
            return false;
          } else if (!zimmerliste.get(zimmerNr).istPersonUngewollt(temp[i])) {
            zimmerliste.get(zimmerNr).addUngewolltenZimmergenossen(temp[i]);
            System.out.println("ungewuenschte Person im Zimmer" + zimmerNr + ": " + temp[i]);
          }
        }
      }
      
    } catch (IOException e) {
      System.err.println("Fehler beim Schreiben der Preferierten-/Ungewuenschtenzeile!");
      e.printStackTrace();
    }
    return true;
  }
          
}