# Emergency Services

**So what?** When a storm or an attack takes down power, phones and roads, emergency services must keep going. The example shows a 911 center can be powered and staffed yet hear nothing, so what lies upstream matters as much as the building.

**Depends on:** Communications, Energy, Transportation, Healthcare and Public Health, Water
**Depended on by:** All other sectors (the framework calls Emergency Services "the mitigation layer for every other sector")

## Sector framework — Emergency Services Sector Framework (DBA-ESS_Sector_Framework)
A sector framework states what a sector's systems must be built to withstand, from ordinary accidents up to deliberate military action. This one covers taking emergency calls and dispatching help, the police, fire and medical forces themselves, and the management of emergencies. Its defining idea is operate-through. Responders are called precisely when power, communications and roads are failing, so the sector cannot assume they are available and must keep working through their loss. The framework also treats the sector as the mitigation layer for every other sector, so a weakened response makes every other failure worse.
*Source: DBA-ESS_Sector_Framework_v0_11*

## Facility class — Public-Safety Answering and Dispatch (DBA-ESS-AD-FC1)
A facility class takes the sector framework down to one kind of facility. This one covers 911 centers and what they rely on: the systems that show where a caller is and recommend which units to send, and the radio systems that carry instructions to the field. A center may be a single room, yet it is the only place in its area where an emergency call is answered. The class sets out how a center keeps answering and dispatching through loss of power, networks and neighbors. It also states what its design cannot cover, such as a failure of call delivery across every carrier, which no center can repair.
*Source: DBA-ESS-AD-FC1_Public-Safety_Answering_and_Dispatch_v0_5*

## Use case — The Compound Failure the Sector Must Operate Through (DBA-ESS-UC-1)
A use case runs a postulated scenario forward through the design to see where it holds and where it does not. This is a sector-wide case, not one issued under the dispatch class. A capable adversary takes down a region's power grid and the supplies, links and routes that emergency services stand on, without attacking the services themselves. The case shows that the protective equipment at 911 centers, radio sites and stations holds, but only for as long as supplies last. What fails is endurance. It also finds that the sector lasts only as long as its shortest link from call to response, and that all three functions draw on the same fuel and the same people. This document is available to defenders and regulators on request.
*Source: DBA-ESS-UC-1_Compound_Failure_Operate-Through_v0_2*

## Reference event — Derecho 911 Outages (DBA-ESS-RE-1)
A reference event reads a real event back through the design basis to ask whether the method was sufficient. On the night of 29 June 2012 a derecho, a long-lived windstorm, cut power across the Mid-Atlantic. On the federal regulator's account, seventy-seven 911 centers in six states serving more than 3.6 million people lost some connectivity, and seventeen centers in three states lost service completely. Fairfax County's center had its own power and staff, yet for seven hours no 911 call reached it, because the failures lay in the telephone network upstream. None of the four marks of military action was present.
*Source: DBA-ESS-RE-1_Derecho_911_Outages_v0_2*
