---
title: Design Decisions
nav_order: 3
---

{: .label }
[Jane Dane]

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Design Decisions

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: 19.12.2025

### Problem statement

Für das Projekt "ProfMatch" mussten wir eine technische Basis wählen, die sowohl die Anforderungen des Kurses erfüllt als auch eine faire, objektive Informationsgrundlage für Studierende schafft. Das Hauptproblem bei bestehenden Lösungen ist oft die Subjektivität: Studierende bewerten Dozenten schlecht, nur weil eine Prüfung schwer war. Unser Ziel war es, ein System zu schaffen, das Eigenschaften (Stil) statt Noten (Leistung) in den Vordergrund stellt und technisch simpel bleibt

### Decision

Wir haben uns für einen monolithischen Flask-Stack mit SQLite und Custom CSS entschieden. Die Entscheidung basiert auf folgenden Faktoren:

Vorgabe & Fokus: Flask und Jinja2 waren Kursvorgaben. Wir haben uns entschieden, die Komplexität niedrig zu halten, um uns auf die Logik des Matching-Algorithmus zu konzentrieren.

Datenhaltung: Wir nutzen Plain SQL statt SQLAlchemy. Da unsere Datenstruktur stabil ist und nur wenige Schreibzugriffe durch User erfolgen. 

Neutralität: Das System wurde gezielt so entworfen, dass es kein klassisches Sterne-Rating gibt. Wir nutzen vordefinierte Kategorien (z.B. Kursstil, Arbeitsaufwand), um eine objektive Einschätzung statt einer emotionalen Bewertung zu ermöglichen.

### Regarded options

Option 1: Database Access - Plain SQL vs. SQLAlchemy | Criterion | Plain SQL (Chosen) | SQLAlchemy | | --- | --- | --- | | Know-how | ✔️ Vorhandene SQL-Kenntnisse konnten direkt genutzt werden | ❌ Hohe Lernkurve für ORM-Konzepte & Syntax | | Complexity | ✔️ Schlankes System ohne zusätzlichen Abstraktionslayer | ❌ Overkill für ein Projekt mit stabilen Datenstrukturen | | Change DB schema | ❌ SQL über den Code verteilt; manuelle Updates nötig | ❔ Gut: Klassen-Struktur, bad: braucht Alembic |

Option 2: Styling - Custom CSS vs. Bootstrap | Criterion | Custom CSS (Chosen) | CSS Frameworks | | --- | --- | --- | | Control | ✔️ Volle Freiheit über das Branding und Layout | ❌ Eingeschränkt durch Standard-Komponenten | | Performance | ✔️ Minimaler Code; kein Laden ungenutzter Klassen | ❌ Große Libraries verursachen unnötigen Overhead |

---

