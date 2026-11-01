# Financial Services

**So what?** Paychecks, pensions, fuel and food purchases all settle through a few payment systems. The design treats the power and communications those systems run on as part of the problem, and asks how ordinary people keep paying through a long outage.

**Depends on:** Communications, Energy
**Depended on by:** All other sectors

## Sector framework — Financial Services Sector Framework (DBA-FIN_Sector_Framework)
A sector framework states what a sector's systems must be built to withstand, from ordinary accidents up to deliberate, sustained attack. Financial Services makes no physical product, so this one is organized by function: moving money so that a payment is final, running markets, and keeping accounts. It relies on other sectors for data centers, networks and power, and it counts those dependencies as part of its own design. Its proposed distinctive measure is the window in which a payment must become final before a failure spreads to everyone waiting on it. Beyond a threshold, the framework states, such a failure erodes the public confidence the monetary system rests on.
*Source: DBA-FIN_Sector_Framework_v0_5*

## Facility class — Payment and Settlement (DBA-FIN-PS-FC1)
A facility class takes the sector framework down to one kind of facility. This one is payment and settlement: the systems and bank connections through which money moves between institutions and a payment becomes final. It is a function, not a building. The class names two ways to fail: a payment that cannot settle in time, and a payment that settles on a false instruction. It sets out how a system keeps settling when power, networks and timing are lost, how instructions are checked before they become final, and how records are verified before work resumes. It declares what remains beyond its design.
*Source: DBA-FIN-PS-FC1_Payment_and_Settlement_v0_2*

## Use case — Settlement Through a Campaign on the Grid and Communications (DBA-FIN-UC-1)
A use case runs a postulated scenario forward through a facility class to see where the design holds and where it does not. Here a country's power and communications are struck for months, and an adversary also corrupts a major bank's payment records and instructions while the settlement system keeps running from reserve sites. The case finds the plan consistent with the real wartime record, though whether settlement holds through the hardest phases remains in question, and shows that a check before payments become final can hold back large or unusual instructions. It leaves open how many times a day the system can verify its records and resume, and how it tells deliberate interference from ordinary outage. This document is available to defenders and regulators on request.
*Source: DBA-FIN-UC-1_Settlement_Through_a_Campaign_on_the_Grid_and_Communications_v0_1*

## Reference event — Ukraine's Payment System Through the War (DBA-FIN-RE-3)
A reference event reads a real event back through the design basis to ask whether the method was sufficient. Ukraine's central bank reports that since the full-scale invasion of February 2022 its main interbank payment system has kept working, from reserve sites, through strikes on the electricity system that began in October 2022. Banks were allowed to use computing hosted abroad, and a network of branches with their own power, more than 2,370 by July 2023, served the public. All four marks of military action are established on the record. The design held at the center. Public access held only because that branch network was built, and the permission to use computing abroad came only after the war began.
*Source: DBA-FIN-RE-3_Ukraines_Payment_System_Through_the_War_v0_2*
