# Communications

**So what?** Emergency calls, hospital links and the grid's own controls all travel over networks that run down quickly when the power fails. The design treats a network failure as a condition every other sector must be built to work through, not as a side issue.

**Depends on:** Energy
**Depended on by:** Emergency Services, Healthcare and Public Health, Energy, Financial Services

## Sector framework — Communications Sector Framework (DBA-COMM_Sector_Framework)
A sector framework states what a sector's systems must be built to withstand, from ordinary failures up to a deliberate, sustained attack. This one covers the networks that carry calls, data, emergency alerts and timing signals, and it sorts them by the job they do rather than by administrative labels. It treats the failure of a communications facility as the moment when every other sector's plan for lost communications begins. It also records that no existing communications instrument sets out a design basis, and that the dependence on electric power runs in both directions.
*Source: DBA-COMM_Sector_Framework_v0_15*

## Facility class — Access and Edge (DBA-COMM-AC-FC2)
A facility class takes the sector framework down to one kind of facility. This one covers the access and edge of the network: the cell sites, central offices, local lines and broadcast transmitters where service is handed to people and to the facilities that depend on it. It is the part of the network that runs out of power first when the grid fails. The class sets out two measures, how long a site keeps going on its own power and how much service survives, and asks that every 911 center and hospital keep at least one working path. It also states what protection cannot do against a determined attacker.
*Source: DBA-COMM-AC-FC2_Access_and_Edge_v0_4*

## Use case — Grid Denied and Critical Access Sites Struck (DBA-COMM-UC-2)
A use case runs a postulated attack forward through a facility class to see where the design holds and where it does not. Here a capable adversary denies the grid across an area and strikes the facilities that serve its emergency services and main hospital. The case shows that power switching at the sites, which acts on conditions measured at each site and cannot be reached from outside, holds. It also shows that backup paths which each pass their own test can share something hidden, leaving both the 911 center and the hospital with none. Past a point, the class hands the problem to emergency communications that do not use the public network. This document is available to defenders and regulators on request.
*Source: DBA-COMM-UC-2_Grid_Denied_Access_Sites_Struck_v0_1*

## Reference event — CenturyLink Outage (DBA-COMM-RE-13)
A reference event reads a real event back through the design basis to ask whether the method was sufficient. In December 2018 a fault in one piece of equipment set off a flood of repeated internal messages across CenturyLink's long-distance network. Service, including 911 for some seventeen million customers in twenty-nine states, was disrupted for almost thirty-seven hours. The event was not military action: nobody chose it, no actor was present, and nothing was aimed. Denial was present only in effect. Two regulators differ on where responsibility for the 911 losses in Washington State lies, and the instrument makes no finding between them.
*Source: DBA-COMM-RE-13_CenturyLink_Outage_v0_2*
