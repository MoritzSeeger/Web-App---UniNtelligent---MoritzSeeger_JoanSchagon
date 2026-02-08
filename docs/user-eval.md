---
title: User Evaluation
nav_order: 4
---

{: .label }
[Jane Dane]

{: .no_toc }
# User evaluation

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: [Title]

### Meta
**Status**
Done
**Updated**
19.12.2025

### Goal
Das Ziel dieser Evaluation war es zu prüfen, wie effizient Studierende einen spezifischen Kurs (z. B. Statistik) finden und ob die bereitgestellten Kriterien ausreichen, um eine fundierte Entscheidung zwischen verschiedenen Dozenten (Dozent A, B oder C) zu treffen. Wir wollten wissen, ob der Weg zum Ziel "strukturiert und ohne Umwege" verläuft.

### Method
Wir haben einen Usability-Test mit Kommilitonen der HWR Berlin durchgeführt. Den Testern wurde ein Laptop mit der laufenden Anwendung übergeben. 
**Aufgabe:** "Du musst im nächsten Semester Statistik belegen. Nutze UniNtelligent, um die verfügbaren Dozenten für diesen Kurs zu finden und entscheide dich basierend auf deinem Lernstil für einen der Dozenten."
Während des Prozesses haben wir beobachtet, wie intuitiv die Navigation durch die Fachbereiche und Kurse wahrgenommen wurde.

### Results
* **Datenbank & Performance:** Die Datenbankanbindung funktionierte reibungslos. Die Kurse und zugehörigen Dozenten wurden korrekt und schnell geladen. 
* **Navigation:** Die Testpersonen fanden den Kurs "Statistik" ohne größere Umwege, was zeigt, dass die Pfade logisch strukturiert sind.
* **Design-Hürden:** Die größte Schwierigkeit lag im visuellen Design. Testpersonen brauchten teilweise einen Moment, um die neutralen Kriterien (Stil statt Note) richtig zu interpretieren. Ein rein neutrales Empfehlungssystem ohne die gewohnten "Sterne-Bewertungen" war für einige Nutzer anfangs ungewohnt.

### Implications
* **Neutralität stärken:** Da das Feedback zeigte, dass neutrale Empfehlungen schwerer zu greifen sind als Noten, haben wir die Beschreibungen der Kriterien im Frontend präzisiert.
* **UI/UX Refinement:** Basierend auf der Rückmeldung zum Design haben wir das Custom CSS angepasst, um die Übersichtlichkeit der Dozenten-Profile zu verbessern und die Vergleichbarkeit der Kriterien optisch deutlicher hervorzuheben. 
* **Skalierung:** Das Feedback bestätigt, dass das System für die HWR funktioniert; für eine Erweiterung sollten wir jedoch überlegen, ein Onboarding-Element einzuführen, das das Konzept der "Stil-Bewertung" kurz erklärt.
---
