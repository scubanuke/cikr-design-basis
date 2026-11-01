# Food and Agriculture

**So what?** Food reaches your table through a few large processing plants and a web of other systems: power, water, trucking, chemicals and finance. The design treats a failure at one of those plants as a safety question and a supply question at once.

**Depends on:** Energy, Water, Transportation, Chemical, Financial Services
**Depended on by:** All other sectors

## Sector framework — Food and Agriculture Sector Framework (DBA-FA_Sector_Framework)
A sector framework states what a sector's systems must be built to withstand, from ordinary accidents up to a deliberate, sustained attack. This one covers growing, processing, storing and distributing food. It holds that food carries two consequences, shortage and harm to health, and asks that they be kept separate. Farms are too many for any one to be critical, so the framework concentrates on chokepoints, above all the few large plants that handle a national share of a product. It also notes that the sector leans on five others at once, and treats the loss of several together as the governing case.
*Source: DBA-FA_Sector_Framework_v0_5*

## Facility class — Food Processing and Manufacturing (DBA-FA-FP-FC2)
A facility class takes the sector framework down to one kind of facility. This one is the plant where raw farm product becomes food, such as meat, dairy, grain, beverages and packaged goods. It follows two chains of harm: a plant that stops and cuts the supply, and a plant that releases unsafe food, with illness appearing days or weeks later. The two join when a plant finds a hazard, stops and holds its product. The class sets out how a plant should accept, release, hold, recall and restart, and states that no single plant can fully protect people from losing a major source of food.
*Source: DBA-FA-FP-FC2_Food_Processing_and_Manufacturing_v0_2*

## Use case — Deliberate Contamination at the Processing Chokepoint With Detection Denied (DBA-FA-UC-1)
A use case runs a postulated scenario forward through a facility class to see where the design holds and where it does not. Here an adversary deliberately contaminates food at a processing chokepoint. The consequence is illness across a large population before the cause is known, and the loss of the plant's share of supply. The case shows that the class's rules for stopping and holding product can limit the harm once the plant has a first credible sign of it, and it raises open questions about warning the public. This document is available to defenders and regulators on request.
*Source: DBA-FA-UC-1_Contamination_at_the_Chokepoint_With_Detection_Denied_v0_1*

## Reference event — Ransomware Attack on JBS (DBA-FA-RE-1)
A reference event reads a real event back through the design basis to ask whether the method was sufficient. At the end of May 2021 a ransomware attack on shared business computer systems led meat processor JBS to suspend them, and its U.S. beef plants stopped within a day. As reported, national cattle slaughter fell 22 percent and hogs 20 percent from a week earlier. On 2 June the company said the vast majority of its facilities had resumed. The Federal Bureau of Investigation attributed the attack to a criminal group. Denial was absent, and the event does not meet the threshold for military action. It showed that shared systems, not single plants, set the supply loss.
*Source: DBA-FA-RE-1_Ransomware_Attack_on_JBS_v0_1*
