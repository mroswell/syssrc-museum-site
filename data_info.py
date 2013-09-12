##some important artifacts
from artifacts.models import Artifact

items = []

CURTA_TITLE = "Curta Calculator"
CURTA_PRICE = "$125-$165"
CURTA_DESCRIPTION = "The Curta is a small, hand-cranked mechanical calculator introduced in 1948. It has an extremely compact design, a small cylinder that fits in the palm of the hand. It can be used to perform addition, subtraction, multiplication, division, and, with more difficulty, square roots and other operations. The Curta's design is a descendant of Gottfried Leibniz's Stepped Reckoner and Thomas's Arithmometer, accumulating values on cogs, which are added or complemented by a stepped drum mechanism."
CURTA = Artifact(title=CURTA_TITLE, price=CURTA_PRICE, description=CURTA_DESCRIPTION)
items.append(CURTA)

DIGI_COMP_TITLE = "Digi-Comp Computer"
DIGI_COMP_PRICE = "$4.95-$49"
DIGI_COMP_DESCRIPTION = "The Digi-Comp is a plastic mechanical computer from the 1960s. It offered three bits of tabletop computing. The machine arrived in kit form; your first task was to assemble the jumble of tubes, rods, and elastic bands into something that resembles a parking garage. Once complete, it's a fantastic hands-on way to teach Boolean algebra and binary numbers."
DIGI_COMP = Artifact(title=DIGI_COMP_TITLE, price=DIGI_COMP_PRICE, description=DIGI_COMP_DESCRIPTION)
items.append(DIGI_COMP)

LINOTYPE_TITLE = "Linotype Typesetter"
LINOTYPE_PRICE = "$3150-$6843"
LINOTYPE_DESCRIPTION = 'The linotype machine operator enters text on a 90-character keyboard. The machine assembles matrices, which are molds for the letter forms, in a line. The assembled line is then cast as a single piece, called a slug, in a process known as "hot metal" typesetting. The casting material is an alloy of lead (85%), antimony (11%), and tin (4%), and produces a one-piece casting slug capable of 300,000 impressions before the casting begins to develop deformities and imperfections, and the type must be cast again.The matrices are then returned to the type magazine from which they came, to be reused later. This allows much faster typesetting and composition than original hand composition in which operators place down one pre-cast metal punctuation mark or at a time.'
LINOTYPE = Artifact(title=LINOTYPE_TITLE, price=LINOTYPE_PRICE, description=LINOTYPE_DESCRIPTION)
items.append(LINOTYPE)

UNIVAC_TITLE = "Univac Computer"
UNIVAC_PRICE = "N/A"
UNIVAC_DESCRIPTION = "The Univac 490 was a 30-bit word core memory machine with 16K or 32K words; 4.8  microsecond cycle time made by UNIVAC. It was a commercial derivative of a computer Univac Federal Systems developed for the United States Navy. That system was the heart of the Naval Tactical Data System which pioneered the use of shipboard computers for air defense."
UNIVAC = Artifact(title=UNIVAC_TITLE, price=UNIVAC_PRICE, description=UNIVAC_DESCRIPTION)
items.append(UNIVAC)

