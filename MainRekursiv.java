package de.zimmerbelegung.java;

import java.io.*;
import java.util.ArrayList;

public class MainRekursiv {

	private static ArrayList<Zimmer> zimmerliste = new ArrayList<>();
	private static File file = new File("zimmerbelegung1.txt");
	private static FileReader fr;
	private static BufferedReader reader;

	public static void main(String[] args) {

		try {
			fr = new FileReader(new File("rsc/" + file));
			reader = new BufferedReader(fr);

			if (checkPersonGrouping()) {
				System.out.println("Es funktioniert!");
				for (int i = 0; i < zimmerliste.size(); i++) {
					System.out.println("Das " + i + ". Zimmer: ");
					zimmerliste.get(i).writeZimmergenossen();
				}
			} else {
				System.out.println("Diese Schueler koennen sich auf keine Zimmerbelegung einigen!");
			}

		} catch (IOException e) {
			System.err.println("Die Datei " + file + " konnte nicht bearbeitet werden!");
		}

	}

	private static boolean checkPersonGrouping() {
		String line;
		try {
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
			boolean schonInZimmer = false;
			for (int i = 0; i < zimmerliste.size(); i++) {
				// hier wird Ueberprueft, ob diese Person schon einem Zimmer
				// angehoert
				if (zimmerliste.get(i).existsZimmergenosse(name)) {
					System.out.println("Die Person " + name + " gehoert Zimmer " + i + " an.(Meth1)");
					if (!checkWritePreferences(i)) {
						// falls es false zurueckgibt, muss abgebrochen werden
						System.out.println("Es funktioniert nicht (Meth1) !");
						return false;
					}
					schonInZimmer = true;
					break;
				}
			}
			if (!schonInZimmer) {
				// die Person ist noch kein Mitglied eines Zimmers
				System.out.println("Die Person gehoert bisher zu keinem Zimmer!");
				line = reader.readLine();
				if (line.startsWith("+")) {
					// die Preferiertenliste der einen Person
					line = line.substring(2);
					boolean kenntPersonAusGruppe = false;
					if (!line.isEmpty()) {
						String[] temp = line.split(" ");
						for (int i = 0; i < zimmerliste.size(); i++) {
							for (int j = 0; j < temp.length; j++) {
								if (zimmerliste.get(i).existsZimmergenosse(temp[j])) {
									if (!zimmerliste.get(i).istPersonUngewollt(name)) {
										System.out.println("Es wurde ein Zimmer fuer " + name + " gefunden! " + i);
										zimmerliste.get(i).addZimmergenossen(name);
										checkWritePreferences(line, i);
										kenntPersonAusGruppe = true;
										break;
										/*
										 * falls die Person mit Personen aus
										 * versch. Zimmern im Zimmer sein
										 * möchte, es kann sein, dass es möglich
										 * ist, die Zimmer zu verbinden
										 * 
										 */
									} else if (zimmerliste.get(i).istPersonUngewollt(name)) {
										System.out.println("Zimmer " + i + " mag nicht, dass " + temp[j] + " zu ihnen kommt!");
										return false;
									}
								}

							}
						}

					}
					if (!kenntPersonAusGruppe) {
						// ein neues Zimmer wird angelegt
						System.out.println("Ein neues Zimmer mit " + name);
						zimmerliste.add(new Zimmer(name));
						if (!writeNewPersonPreferences(line)) {
							// Diese Methode bricht ab falls kein neues Zimmer
							// erstellt werden kann
							System.out.println("Es funktioniert nicht (Meth3) !");
							return false;
						}
					}
				}
			}
			for (int i = 0; i < zimmerliste.size(); i++) {
				System.out.println("Das " + i + ". Zimmer: ");
				zimmerliste.get(i).writeZimmergenossen();
			}

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

	private static boolean checkWritePreferences(int zimmerNr) {
		// Diese Methode Ueberprueft die Uebereinstimmung der Person mit dem
		// Zimmer
		System.out.println("Bearbeiten von Zimmer: " + zimmerNr);
		try {
			String line = reader.readLine();
			if (line.startsWith("+")) {
				// die Preferiertenliste der einen Person
				System.out.println(line);
				line = line.substring(2);
				if (!line.isEmpty()) {
					String[] temp = line.split(" ");
					for (int i = 0; i < temp.length; i++) {
						// testet, ob die Freunde der ungewolltenListe des
						// Zimmers widersprechen
						if (zimmerliste.get(zimmerNr).istPersonUngewollt(temp[i])) {
							System.out.println("Freundin: " + temp[i] + " kann nicht mit in das Zimmer!");
							return false;
						} else if (!zimmerliste.get(zimmerNr).existsZimmergenosse(temp[i])) {
							zimmerliste.get(zimmerNr).addZimmergenossen(temp[i]);
							System.out.println("Neue Person im Zimmer " + zimmerNr + ": " + temp[i]);
						}
					}
				}
				System.out.println("Die Preferiertenliste wurde überprüft!");
			}
			line = reader.readLine();
			if (line.startsWith("-")) {
				// die Ungewuenschtenliste der einen Person
				System.out.println(line);
				line = line.substring(2);
				if (!line.isEmpty()) {
					String[] temp = line.split(" ");
					for (int i = 0; i < temp.length; i++) {
						System.out.println(temp[i]);
						if (zimmerliste.get(zimmerNr).existsZimmergenosse(temp[i])) {
							System.out.println("Person mag nicht: " + temp[i] + " aus dem Zimmer");
							return false;
						} else if (!zimmerliste.get(zimmerNr).istPersonUngewollt(temp[i])) {
							zimmerliste.get(zimmerNr).addUngewolltenZimmergenossen(temp[i]);
							System.out.println("ungewuenschte Person im Zimmer " + zimmerNr + ": " + temp[i]);
						}
					}
				}
			}
			System.out.println("Fertig mit der Person!");
		} catch (IOException e) {
			System.err.println("Fehler beim Bearbeiten der Preferierten-/Ungewuenschtenzeile!");
			e.printStackTrace();
		}
		return true;
	}

	private static boolean checkWritePreferences(String prefLine, int zimmerNr) {
		// Diese Methode Ueberprueft die Uebereinstimmung der Person mit dem
		// Zimmer
		System.out.println("Bearbeiten von Zimmer: " + zimmerNr);
		try {
			String line = prefLine;
			System.out.println("+ " + line);
			// die Preferiertenliste der einen Person
			if (!line.isEmpty()) {
				String[] temp = line.split(" ");
				for (int i = 0; i < temp.length; i++) {
					// testet, ob die Freunde der ungewolltenListe des Zimmers
					// widersprechen
					if (zimmerliste.get(zimmerNr).istPersonUngewollt(temp[i])) {
						System.out.println("In das Zimmer kann nicht: " + temp[i]);
						return false;
					} else if (!zimmerliste.get(zimmerNr).existsZimmergenosse(temp[i])) {
						zimmerliste.get(zimmerNr).addZimmergenossen(temp[i]);
						System.out.println("Neue Person in dem Zimmer: " + temp[i]);
					}
				}
			}
			System.out.println("Die Preferiertenliste wurde überprüft!");
			line = reader.readLine();
			if (line.startsWith("-")) {
				// die Ungewuenschtenliste der einen Person
				line = line.substring(2);
				if (!line.isEmpty()) {
					String[] temp2 = line.split(" ");
					for (int i = 0; i < temp2.length; i++) {
						if (zimmerliste.get(zimmerNr).existsZimmergenosse(temp2[i])) {
							System.out.println("Person mag nicht: " + temp2[i] + " aus dem Zimmer");
							return false;
						} else if (!zimmerliste.get(zimmerNr).istPersonUngewollt(temp2[i])) {
							zimmerliste.get(zimmerNr).addUngewolltenZimmergenossen(temp2[i]);
							System.out.println("ungewuenschte Person im Zimmer" + zimmerNr + ": " + temp2[i]);
						}
					}
				}
			}
			System.out.println("Fertig mit der Person!");
		} catch (IOException e) {
			System.err.println("Fehler beim Bearbeiten der Preferierten-/Ungewuenschtenzeile (Meth2)!");
			e.printStackTrace();
		}

		return true;
	}

	private static boolean writeNewPersonPreferences(String prefLine) {
		// hier wird der Wunsch einer neuen Person fuer ein Zimmer festgelegt
		System.out.println("Hinzufuegen von Zimmer: " + (zimmerliste.size() - 1));
		try {
			String line = prefLine;
			System.out.println("+ " + line);
			// die Preferiertenliste der einen Person
			if (!line.isEmpty()) {
				String[] temp = line.split(" ");
				for (int i = 0; i < temp.length; i++) {
					// hier wird die komplette Wunschliste ruebergeschrieben
					zimmerliste.get(zimmerliste.size() - 1).addZimmergenossen(temp[i]);
					System.out.println("Neue Person in dem Zimmer: " + temp[i]);
				}
			}
			System.out.println("Die Preferiertenliste wurde geschrieben!");
			line = reader.readLine();
			System.out.println(line);
			if (line.startsWith("-")) {
				// die Ungewuenschtenliste der einen Person
				line = line.substring(2);
				if (!line.isEmpty()) {
					String[] temp2 = line.split(" ");
					for (int i = 0; i < temp2.length; i++) {
						// hier wird die komplette Ungewunschtenliste
						// ruebergeschrieben
						zimmerliste.get(zimmerliste.size() - 1).addUngewolltenZimmergenossen(temp2[i]);
						System.out.println("ungewuenschte Person in dem Zimmer: " + temp2[i]);
					}
				}
			}
			System.out.println("Fertig mit der Person!");
		} catch (IOException e) {
			System.err.println("Fehler beim Bearbeiten der Preferierten-/UngewÃ¼nschtenzeile (Meth3)!");
			e.printStackTrace();
		}

		return true;
	}

}
