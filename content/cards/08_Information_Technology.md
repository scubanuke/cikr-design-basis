# Information Technology

**So what?** Almost every organization runs on software it did not write, so one bad update can reach hospitals, call centers and banks at once. The design asks that no vendor's update be able to change a facility's safety controls without the facility's own deliberate act.

**Depends on:** Energy, Communications, Critical Manufacturing, Transportation
**Depended on by:** All other sectors

## Sector framework — Information Technology Sector Framework (DBA-IT_Sector_Framework)
A sector framework states what a sector's systems must be built to withstand, from ordinary accidents up to deliberate, sustained attack. This one covers the unseen layer of computing: the naming and trust services that tell computers where to go and whom to believe, the cloud services that run on shared machines, and the software every other sector installs. Its distinctive point is that serious harm here needs no physical failure. A trusted update or a compromised trust service can reach every dependent system at once while every building keeps running. So the framework measures consequence by how far a failure spreads, not by how long it lasts.
*Source: DBA-IT_Sector_Framework_v0_6*

## Facility class — Software, Hardware and Product Supply Chain (DBA-IT-SW-FC3)
A facility class takes the sector framework down to one kind of facility. Here it is not a building but a pathway: the making and delivery of the software products that other sectors install and keep updated. The class sets out that a vendor's signature shows where an update came from, not that it is sound, so what ships must be shown to match what was reviewed, and each customer keeps authority over what enters its own systems. It calls for updates released in stages, so a mistake reaches few machines before it is seen, and for recovery that does not depend on the channel that failed. It also declares what remains beyond its design when an adversary is deliberate.
*Source: DBA-IT-SW-FC3_Software_Hardware_and_Product_Supply_Chain_v0_2*

## Use case — A Capability Pre-Positioned in a Trusted Product (DBA-IT-UC-1)
A use case runs a postulated scenario forward through a facility class to see where the design holds and where it does not. Here a capable adversary quietly places a hidden capability in a widely trusted software product, then uses it during an attack on the power grid to disable the computers of hospitals, emergency call centers and utilities together. The case shows that where facilities kept their safety and treatment controls out of the product's reach, the damage stops at the computers and those controls keep protecting. Recovery is the weak point. Rebuilding by a facility's own staff was rehearsed with networks up and help available, and those conditions would be gone. This document is available to defenders and regulators on request.
*Source: DBA-IT-UC-1_Pre-Positioned_Capability_Activated_During_a_Grid_Attack_v0_1*

## Reference event — Faulty Content Update of 19 July 2024 (DBA-IT-RE-2)
A reference event reads a real event back through the design basis to ask whether the method was sufficient. On 19 July 2024 a faulty content update to a widely used security product stopped about 8.5 million computers. The vendor reversed it after 78 minutes, but many machines had to be repaired by hand. Some emergency call centers fell back to taking calls by hand, and at a House hearing members described disruption at hospitals, banks and airlines. It was an accident, not an attack, and the reading makes no finding of fault. Read against the event, the class held, with gaps, among them that recovery should be measured to the service, not the machine.
*Source: DBA-IT-RE-2_Faulty_Content_Update_of_19_July_2024_v0_1*
