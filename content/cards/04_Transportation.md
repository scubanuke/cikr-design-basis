# Transportation

**So what?** Nearly every other sector's goods arrive by road, rail, water or air, and the movement itself runs on power, communications and satellite timing. A few concentrated points, such as a major port or a long bridge, carry a disproportionate share of the flow.

**Depends on:** Energy, Communications
**Depended on by:** Energy, Chemical, Food and Agriculture, Critical Manufacturing

## Sector framework — Transportation Sector Framework (DBA-TRAN_Sector_Framework)
A sector framework states what a sector's systems must be built to withstand, from ordinary accidents up to a deliberate, sustained attack. This one covers aviation, rail and transit, shipping and inland waterways, and highways. Instead of organizing by mode, it organizes by function: the places where movement gathers, the routes it travels, the vehicles that carry it, and the control that grants permission to move. It does not let a facility count on electric power, communications or satellite positioning and timing staying available when their loss is itself one of the events planned for. It also states plainly that no design makes the sector proof against a state that sets out to stop it.
*Source: DBA-TRAN_Sector_Framework_v0_11*

## Facility class — Nodes and Terminals (DBA-TRAN-ND-FC1)
A facility class takes the sector framework down to one kind of facility. This one covers nodes: airports, seaports, rail yards, transit stations and truck terminals, where movement gathers and changes hands. A small number of nodes carry a large share of the nation's movement, so losing one is not a local event. The class weighs two harms: goods that cannot move, and people inside the node who must reach safety. It finds that a node's fallback is a rate, not a switch. When systems fail, the node falls back to working by hand, more slowly, for as long as its people and paper last.
*Source: DBA-TRAN-ND-FC1_Nodes_and_Terminals_v0_3*

## Use case — Denial of a Strategic Seaport During a Deployment (DBA-TRAN-UC-1)
A use case runs a postulated attack forward through a facility class to see where the design holds and where it does not. Here a capable adversary denies a strategic seaport needed for a military deployment, while the ports that could take its traffic are also struck or full. The case shows that most of the physical design holds and that the port can keep working by hand, though only for cargo whose records it can trust. But working by hand moves less, and the shortfall accumulates. Once access is closed and the alternatives are gone, nothing inside the fence restores the flow. That answer lies with the routes, the control of movement and the national response. This document is available to defenders and regulators on request.
*Source: DBA-TRAN-UC-1_Strategic_Seaport_Denial_v0_2*

## Reference event — Key Bridge Collapse (DBA-TRAN-RE-8)
A reference event reads a real event back through the design basis to ask whether the method was sufficient. On 26 March 2024 the containership Dali lost power near Baltimore and struck a pier of the Francis Scott Key Bridge. The bridge collapsed, six members of a highway maintenance crew died, and the shipping channel beneath reopened in stages, fully restored only after seventy-six days. The National Transportation Safety Board found an electrical failure aboard the ship as the probable cause. None of the four marks of military action was present. The event showed what one span can do when it carries two routes at once, a highway and a channel.
*Source: DBA-TRAN-RE-8_Key_Bridge_Collapse_v0_2*
