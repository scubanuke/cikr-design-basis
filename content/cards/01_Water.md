# Water

**So what?** Nearly everything a water system does runs on electricity, and nearly everything a town does runs on water: hospitals, dialysis, firefighting, food. The design treats both directions as part of the problem, not as someone else's.

**Depends on:** Energy, Chemical
**Depended on by:** Healthcare and Public Health, Emergency Services, Energy, Nuclear, Food and Agriculture

## Sector framework — Water Sector Framework (DBA-W-Sector_Framework)
A sector framework states what a sector's systems must be built to withstand, from floods and long power outages up to a deliberate, sustained attack. This one covers drinking water and wastewater, and it names three functions that must hold: safe drinking water, contained wastewater, and protection of public health. It does not let a utility count on the power grid or chemical deliveries staying available when their loss is itself one of the events planned for. It also asks that what operators see on their screens be trustworthy, not merely present, because every manual safeguard depends on an operator acting on an accurate picture.
*Source: DBA-W-Sector_Framework_v1_16*

## Facility class — Water Treatment Plant (DBA-W-FC1)
A facility class takes the sector framework down to one kind of facility. This one is the treatment plant, where river or well water is made safe to drink, together with the chemical storage that disinfection depends on. A treatment plant carries two dangers at once: losing disinfection, which reaches every tap downstream, and a release of stored treatment chemicals, which reaches the neighborhood around the plant. The class sets out how a plant should settle into a safe condition on its own, with only a small crew, when it loses its networked controls and outside support, and it states plainly what remains beyond its design.
*Source: DBA-W-FC1_Water_Treatment_Plant_v0_6*

## Use case — Area-Denial Attack on a Large Surface-Water Treatment Plant (DBA-W-UC-1)
A use case runs a postulated attack forward through a facility class to see where the design holds and where it does not. Here a capable adversary strikes a large treatment plant's chemical storage, forcing the crew to leave, and interferes with the plant's controls at the same time. The case shows that a plant able to reach a safe state by itself defeats the control-system half of the attack and keeps the drinking-water consequence inside the fence. The chemical release is different. It crosses the fence line, and there the plant's design hands off to community emergency planning. This document is available to defenders and regulators on request.
*Source: DBA-W-UC-1_Area_Denial_Surface_Water_Plant_v0_3*

## Reference event — Minnesota Water Campaign (DBA-W-RE-1)
A reference event reads a real event back through the design basis to ask whether the method was sufficient. In late July 2026 a coordinated cyber attack disrupted controls at more than thirty Minnesota water and wastewater systems, the first-reported part of a campaign later counted at about a hundred facilities in at least twelve states. In the Minnesota cases officials said drinking-water quality was not affected, and at Braham crews restored the plant in about two hours. The event showed three of the four marks of military action; the fourth, denial, was absent, because crews could reach their plants. No official attribution has been made, and the record remains open.
*Source: DBA-W-RE-1_Minnesota_Water_Campaign_v0_8*
